from peewee import *
from playhouse.shortcuts import model_to_dict

db = SqliteDatabase('football-stats.db')
db.connect()
db.execute_sql('PRAGMA foreign_keys = ON;')

# Set up database
def db_set_up() :
    print("Setting up database...")
    
    # List of test teams
    teams = [
        { 'location': 'Philadelphia', 'mascot': 'Eagles' },
        { 'location': 'Washington', 'mascot': 'Commanders' },
        { 'location': 'Dallas', 'mascot': 'Cowboys' },
        { 'location': 'New York', 'mascot': 'Giants' }
    ]
    
    # Reset database tables
    db.drop_tables([Game, Statline, Team, Season], safe = True)
    db.create_tables([Season, Team, Statline, Game])

    # Add seasons
    Season.create(year = 2022)
    Season.create(year = 2023)

    # Add teams
    for team in teams :
        newTeam = Team(location = team['location'], mascot = team['mascot'])
        newTeam.save()
    
    # Add statlines
    Statline.create(score = 26, passing_yards = 132, passing_attempts = 15, passing_completions = 25, passing_touchdowns = 2, rushing_yards = 136, rushing_attempts = 39, rushing_touchdowns = 1, sacks = 0, interceptions = 3, fumbles_recovered = 0)
    Statline.create(score = 17, passing_yards = 181, passing_attempts = 18, passing_completions = 38, passing_touchdowns = 1, rushing_yards = 134, rushing_attempts = 26, rushing_touchdowns = 1, sacks = 4, interceptions = 0, fumbles_recovered = 0)
    
    # Add games
    Game.create(home_team = 1, home_team_statline = 1, away_team = 3, away_team_statline = 2, season = 1)
    Game.create(home_team = 1, home_team_statline = None, away_team = 3, away_team_statline = None, season = 2)
    
    # Ensure that the database was set up correctly
    seasons = season_get_all()
    assert len(seasons) == 2
    
    teams = team_get_all()
    assert len(teams) == 4
    
    statlines = statline_get_all()
    assert len(statlines) == 2
    
    games = game_get_all()
    assert len(games) == 2
    
    print("Database set up complete")

#########################################################
# Teams
#########################################################
class Team(Model) :
    location = CharField()
    mascot = CharField()
    class Meta :
        database = db

# Database Methods
def team_get_all(search = "") :
    teams = Team.select().where((Team.location + ' ' + Team.mascot).contains(search))
    teams = [model_to_dict(team) for team in teams]
    return teams

def team_get(id) :
    team = Team.get_or_none(Team.id == id)
    if team is not None :
        return model_to_dict(team)
    
    return None

def team_add(location, mascot) :    
    team = Team(location=location, mascot=mascot)
    team.save()
    return team.id

def team_update(id, location, mascot) :
    team = Team(id=id, location=location, mascot=mascot)
    team.save()

def team_delete(id) :
    Team.delete().where(Team.id == id).execute()
    
#########################################################
# Seasons
#########################################################

# Season Data Model
class Season(Model) :
    year = IntegerField(unique=True)
    class Meta :
        database = db

# Database Methods
def season_get_all() :
    seasons = [model_to_dict(season) for season in Season.select().order_by(Season.year.desc())]
    return seasons

def season_get(id) :
    season = (Season \
                .select(Season, Game) \
                .join(Game, JOIN.LEFT_OUTER, on=(Game.season == Season.id))\
                .where(Season.id == id) \
                .get_or_none())
    
    if season is not None :
        season_dict = model_to_dict(season)
        season_dict['games'] = [model_to_dict(game) for game in season.games]
        return season_dict
    return None

def year_exists(year) :
    return Season.get_or_none(Season.year == year) is not None

def season_add(year) :
    season = Season(year=year)
    season.save()
    return season.id
    
def season_update(id, year) :
    season = Season(id=id, year=year)
    season.save()

def season_delete(id) :
    Season.delete().where(Season.id == id).execute()

#########################################################
# Statlines
#########################################################
class Statline(Model) :
    score = IntegerField()
    passing_yards = IntegerField()
    passing_attempts = IntegerField()
    passing_completions = IntegerField()
    passing_touchdowns = IntegerField()
    rushing_yards = IntegerField()
    rushing_attempts = IntegerField()
    rushing_touchdowns = IntegerField()
    sacks = IntegerField()
    interceptions = IntegerField()
    fumbles_recovered = IntegerField()
    class Meta :
        database = db

# Database Methods
def statline_get_all() :
    statlines = [model_to_dict(statline) for statline in Statline.select()]
    return statlines

def statline_get(id) :
    statline = Statline.get_or_none(Statline.id == id)
    if statline is not None :
        return model_to_dict(statline)
    
    return None

def statline_add(game_id, is_home, score, passing_yards, passing_attempts, passing_completions, passing_touchdowns, rushing_yards, rushing_attempts, rushing_touchdowns, sacks, interceptions, fumbles_recovered) :    
    statline = Statline(score=score, passing_yards=passing_yards, passing_attempts=passing_attempts, passing_completions=passing_completions, passing_touchdowns=passing_touchdowns, rushing_yards=rushing_yards, rushing_attempts=rushing_attempts, rushing_touchdowns=rushing_touchdowns, sacks=sacks, interceptions=interceptions, fumbles_recovered=fumbles_recovered)
    statline.save()
    
    game = Game.get(Game.id == game_id)
    print("Saving to game: ", model_to_dict(game))
    print("is_home: ", is_home)
    print("ID TO SAVE: ", statline.id if is_home else game.home_team_statline)
    game_update(game.id, game.home_team, statline.id if is_home else game.home_team_statline, game.away_team, statline.id if not is_home else game.away_team_statline, game.season)
    
    return statline.id

def statline_update(id, score, passing_yards, passing_attempts, passing_completions, passing_touchdowns, rushing_yards, rushing_attempts, rushing_touchdowns, sacks, interceptions, fumbles_recovered) :
    statline = Statline(id=id, score=score, passing_yards=passing_yards, passing_attempts=passing_attempts, passing_completions=passing_completions, passing_touchdowns=passing_touchdowns, rushing_yards=rushing_yards, rushing_attempts=rushing_attempts, rushing_touchdowns=rushing_touchdowns, sacks=sacks, interceptions=interceptions, fumbles_recovered=fumbles_recovered)
    statline.save()
    
def statline_delete(id) :
    Statline.delete().where(Statline.id == id).execute()

#########################################################
# Games
#########################################################

# Game Data Model
class Game(Model) :
    home_team = ForeignKeyField(Team, backref='home_games', on_delete='CASCADE')
    home_team_statline = ForeignKeyField(Statline, null=True)
    away_team = ForeignKeyField(Team, backref='away_games', on_delete='CASCADE')
    away_team_statline = ForeignKeyField(Statline, null=True)
    season = ForeignKeyField(Season, backref='games', on_delete='CASCADE')
    
    class Meta :
        database = db

# Database Methods
def game_get_all() :
    HomeTeam = Team.alias()
    AwayTeam = Team.alias()
    
    games = Game.select(Game, HomeTeam, AwayTeam) \
            .join(HomeTeam, on=(Game.home_team == HomeTeam.id)) \
            .switch(Game) \
            .join(AwayTeam, on=(Game.away_team == AwayTeam.id)) \
            .objects() \
            .get_or_none()
    
    games = [model_to_dict(game) for game in Game.select()]
    return games

def game_get(id) :
    HomeTeam = Team.alias()
    HomeTeamStatline = Statline.alias()
    AwayTeam = Team.alias()
    AwayTeamStatline = Statline.alias()
    
    game = Game.select(Game, HomeTeam, AwayTeam) \
            .join(HomeTeam, on=(Game.home_team == HomeTeam.id)) \
            .switch(Game) \
            .join(AwayTeam, on=(Game.away_team == AwayTeam.id)) \
            .where(Game.id == id) \
            .join(HomeTeamStatline, JOIN.LEFT_OUTER, on=(Game.home_team_statline == HomeTeamStatline.id)) \
            .switch(Game) \
            .join(AwayTeamStatline, JOIN.LEFT_OUTER, on=(Game.away_team_statline == AwayTeamStatline.id)) \
            .objects() \
            .get_or_none()
            
    if game is not None :
        game_dict = model_to_dict(game)
        return game_dict
    return None

def game_add(home_team, away_team, season) :
    game = Game(home_team=home_team, away_team=away_team, season=season)
    game.save()
    return game.id

def game_update(id, home_team, home_team_statline, away_team, away_team_statline, season) :
    game = Game(id=id, home_team=home_team, home_team_statline=home_team_statline, away_team=away_team, away_team_statline=away_team_statline, season=season)
    game.save()

def game_delete(id) :
    Game.get(id=id).delete_instance()
    
if __name__ == '__main__' :
    db_set_up()