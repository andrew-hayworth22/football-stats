<html>
    <head>
        <title>Football Stats</title>
    </head>

    <body style="width: 500px;">
        <a href="/season/{{ game['season']['id'] }}">Back</a>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h1>Edit Game</h1>
            <form action="/game/{{ game['id'] }}/delete" method="POST">
                <button type="submit">Delete</button>
            </form>
        </div>
        

        % if message :
        <div>{{ message }}</div>
        % end

        <form action="/game/{{ game['id'] }}" method="POST">
            <div style="margin-bottom: 12px">
                <label for="home_team" style="display: block;">Home Team</label>
                <select id="home_team" name="home_team" required>
                    <option value="">Select team...</option>
                    % for team in teams :
                        <option value={{ team['id'] }} {{ 'selected' if team['id'] == game['home_team']['id'] else '' }}>{{ team['location'] + ' ' + team['mascot'] }}</option>
                    % end
                </select>
            </div>
            
            <div style="margin-bottom: 12px;">
                % if game['home_team_statline'] is not None :
                    <div style="border: solid 1px;">
                        <h3 style="text-align: center">Statistics</h3>
                        <hr>
                        <div>
                            <div>Score: {{ game['home_team_statline']['score'] }}</div>
                            <div>Passing Yards: {{ game['home_team_statline']['passing_yards'] }}</div>
                            <div>Passing Attempts: {{ game['home_team_statline']['passing_attempts'] }}</div>
                            <div>Passing Completions: {{ game['home_team_statline']['passing_completions'] }}</div>
                            <div>Passing Touchdowns: {{ game['home_team_statline']['passing_touchdowns'] }}</div>
                            <div>Rushing Yards: {{ game['home_team_statline']['rushing_yards'] }}</div>
                            <div>Rushing Attempts: {{ game['home_team_statline']['rushing_attempts'] }}</div>
                            <div>Rushing Touchdowns: {{ game['home_team_statline']['rushing_touchdowns'] }}</div>
                            <div>Sacks: {{ game['home_team_statline']['sacks'] }}</div>
                            <div>Interceptions: {{ game['home_team_statline']['interceptions'] }}</div>
                            <div>Fumbles Recovered: {{ game['home_team_statline']['fumbles_recovered'] }}</div>
                        </div>
                    </div>
                % else :
                    <div>
                        <a href="/game/{{ game['id'] }}/add_stats/home">Add Stats</a>
                    </div>
                % end
            </div>

            <div style="margin-bottom: 12px">
                <label for="away_team" style="display: block;">Away Team</label>
                <select id="away_team" name="away_team" required>
                    <option value="">Select team...</option>
                    % for team in teams :
                        <option value={{ team['id'] }} {{ 'selected' if team['id'] == game['away_team']['id'] else '' }}>{{ team['location'] + ' ' + team['mascot'] }}</option>
                    % end
                </select>
            </div>

            <div style="margin-bottom: 12px;">
                % print(game)
                % if game['away_team_statline'] is not None :
                    <div>
                        <div style="border: solid 1px;">
                            <h3 style="text-align: center">Statistics</h3>
                            <hr>
                            <div>
                                <div>Score: {{ game['away_team_statline']['score'] }}</div>
                                <div>Passing Yards: {{ game['away_team_statline']['passing_yards'] }}</div>
                                <div>Passing Attempts: {{ game['away_team_statline']['passing_attempts'] }}</div>
                                <div>Passing Completions: {{ game['away_team_statline']['passing_completions'] }}</div>
                                <div>Passing Touchdowns: {{ game['away_team_statline']['passing_touchdowns'] }}</div>
                                <div>Rushing Yards: {{ game['away_team_statline']['rushing_yards'] }}</div>
                                <div>Rushing Attempts: {{ game['away_team_statline']['rushing_attempts'] }}</div>
                                <div>Rushing Touchdowns: {{ game['away_team_statline']['rushing_touchdowns'] }}</div>
                                <div>Sacks: {{ game['away_team_statline']['sacks'] }}</div>
                                <div>Interceptions: {{ game['away_team_statline']['interceptions'] }}</div>
                                <div>Fumbles Recovered: {{ game['away_team_statline']['fumbles_recovered'] }}</div>
                            </div>
                        </div>
                    </div>
                % else :
                    <div>
                        <a href="/game/{{ game['id'] }}/add_stats/away">Add Stats</a>
                    </div>
            </div>

            <div>
                <button type="submit">Submit</button>
            </div>
        </form>
    </body>
</html>