<html>
    <head>
        <title>Football Stats</title>
    </head>
    <body>
        <a href="/home">Back</a>
        <h1> Add Season </h1>

        % if message :
        <div style="color: red">{{ message }}</div>
        % end

        <form action="/season" method="POST">
            <div style="margin-bottom: 12px">
                <label for="year" style="display: block;">Year</label>
                <input type="number" min="1900" max="2100" id="year" name="year" required/>
            </div>
            <input type="submit" value="Create">
        </form>
    </body>
</html>