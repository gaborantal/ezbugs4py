def groupby(be : dict):
    ki = {}
    for key, value in be.items():
        ki[value] = ki.get(value, []) + [key]
    return ki
