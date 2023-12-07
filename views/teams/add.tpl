<html>
    <head>
        <title>Football Stats</title>
    </head>

    <body>
        <a href="/teams">Back</a>
        <h1>Add Team</h1>

        % if message :
        <div>{{ message }}</div>
        % end

        <form action="/team" method="POST">
            <div style="margin-bottom: 12px">
                <label for="location" style="display: block;">Location</label>
                <input id="location" name="location" required/>
            </div>
            <div style="margin-bottom: 12px">
                <label for="mascot" style="display: block;">Mascot</label>
                <input id="mascot" name="mascot" required/>
            </div>
            <div>
                <input type="submit" value="Create">
            </div>
        </form>
    </body>
</html>