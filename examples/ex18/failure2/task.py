def match_results(lst):
    words = []
    goals = []
    ret = dict()
    for item in lst:
        words = item.split(';')
        home_team = words[0]
        away_team = words[1]
        goals = words[2].split('-')
        home_goals = goals[0]
        away_goals = goals[1]
        ret[home_team] += ret.get(home_team, 0) + int(home_goals)
        ret[away_team] += ret.get(away_team, 0) + int(away_goals)
    return ret
