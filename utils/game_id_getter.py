from endpoints.game_getter import get_games


def get_game_id(week: int, team_id: int) -> (int | None, bool):
    week_games = get_games(week)
    for game in week_games:
        if game['HomeTeamId'] == team_id or game['AwayTeamId'] == team_id:
            return game['Id'], game['RecapAvailable']

    return None, False
