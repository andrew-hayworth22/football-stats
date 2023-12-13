from bottle import HTTPResponse, route, run, template, redirect, post, put, request
import database.db as db

@route('/')
def get_index() :
    redirect('/home')

@route('/home')
def get_home() :
    return template("home.tpl", seasons = db.season_get_all())

#########################################################
# Seasons
#########################################################

# Create season screen
@route('/season')
def get_new_season() :
    return template("seasons/add.tpl", message="")

# Create season endpoint
@post('/season')
def create_season() :
    year = request.forms.get('year')
    
    if not year :
        return template("seasons/add.tpl", message = "Please fill out all required fields")
    
    if db.year_exists(year) :
        return template("seasons/add.tpl", message = "Season already exists")
    
    try :
        db.season_add(year)
    except :
        return HTTPResponse(status=500, body="There was an error creating the season")
    
    redirect('/home')

# Update season screen
@route('/season/<id>')
def get_season(id) :
    season = db.season_get(id)
    if season is None :
        return HTTPResponse(status=404, body='Season does not exist <div><a href="/home">Go back</a></div>')
        
    return template("seasons/edit.tpl", season = season, message="")

# Update season endpoint
@post('/season/<id>')
def update_season(id) :
    season = db.season_get(id)
    year = request.forms.get('year')
    
    if not year or not season :
        return template("seasons/update.tpl", message = "Please fill out all required fields")
    
    if not season :
        return template("seasons/update.tpl", message = "Season does not exist")
    
    try :
        db.season_update(id, year)
    except :
        return HTTPResponse(status=500, body="There was an error updating the season")
    
    redirect('/home')
    
# Delete season endpoint
@post('/season/<id>/delete')
def delete_season(id) :
    season = db.season_get(id)
    
    if not season :
        return template("seasons/update.tpl", message = "Season does not exist")
    
    try :
        db.season_delete(id)
    except :
        return HTTPResponse(status=500, body="There was an error deleting the season")
    
    redirect('/home')

#########################################################
# Teams
#########################################################

# Team list
@route('/teams')
def get_teams() :
    search = request.query.get('search') or ""
    return template("teams/list.tpl", teams = db.team_get_all(search), search=search)

# Create team screen
@route('/team')
def get_new_team() :
    return template("teams/add.tpl", message="")

# Create team endpoint
@post('/team')
def create_team() :
    location = request.forms.get('location')
    mascot = request.forms.get('mascot')
    
    if not location or not mascot :
        return template("teams/add.tpl", message = "Please fill out all required fields")
    
    try :
        result = db.team_add(location, mascot)
    except :
        return HTTPResponse(status=500, body="There was an error creating the team")
    
    redirect('/teams')

# Update team screen
@route('/team/<id>')
def get_team(id) :
    team = db.team_get(id)
    if team is None :
        return HTTPResponse(status=404, body='Team does not exist <div><a href="/teams">Go back</a></div>')
        
    return template("teams/edit.tpl", team = team, message="")

# Update team endpoint
@post('/team/<id>')
def update_team(id) :
    team = db.team_get(id)
    location = request.forms.get('location')
    mascot = request.forms.get('mascot')
    
    if not location or not mascot or not team :
        return template("teams/update.tpl", message = "Please fill out all required fields")
    
    if not team :
        return template("teams/update.tpl", message = "Team does not exist")
    
    try :
        db.team_update(id, location, mascot)
    except :
        return HTTPResponse(status=500, body="There was an error updating the team")
    
    redirect('/teams')

# Delete team endpoint
@post('/team/<id>/delete')
def delete_team(id) :
    team = db.team_get(id)
    
    if not team :
        return template("teams/update.tpl", message = "Team does not exist")
    
    try :
        db.team_delete(id)
    except :
        return HTTPResponse(status=500, body="There was an error deleting the team")
    
    redirect('/teams')

#########################################################
# Games
#########################################################

# Create game screen
@route('/season/<id>/game')
def get_new_team(id) :
    return template("games/add.tpl", teams = db.team_get_all(), season_id = id, message="")

# Create game endpoint
@post('/game')
def create_game() :
    home_team = db.team_get(request.forms.get('home_team'))
    away_team = db.team_get(request.forms.get('away_team'))
    season = db.season_get(request.forms.get('season'))
    
    if not home_team or not away_team or not season :
        return template("games/add.tpl", teams = db.team_get_all(), message = "Please fill out all required fields")
    
    id = db.game_add(home_team['id'], away_team['id'], season['id'])
    redirect('/game/' + str(id))
    
# Update game screen
@route('/game/<id>')
def get_game(id) :
    game = db.game_get(id)
    if game is None :
        return HTTPResponse(status=404, body='Game does not exist <div><a href="/games">Go back</a></div>')
        
    return template("games/edit.tpl", game = game, teams = db.team_get_all(), message="")

# Delete game endpoint
@post('/game/<id>/delete')
def delete_game(id) :
    game = db.game_get(id)
    
    if not game :
        return template("games/update.tpl", message = "Game does not exist")
    
    try :
        db.game_delete(id)
    except :
        return HTTPResponse(status=500, body="There was an error deleting the game")

    redirect('/season/' + str(game['season']['id']))

#########################################################
# Statlines
#########################################################

# Create statline screen
@route('/game/<game_id>/add_stats/<team>')
def get_new_statline(game_id, team) :
    is_home = team == "home"
    return template("statlines/add.tpl", game_id=game_id, is_home=is_home, message="")

# Create statline endpoint
@post('/statline')
def create_statline() :
    game_id = int(request.forms.get('game_id'))
    is_home = request.forms.get('is_home') == 'True'
    score = int(request.forms.get('score'))
    passing_yards = int(request.forms.get('passing_yards'))
    passing_attempts = int(request.forms.get('passing_attempts'))
    passing_completions = int(request.forms.get('passing_completions'))
    passing_touchdowns = int(request.forms.get('passing_touchdowns'))
    rushing_yards = int(request.forms.get('rushing_yards'))
    rushing_attempts = int(request.forms.get('rushing_attempts'))
    rushing_touchdowns = int(request.forms.get('rushing_touchdowns'))
    sacks = int(request.forms.get('sacks'))
    interceptions = int(request.forms.get('interceptions'))
    fumbles_recovered = int(request.forms.get('fumbles_recovered'))
    
    if not game_id:
        return template("statlines/add.tpl", game_id=game_id, is_home=is_home, message = "There was an error creating the statline")
    
    try :
        db.statline_add(game_id, is_home, score, passing_yards, passing_attempts, passing_completions, passing_touchdowns, rushing_yards, rushing_attempts, rushing_touchdowns, sacks, interceptions, fumbles_recovered)
    except Exception as e :
        print(e)
        return HTTPResponse(status=500, body="There was an error creating the statline")
    
    redirect('/game/' + str(game_id))

run(host="localhost", port=8080, debug=True)