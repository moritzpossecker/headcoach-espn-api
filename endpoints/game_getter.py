from datetime import datetime

import requests
from utils.current_season_getter import get_current_season
from utils.ref_getter import get_refs


def get_games(week: int) -> list[dict]:
    url = 'https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/'
    url = url + str(get_current_season()) + '/types/2/weeks/'
    url = url + str(week) + '/events?lang=en&region=us'
    game_refs = get_refs(url)
    games = []
    for game_ref in game_refs:
        request = requests.get(game_ref)
        data = request.json()
        game = {
            'RefUrl': data['$ref'],
            'Id': int(data['id']),
            'WeekId': int(str(get_current_season()) + str(week)),
            'Uid': data['uid'],
            'Date': datetime.strptime(data['date'], '%Y-%m-%dT%H:%MZ'),
            'Name': data['name'],
            'ShortName': data['shortName'],
            'RecapAvailable': data['competitions'][0]['recapAvailable'],
            'HomeTeamId': int(data['competitions'][0]['competitors'][0]['id']),
            'AwayTeamId': int(data['competitions'][0]['competitors'][1]['id']),
        }
        games.append(game)
    return games
