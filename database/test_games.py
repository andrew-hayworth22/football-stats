from peewee import *
from db import *

db = SqliteDatabase('football-stats.db')
db.connect()

# Database Tests
def test_get_all() :
    print("Testing get all games...")
    db_set_up()

    games = game_get_all()

    assert type(games) is list
    assert len(games) > 0

    for game in games :
        assert type(game) is dict

        assert 'id' in game
        assert type(game['id']) is int

        assert 'home_team' in game
        assert type(game['home_team']) is dict

        assert 'away_team' in game
        assert type(game['away_team']) is dict

def test_get() :
    print('Testing get game...')
    db_set_up()

    games = game_get_all()

    for game in games :
        fetched_game = game_get(game['id'])
        assert type(fetched_game) is dict
        assert fetched_game['id'] == game['id']
        assert fetched_game['home_team'] == game['home_team']

def test_add() :
    print("Testing add game...")
    db_set_up()

    original_length = len(game_get_all())
    teams = team_get_all()
    seasons = season_get_all()

    game_add(teams[2]['id'], teams[3]['id'], seasons[0]['id'])

    games = game_get_all()
    home_teams = [ game['home_team'] for game in games ]
    seasons = [ game['season'] for game in games ]

    assert len(games) == original_length + 1
    assert teams[2] in home_teams
    assert seasons[0] in seasons

def test_update() :
    print("Testing game update...")
    db_set_up()

    original_games = game_get_all()
    original_game = original_games[0]

    game_update(original_game['id'], 3, 1, 4, 2, 2)

    new_games = game_get_all()
    new_game = game_get(original_game['id'])

    assert len(new_games) == len(original_games)
    assert original_game != new_game
    assert new_game['home_team'] == team_get(3)
    assert new_game['season']['id'] == 2
    
    
def test_delete() :
    print('Testing delete game...')
    db_set_up()

    original_games = game_get_all()
    
    game_to_delete = original_games[0]

    game_delete(game_to_delete['id'])

    new_games = game_get_all()

    assert len(new_games) == len(original_games) - 1

test_get_all()
test_get()
test_add()
test_update()
test_delete()
print("Done.")