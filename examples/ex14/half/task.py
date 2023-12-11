class Clustering(dict):
    def __init__(self, algorithm):
        if not isinstance(algorithm, str):
            raise TypeError
        self._algorithm = algorithm

    @property
    def algorithm(self):
        return "\"" + self._algorithm + "\"" + " algorithm"

    def put_into(self, element, cluster):
        if not isinstance(element, str) and not isinstance(element, int):
            raise TypeError
        if not isinstance(cluster, str):
            raise TypeError
        if not element in self:
            self[element] = cluster
            return True
        else:
            self[element] = cluster
            return False

    @property
    def cluster_count(self):
        result = []
        for key in self:
            if key not in result:
                result.append(key)
        return len(result)

    def count_of(self, input):
        if not isinstance(input, str):
            raise TypeError
        result = 0
        for key in self:
            if self[key] == input:
                result = result + 1
        return result

    def __str__(self):
        return str(len(self)) + " items in " + str(
            self.cluster_count) + " clusters are detected with " +\
               self.algorithm
