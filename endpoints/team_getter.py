import requests
from utils.ref_getter import get_refs


def get_teams(season: int) -> list[dict]:
    team_refs = get_refs(
        'https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/' + str(season) + '/teams?limit=64')

    teams = []
    for ref in team_refs:
        request = requests.get(ref)
        data = request.json()
        team = {
            'RefUrl': data['$ref'],
            'Id': int(data['id']),
            'GuId': data['guid'],
            'Uid': data['uid'],
            'Slug': data['slug'],
            'Location': data['location'],
            'Name': data['name'],
            'Nickname': data['nickname'],
            'Abbreviation': data['abbreviation'],
            'DisplayName': data['displayName'],
            'ShortDisplayName': data['shortDisplayName'],
            'Color': data['color'],
            'AlternateColor': data['alternateColor'],
            'LogoUrl': data['logos'][0]['href'],
        }
        teams.append(team)

    return teams


get_teams(2024)
