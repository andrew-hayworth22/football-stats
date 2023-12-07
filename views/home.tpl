<html>
    <head>
        <title>Football Stats</title>
    </head>

    <body style="width: 500px">
        <h1>Football Statistics</h1>

        <p>
            This is a simple web application that allows you to manage football statistics.
            Get started by <a href="/teams">adding your teams</a>.
            After that, you can add seasons and create games within those seasons.
        </p>

        <h2>Seasons</h2>

        <ul>
            % for season in seasons :
                <li><a href="/season/{{ season['id'] }}">{{ season['year'] }}</a></li>
            % end
        </ul>
        <a href="/season">Add Season</a>
    </body>
</html>