[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](https://github.com/moritzpossecker/headcoach-espn-api/releases/tag/v1.0.0) 
# NFL API

This is a Flask-based API that provides various endpoints for retrieving NFL-related data.

## Endpoints

### 1. /all-nfl-teams

* https://headcoach-espn-api.onrender.com/all-nfl-teams
* Method: GET
* Returns: A JSON response containing a list of all NFL teams for the current season.

Example response:

```json
[
  {
    "Abbreviation": "ARI",
    "AlternateColor": "ffffff",
    "Color": "a40227",
    "DisplayName": "Arizona Cardinals",
    "GuId": "8fc7b962-95e1-3cb8-6a7d-b499de9ad546",
    "Id": 22,
    "Location": "Arizona",
    "LogoUrl": "https://a.espncdn.com/i/teamlogos/nfl/500/ari.png",
    "Name": "Cardinals",
    "Nickname": "Cardinals",
    "RefUrl": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/teams/22?lang=en&region=us",
    "ShortDisplayName": "Cardinals",
    "Slug": "arizona-cardinals",
    "Uid": "s:20~l:28~t:22"
  },
  ...
]
```

### 2. /current-week

* https://headcoach-espn-api.onrender.com/current-week
* Method: GET
* Returns: A JSON response containing the current week of the NFL season.

Example response:

```json
{
    "EndDate": "Wed, 09 Oct 2024 06:59:00 GMT",
    "Id": 52024,
    "Number": 5,
    "Season": 2024,
    "StartDate": "Wed, 02 Oct 2024 07:00:00 GMT"
}
```

### 3. /games

* https://headcoach-espn-api.onrender.com/games?week=5
* Method: GET
* Parameters:
    * `week`: The week number for which to retrieve games (required)
* Returns: A JSON response containing a list of games for the specified week.

Example response:

```json
[
  {
    "AwayTeamId": 17,
    "Date": "Fri, 20 Sep 2024 00:15:00 GMT",
    "HomeTeamId": 20,
    "Id": 401671808,
    "Name": "New England Patriots at New York Jets",
    "RecapAvailable": true,
    "RefUrl": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/401671808?lang=en&region=us",
    "ShortName": "NE @ NYJ",
    "Uid": "s:20~l:28~e:401671808",
    "WeekId": 42024
  },
  ...
]
```

### 4. /athletes

* https://headcoach-espn-api.onrender.com/athletes?positionId=8
* Method: GET
* Parameters:
    * `positionId`: The ID of the position for which to retrieve athletes (required)
* Returns: A JSON response containing a list of athletes for the specified position.

Example response:

```json
[
  {
    "Age": 28,
    "FirstName": "Josh",
    "FullName": "Josh Allen",
    "GuId": "853f8768-54bd-6a4f-cb10-63d6df1e7742",
    "HeadshotUrl": "https://a.espncdn.com/i/headshots/nfl/players/full/3918298.png",
    "Height": "6' 5\"",
    "Id": 3918298,
    "Jersey": 17,
    "LastName": "Allen",
    "PositionAbbreviation": "QB",
    "PositionId": 8,
    "PositionName": "Quarterback",
    "RefUrl": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/athletes/3918298?lang=en&region=us",
    "TeamId": 2,
    "Uid": "s:20~l:28~a:3918298",
    "Weight": "237 lbs"
  },
  ...
]
```

### 5. /team-performance

* https://headcoach-espn-api.onrender.com/athletes?week=3&teamId=20
* Method: GET
* Parameters:
    * `week`: The week number for which to retrieve team performance data (required)
    * `teamId`: The ID of the team for which to retrieve performance data (required)
* Returns: A JSON response containing team performance data for the specified week and team.

Example response:

```json
{
  "Defense": {
    "Interceptions": 0,
    "PointsAllowed": 3,
    "Sacks": 7,
    "Safeties": 0,
    "Touchdowns": 0,
    "YardsAllowed": 139
  },
  "GameId": 401671808,
  "Passing": {
    "Interceptions": 0,
    "PassingTouchdowns": 2,
    "PassingYards": 281,
    "TwoPtPass": 0
  },
  "Rushing": {
    "RushingFumbles": 0,
    "RushingTouchdowns": 1,
    "RushingYards": 133,
    "TwoPtRush": 0
  },
  "TeamId": 20,
  "Week": 3
}
```

### 6. /athlete-performance

* https://headcoach-espn-api.onrender.com/athletes?week=3&teamId=2&athleteId=3918298
* Method: GET
* Parameters:
    * `week`: The week number for which to retrieve athlete performance data (required)
    * `teamId`: The ID of the team for which to retrieve athlete performance data (required)
    * `athleteId`: The ID of the athlete for which to retrieve performance data (required)
* Returns: A JSON response containing athlete performance data for the specified week, team, and athlete.

Example response:

```json
{
  "Defense": {
    "Interceptions": 0,
    "PointsAllowed": 0,
    "Sacks": 0,
    "Safeties": 0,
    "Touchdowns": 0,
    "YardsAllowed": 0
  },
  "GameId": 401671682,
  "General": {
    "FumblesForced": 0,
    "FumblesLost": 0,
    "FumblesRecovered": 0
  },
  "Kicking": {
    "ExtraPoints": 0,
    "FieldGoals": 0,
    "FieldGoalsLong": 0,
    "FieldGoalsShort": 0
  },
  "Passing": {
    "Interceptions": 0,
    "PassingTouchdowns": 4,
    "PassingYards": 263
  },
  "Receiving": {
    "ReceivingTouchdowns": 0,
    "ReceivingYards": 0
  },
  "Rushing": {
    "RushingFumbles": 0,
    "RushingTouchdowns": 0,
    "RushingYards": 44
  },
  "TeamId": 2,
  "Week": 3
}
```

## Running the API

To run the API, execute the following command in your terminal:

```powershell
python main.py
```

The API will be available at `http://localhost:5000`. You can use a tool like `curl` or a web browser to test the
endpoints.