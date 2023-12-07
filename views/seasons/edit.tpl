<html>
    <head>
        <title>Football Stats</title>
    </head>
    <body>
        <a href="/home">Back</a>
        <h1> {{ season['year'] }} </h1>
        <form action="/season/{{ season['id'] }}" method="POST">
            <div style="margin-bottom: 12px">
                <label for="year" style="display: block;">Year</label>
                <input type="number" min="1900" max="2100" id="year" name="year" value="{{ season['year'] }}" required/>
            </div>
            <input type="submit" value="Save">

            <hr>

            <div>
                <h2>Games</h2>
                
                <ul>
                    % for game in season['games']:
                        <li>
                            <a href="/game/{{ game['id'] }}">{{ game['away_team']['mascot'] }} @ {{ game['home_team']['mascot'] }}</a>
                        </li>
                    % end
                </ul>
                
                <a href="/season/{{ season['id'] }}/game">Create Game</a>
            </div>
        </form>
    </body>
</html>