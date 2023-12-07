<html>
    <head>
        <title>Football Stats</title>
    </head>

    <body>
        <a href="/teams">Back</a>
        <h1>{{ team['location'] + ' ' + team['mascot'] }}</h1>

        % if message :
        <div>{{ message }}</div>
        % end

        <form action="/team/{{ team['id'] }}" method="POST">
            <div style="margin-bottom: 12px">
                <label for="location" style="display: block;">Location</label>
                <input id="location" name="location" required value="{{ team['location'] }}"/>
            </div>
            <div style="margin-bottom: 12px">
                <label for="mascot" style="display: block;">Mascot</label>
                <input id="mascot" name="mascot" required value="{{ team['mascot'] }}"/>
            </div>
            <div>
                <input type="submit" value="Save">
            </div>
        </form>

        <form action="/team/{{ team['id'] }}/delete" method="POST">
            <button type="submit" onclick="return confirm('Are you sure you want to delete this team? All games involving this team will be deleted as well!')">Delete</button>
        </form>
    </body>
</html>