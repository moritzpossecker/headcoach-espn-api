from datetime import datetime
import requests
from utils.current_season_getter import get_current_season


def get_current_week() -> dict:
    url = 'https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?limit=1&dates='
    current_season = get_current_season()
    url = url + str(current_season)
    request = requests.get(url)
    data = request.json()
    calendar = data['leagues'][0]['calendar'][1]
    entries = calendar['entries']
    for entry in entries:
        start_date = datetime.strptime(entry['startDate'], '%Y-%m-%dT%H:%MZ')
        end_date = datetime.strptime(entry['endDate'], '%Y-%m-%dT%H:%MZ')
        now = datetime.now()
        if start_date <= now <= end_date:
            return {
                'Id': int(str(entry['value']) + str(current_season)),
                'Number': int(entry['value']),
                'Season': current_season,
                'StartDate': start_date,
                'EndDate': end_date,
            }

    return {
        'Id': -1,
        'Number': None,
        'Season': None,
        'StartDate': None,
        'EndDate': None,
    }
