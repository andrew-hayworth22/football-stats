from peewee import *
from db import *

db = SqliteDatabase('football-stats.db')
db.connect()

# Database Tests
def test_set_up() :
    print("Testing team set up")
    db_set_up()

    teams = team_get_all()
    assert len(teams) == 4

def test_get_all() :
    print("Testing get all teams...")

    db_set_up()

    teams = team_get_all()

    assert type(teams) is list
    assert len(teams) > 0

    for team in teams :
        assert type(team) is dict

        assert 'id' in team
        assert type(team['id']) is int

        assert 'location' in team
        assert type(team['location']) is str

        assert 'mascot' in team
        assert type(team['mascot']) is str

def test_get() :
    print('Testing get team...')

    db_set_up()

    teams = team_get_all()

    for team in teams :
        fetched_team = team_get(team['id'])
        assert type(fetched_team) is dict
        assert fetched_team['id'] == team['id']
        assert fetched_team['location'] == team['location']

def test_add() :
    print("Testing add team...")

    db_set_up()

    original_length = len(team_get_all())

    team_add('Seattle', 'Seahawks')

    teams = team_get_all()
    locations = [ team['location'] for team in teams ]

    assert len(teams) == original_length + 1
    assert 'Seattle' in locations

def test_update() :
    print("Testing team update...")

    db_set_up()

    original_teams = team_get_all()
    
    for team in original_teams :
        team_update(team['id'], team['location'] + ' UPDATED', team['mascot'] + ' UPDATED')

    new_teams = team_get_all()

    assert len(new_teams) == len(original_teams)

    locations = [ team['location'] for team in new_teams ]
    for location in ['Philadelphia UPDATED', 'Washington UPDATED', 'Dallas UPDATED', 'New York UPDATED'] :
        assert location in locations
    
def test_delete() :
    print('Testing delete team...')

    db_set_up()

    original_teams = team_get_all()
    
    team_to_delete = original_teams[0]

    team_delete(team_to_delete['id'])

    new_teams = team_get_all()
    locations = [ team['location'] for team in new_teams ]

    assert len(new_teams) == len(original_teams) - 1
    assert team_to_delete['location'] not in locations

test_set_up()
test_get_all()
test_get()
test_add()
test_update()
test_delete()
print("Done.")