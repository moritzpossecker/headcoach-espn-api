import threading
import requests
from utils.ref_getter import get_refs
from utils.current_season_getter import get_current_season


def get_position_athletes(position_id: int) -> list[dict]:
    team_refs = get_refs(
        'https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/' + str(
            get_current_season()) + '/teams?limit=64')

    athletes = []
    threads = []
    for ref in team_refs:
        thread = threading.Thread(target=get_team_athletes_thread, args=(ref, position_id, athletes))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return athletes


def get_team_athletes_thread(ref: str, position_id: int, athletes: list[dict]) -> None:
    team_data = requests.get(ref).json()
    athletes_url = team_data['athletes']['$ref'] + '&limit=1000'
    athlete_urls = get_refs(athletes_url)
    threads = []
    for athlete_url in athlete_urls:
        thread = threading.Thread(target=get_athletes_thread,
                                  args=(athlete_url, position_id, int(team_data['id']), athletes))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def get_athletes_thread(ref: str, position_id: int, team_id: int, athletes: list[dict]) -> None:
    data = requests.get(ref).json()
    if int(data['position']['id']) != position_id:
        return
    athlete = {
        'RefUrl': data['$ref'],
        'Id': int(data['id']),
        'Uid': data['uid'],
        'GuId': data['guid'],
        'FirstName': data['firstName'],
        'LastName': data['lastName'],
        'FullName': data['fullName'],
        'Weight': data['displayWeight'],
        'Height': data['displayHeight'],
        'PositionId': int(data['position']['id']),
        'PositionName': data['position']['displayName'],
        'PositionAbbreviation': data['position']['abbreviation'],
        'TeamId': team_id
    }
    try:
        athlete['Age'] = int(data['age'])
    except KeyError:
        athlete['Age'] = None
    try:
        athlete['HeadshotUrl'] = data['headshot']['href']
    except KeyError:
        athlete['HeadshotUrl'] = None

    try:
        athlete['Jersey'] = int(data['jersey'])
    except KeyError:
        athlete['Jersey'] = None

    if athlete['Jersey'] is not None:
        athletes.append(athlete)
