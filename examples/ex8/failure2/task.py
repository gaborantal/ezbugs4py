class PrettyPrint(object):
    def __init__(self, prefix=""):
        self.prefix = prefix

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, value):
        self.prefix = value

    def get(self, param):
        if type(param) is None:
            return str(self.get_prefix()) + self.get_NoneType(param) + str(param)
        elif type(param) == int:
            return str(self.get_prefix()) + self.get_int(param) + str(param)
        elif type(param) == float:
            return str(self.get_prefix()) + self.get_float(param) + str(param)
        elif type(param) == str:
            return str(self.get_prefix()) + self.get_str(param) + str(param)
        elif type(param) == list:
            return str(self.get_prefix()) + self.get_list(param) + str(param)
        elif type(param) == dict:
            return str(self.get_prefix()) + self.get_dict(param) + str(param)
        else:
            return "(unknown)"

    def get_NoneType(self, param):
        return ""

    def get_int(self, param):
        return " (integer) "

    def get_float(self, param):
        return " (float) "

    def get_str(self, param):
        return " (string) "

    def get_list(self, param):
        return " (list object) "

    def get_dict(self, param):
        return " (dictionary) "
