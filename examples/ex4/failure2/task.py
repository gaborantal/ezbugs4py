class LightString(object):
    def __init__(self, length=0, lights=list()):
        self.length = length
        self._lights = list()

    @property
    def lights(self):
        return self._lights

    @lights.setter
    def lights(self, lights):
        if isinstance(lights, list()):
            self._lights = lights
        else:
            raise TypeError("The lights can only be a list!")

    def add_light(self, color):
        if color == "cold_white" or color == "warm_white" or color == "red" or color == "green" or color == "blue" or color == "yellow":
            self._lights.append(color)
        else:
            pass

    def __lt__(self, other):
        return len(self.__dict__) < len(other.__dict__)

    def __str__(self):
        different_colors = self._lights.sort()
        return f"{self.length} cm long light string, {len(self._lights)} pieces ({different_colors}) colored lights."

    def __eq__(self, other):
        return isinstance(other, str) and self.__dict__ == other.__dict__
