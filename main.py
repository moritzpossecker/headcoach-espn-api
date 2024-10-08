from flask import Flask, jsonify, request
from flask_cors import CORS
from endpoints.team_getter import get_teams
from utils.current_season_getter import get_current_season
from endpoints.current_week_getter import get_current_week
from endpoints.game_getter import get_games
from endpoints.athlete_getter import get_position_athletes
from endpoints.team_performance_getter import get_team_performance
from endpoints.athlete_performance_getter import get_athlete_performance

app = Flask(__name__)
CORS(app)


@app.route('/all-nfl-teams', methods=['GET'])
def request_all_nfl_teams():
    return jsonify(get_teams(get_current_season())), 200


@app.route('/current-week', methods=['GET'])
def request_current_week():
    return jsonify(get_current_week()), 200


@app.route('/games', methods=['GET'])
def request_games():
    week = request.args.get('week')
    return jsonify(get_games(int(week))), 200


@app.route('/athletes', methods=['GET'])
def request_athletes():
    position_id = request.args.get('positionId')
    return jsonify(get_position_athletes(int(position_id))), 200


@app.route('/team-performance', methods=['GET'])
def request_team_performance():
    week = request.args.get('week')
    team_id = request.args.get('teamId')
    return jsonify(get_team_performance(int(team_id), int(week))), 200


@app.route('/athlete-performance', methods=['GET'])
def request_athlete_performance():
    week = request.args.get('week')
    team_id = request.args.get('teamId')
    athlete_id = request.args.get('athleteId')
    return jsonify(get_athlete_performance(int(athlete_id), int(team_id), int(week))), 200


if __name__ == '__main__':
    app.run(debug=True)
