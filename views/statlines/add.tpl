<html>
    <head>
        <title>Football Stats</title>
    </head>

    <body style="width: 500px;">
        <a href="/game/{{ game_id }}">Back</a>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h1>Add {{ 'Home' if is_home else 'Away' }} Stats</h1>
        </div>

        % if message :
        <div>{{ message }}</div>
        % end

        <form action="/statline" method="POST">
            <input type="hidden" name="game_id" value="{{ game_id }}">
            <input type="hidden" name="is_home" value="{{ is_home }}">

            <div style="margin-bottom: 12px">
                <label for="score" style="display: block;">Score</label>
                <input type="number" id="score" name="score" min="0" required>
            </div>

            <div style="margin-bottom: 12px">
                <label for="passing_yards" style="display: block;">Passing Yards</label>
                <input type="number" id="passing_yards" name="passing_yards" min="0" required>
            </div>

            <div style="margin-bottom: 12px">
                <label for="passing_attempts" style="display: block;">Passing Attempts</label>
                <input type="number" id="passing_attempts" name="passing_attempts" min="0" required>
            </div>

            <div style="margin-bottom: 12px">
                <label for="passing_completions" style="display: block;">Passing Completions</label>
                <input type="number" id="passing_completions" name="passing_completions" min="0" required>
            </div>

            <div style="margin-bottom: 12px">
                <label for="passing_touchdowns" style="display: block;">Passsing Touchdowns</label>
                <input type="number" id="passing_touchdowns" name="passing_touchdowns" min="0" required>
            </div>

            <div style="margin-bottom: 12px">
                <label for="rushing_yards" style="display: block;">Rushing Yards</label>
                <input type="number" id="rushing_yards" name="rushing_yards" min="0" required>
            </div>

            <div style="margin-bottom: 12px">
                <label for="rushing_attempts" style="display: block;">Rushing Attempts</label>
                <input type="number" id="rushing_attempts" name="rushing_attempts" min="0" required>
            </div>

            <div style="margin-bottom: 12px">
                <label for="rushing_touchdowns" style="display: block;">Rushing Touchdowns</label>
                <input type="number" id="rushing_touchdowns" name="rushing_touchdowns" min="0" required>
            </div>

            <div style="margin-bottom: 12px">
                <label for="sacks" style="display: block;">Sacks</label>
                <input type="number" id="sacks" name="sacks" min="0" required>
            </div>

            <div style="margin-bottom: 12px">
                <label for="interceptions" style="display: block;">Interceptions</label>
                <input type="number" id="interceptions" name="interceptions" min="0" required>
            </div>

            <div style="margin-bottom: 12px">
                <label for="fumbles_recovered" style="display: block;">Fumbles Recovered</label>
                <input type="number" id="fumbles_recovered" name="fumbles_recovered" min="0" required>
            </div>

            <input type="submit" value="Save">
        </form>
    </body>
</html>