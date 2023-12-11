class PrettyPrint(object):
    def __init__(self, prefix=""):
        self._prefix = prefix

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, value):
        self._prefix = value

    def get(self, data):
        if data is None:
            return self.get_NoneType(data)
        elif isinstance(data, int):
            return self.get_int(data)
        elif isinstance(data, float):
            return self.get_float(data)
        elif isinstance(data, str):
            return self.get_str(data)
        elif isinstance(data, list):
            return self.get_list(data)
        elif isinstance(data, dict):
            return self.get_dict(data)
        else:
            return f"{self.prefix} (unknown) err"

    def get_NoneType(self, data):
        return f"{self.prefix} {None}"

    def get_int(self, data):
        return f"{self.prefix} (integer) {data}"

    def get_float(self, data):
        return f"{self.prefix} (float) {data}"

    def get_str(self, data):
        return f"{self.prefix} (str) {data}"

    def get_list(self, data):
        return f"{self.prefix} (list) {data}"

    def get_dict(self, data):
        return f"{self.prefix} (dict) {data}"
