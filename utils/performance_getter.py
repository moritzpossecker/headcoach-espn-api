def get_passing_performance(category, performance):
    stats = category['stats']
    passing_performance = try_get_performance_item('Passing', performance)
    for stat in stats:
        if stat['name'] == 'interceptions':
            passing_performance['Interceptions'] = stat['value']
        elif stat['name'] == 'passingTouchdowns':
            passing_performance['PassingTouchdowns'] = stat['value']
        elif stat['name'] == 'passingYards':
            passing_performance['PassingYards'] = stat['value']
        elif stat['name'] == 'twoPointPassConvs':
            passing_performance['TwoPtPass'] = stat['value']


def get_rushing_performance(category, performance):
    stats = category['stats']
    rushing_performance = try_get_performance_item('Rushing', performance)
    for stat in stats:
        if stat['name'] == 'rushingFumbles':
            rushing_performance['RushingFumbles'] = stat['value']
        elif stat['name'] == 'rushingTouchdowns':
            rushing_performance['RushingTouchdowns'] = stat['value']
        elif stat['name'] == 'rushingYards':
            rushing_performance['RushingYards'] = stat['value']
        elif stat['name'] == 'twoPointRushConvs':
            rushing_performance['TwoPtRush'] = stat['value']


def get_defense_performance(category, performance):
    stats = category['stats']
    defense_performance = try_get_performance_item('Defense', performance)
    for stat in stats:
        if stat['name'] == 'sacks':
            defense_performance['Sacks'] = stat['value']
        elif stat['name'] == 'safeties':
            defense_performance['Safeties'] = stat['value']
        elif stat['name'] == 'yardsAllowed':
            defense_performance['YardsAllowed'] = stat['value']
        elif stat['name'] == 'pointsAllowed':
            defense_performance['PointsAllowed'] = stat['value']
        elif stat['name'] == 'defensiveTouchdowns':
            defense_performance['Touchdowns'] = stat['value']


def get_defense_interceptions(category, performance):
    stats = category['stats']
    for stat in stats:
        if stat['name'] == 'interceptions':
            performance['Defense']['Interceptions'] = stat['value']
            return


def get_general_performance(category, performance):
    stats = category['stats']
    general_performance = try_get_performance_item('General', performance)
    for stat in stats:
        if stat['name'] == 'fumblesLost':
            general_performance['FumblesLost'] = stat['value']
        elif stat['name'] == 'fumblesRecovered':
            general_performance['FumblesRecovered'] = stat['value']
        elif stat['name'] == 'fumblesForced':
            general_performance['FumblesForced'] = stat['value']


def get_receiving_performance(category, performance):
    stats = category['stats']
    receiving_performance = try_get_performance_item('Receiving', performance)
    for stat in stats:
        if stat['name'] == 'receivingTouchdowns':
            receiving_performance['ReceivingTouchdowns'] = stat['value']
        elif stat['name'] == 'receivingYards':
            receiving_performance['ReceivingYards'] = stat['value']


def get_kicking_performance(category, performance):
    stats = category['stats']
    kicking_performance = try_get_performance_item('Kicking', performance)
    for stat in stats:
        if stat['name'] == 'extraPointsMade':
            kicking_performance['ExtraPoints'] = stat['value']
        elif stat['name'] == 'fieldGoalsMade':
            kicking_performance['FieldGoals'] = stat['value']
        elif stat['name'] == 'fieldGoalsMade50':
            kicking_performance['FieldGoalsLong'] = stat['value']

    kicking_performance['FieldGoalsShort'] = kicking_performance['FieldGoals'] - kicking_performance['FieldGoalsLong']


def try_get_performance_item(name: str, performance):
    try:
        return performance[name]
    except KeyError:
        performance[name] = {}
        return performance[name]
