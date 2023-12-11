def groupby(clustering):
    groups = dict()
    if not isinstance(clustering, dict):
        raise TypeError()
    for item, cluster in clustering:
        if not isinstance(item, int) and not isinstance(item,
                                                        str) and not \
                isinstance(item, float) and not isinstance(item, bool):
            raise TypeError()
        if not isinstance(cluster, int) and not isinstance(cluster,
                                                           str) and not \
                isinstance(cluster, float) and not isinstance(cluster, bool):
            raise TypeError()
        groups[cluster] = groups.get(cluster, []) + [item]
    return groups
