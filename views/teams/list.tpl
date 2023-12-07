<html>
    <head>
        <title>Football Stats</title>
    </head>

    <body>
        <a href="/home">Back</a>
        <h1>Teams</h1>

        <div style="display: flex; gap: 4px;">
            <form action="/teams" method="GET">
                <input type="text" name="search" placeholder="Search for a team" value="{{ search }}">
                <input type="submit" value="Search">
            </form>
            <form action="/teams" method="GET">
                <input type="submit" value="Clear">
            </form>
        </div>

        <ul>
            % for team in teams :
                <li><a href="/team/{{ team['id'] }}">{{ team['location'] + ' ' + team['mascot'] }}</li>
            % end
        </ul>
        <a href="/team">Create Team</a>
    </body>
</html>