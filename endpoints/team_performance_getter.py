import requests
from utils.game_id_getter import get_game_id
from utils.performance_getter import get_passing_performance, get_rushing_performance, get_defense_performance, get_defense_interceptions


def get_team_performance(team_id: int, week: int):
    game_id, recap_available = get_game_id(week, team_id)

    if game_id is None:
        raise Exception("Team isn't playing this week.")
    if not recap_available:
        raise Exception("No recap available yet.")

    return get_performance(game_id, team_id, week)


def get_performance(game_id: int, team_id: int, week: int):
    statistics_url = 'http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/' + str(game_id) + '/competitions/' + str(game_id) + '/competitors/' + str(team_id) + '/statistics?lang=en&region=us'
    data = requests.get(statistics_url).json()
    categories = data['splits']['categories']
    performance = {
        'GameId': game_id,
        'TeamId': team_id,
        'Week': week,
    }
    for category in categories:
        if category['name'] == 'passing':
            get_passing_performance(category, performance)
        elif category['name'] == 'rushing':
            get_rushing_performance(category, performance)
        elif category['name'] == 'defensive':
            get_defense_performance(category, performance)
        elif category['name'] == 'defensiveInterceptions':
            get_defense_interceptions(category, performance)

    return performance
