import requests
from utils.performance_getter import *
from utils.game_id_getter import get_game_id


def get_athlete_performance(athlete_id: int, team_id: int, week: int):
    game_id, recap_available = get_game_id(week, team_id)

    if game_id is None:
        raise Exception("Team isn't playing this week.")
    if not recap_available:
        raise Exception("No recap available yet.")

    return get_performance(game_id, athlete_id, team_id, week)


def get_performance(game_id, athlete_id, team_id, week):
    statistics_url = 'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/' + str(game_id) + '/competitions/' + str(game_id) + '/competitors/' + str(team_id) + '/roster/' + str(athlete_id) + '/statistics/0?lang=en&region=us'
    data = requests.get(statistics_url).json()
    categories = data['splits']['categories']
    performance = {
        'GameId': game_id,
        'TeamId': team_id,
        'Week': week,
    }
    for category in categories:
        if category['name'] == 'general':
            get_general_performance(category, performance)
        elif category['name'] == 'passing':
            get_passing_performance(category, performance)
        elif category['name'] == 'receiving':
            get_receiving_performance(category, performance)
        elif category['name'] == 'rushing':
            get_rushing_performance(category, performance)
        elif category['name'] == 'defensive':
            get_defense_performance(category, performance)
        elif category['name'] == 'defensiveInterceptions':
            get_defense_interceptions(category, performance)
        elif category['name'] == 'kicking':
            get_kicking_performance(category, performance)

    return performance
