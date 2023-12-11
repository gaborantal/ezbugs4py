def match_results(results):
    ret = dict()

    def update(team, scored):
        if team in ret:
            ret[team] += scored
        else:
            ret[team] = scored

    for match in results:
        home, away, score = match.split(';')
        h_goal, a_goal = [int(i) for i in score.split('-')]

        update(home, h_goal)
        update(away, a_goal)

    return ret
