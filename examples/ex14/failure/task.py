class Clustering(dict):
    def __init__(self, name):
        super().__init__(**{})
        _algorithm = name

    @property
    def algorithm(self):
        return f'"{self._algorithm}" algorithm'

    def put_into(self, item, cluster):
        result = item not in self
        self[item] = cluster
        return result

    @property
    def cluster_count(self):
        return len(set(self.values()))

    def count_of(self, cluster):
        return len([item for item, current_cluster in self.items() if
                    current_cluster == cluster])

    def __str__(self):
        return f'{len(self)} items in {self.cluster_count} ' \
               f'clusters detected with {self.algorithm}'
