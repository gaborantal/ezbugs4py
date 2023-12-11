class Clustering(dict):
    def __init__(self, _algorithm):
        self._algorithm = _algorithm

    @property
    def algorithm(self):
        return f'"{self._algorithm}" algorithm'

    def put_into(self, element, cluster_name):
        if element not in self:
            self[element] = cluster_name
            return True
        else:
            self[element] = cluster_name
            return False

    @property
    def cluster_count(self):
        ret = {}
        for x in self:
            ret[self[x]] = 1
        return len(ret)

    def getClusterMap(self):
        ret = {}
        for x in self:
            if self[x] not in ret:
                ret[self[x]] = [x]
            else:
                ret[self[x]].append(x)

        return ret

    def count_of(self, s):
        if s not in self.getClusterMap():
            return 0
        return len(self.getClusterMap()[s])

    def __str__(self):
        return f"{str(len(self))} items in {len(self.getClusterMap())}" \
               f" detected with {self._algorithm}"
