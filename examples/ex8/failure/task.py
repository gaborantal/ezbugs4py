class PrettyPrint:
    def __init__(self, prefix=""):
        self._prefix = prefix

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, value):
        _prefix = value

    def get(self, data):
        output = str(self._prefix) + " "
        types = ["NoneType", "int", "float", "str", "list", "dict"]

        _name = type(data).__name__
        if _name in types:
            _func = getattr(self, "get_" + _name)
            output += _func(data)
        else:
            output += self.get_unknown(data)

        return (output)

    def get_NoneType(self, data):
        return str(data)

    def get_int(self, data):
        return "(integer) " + str(data)

    def get_float(self, data):
        return "(float) " + str(data)

    def get_str(self, data):
        return "(string) " + str(data)

    def get_list(self, data):
        return "(list object) " + str(data)

    def get_dict(self, data):
        return "(dictionary) " + str(data)

    def get_unknown(self, data):
        return "(unknown) " + str(data)
