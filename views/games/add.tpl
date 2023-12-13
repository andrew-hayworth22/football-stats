<html>
    <head>
        <title>Football Stats</title>
    </head>

    <body>
        <a href="/season/{{season_id}}">Back</a>
        <h1>Add Game</h1>

        % if message :
        <div>{{ message }}</div>
        % end

        <form action="/game" method="POST">
            <input type="hidden" name="season" value="{{ season_id }}">
            <div style="margin-bottom: 12px">
                <label for="home_team" style="display: block;">Home Team</label>
                <select id="home_team" name="home_team" required>
                    <option value="">Select team...</option>
                    % for team in teams :
                        <option value={{ team['id'] }}>{{ team['location'] + ' ' + team['mascot'] }}</option>
                    % end
                </select>
            </div>
            <div style="margin-bottom: 12px">
                <label for="away_team" style="display: block;">Away Team</label>
                <select id="away_team" name="away_team" required>
                    <option value="">Select team...</option>
                    % for team in teams :
                        <option value={{ team['id'] }}>{{ team['location'] + ' ' + team['mascot'] }}</option>
                    % end
                </select>
            </div>
            <div>
                <button type="submit">Submit</button>
            </div>
        </form>
    </body>
</html>