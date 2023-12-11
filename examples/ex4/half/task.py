class LightString(object):
    def __init__(self, length=0, _lights=[""]):
        self.lenght = length
        self._lights = []

    @property
    def lights(self, _lights):
        copy = self._lights
        return copy

    @property
    def lights(self, _lights):
        copy = _lights
        if isinstance(_lights, list):
            raise TypeError("The lights can only be a list!")
        self._lights = copy

    def add_light(self, str):
        if str == "cold_white" or "warm_white" or "red" or "blue" or "blue" or "yellow":
            self._lights.append(str)

    def __lt__(self, other):
        if self.lenght < other.length:
            return True
        else:
            return False

    def __str__(self):
        return self.lenght + " centimeter long light string, " + len(self._lights) + " pieces (" + print(self._lights.sort()) + ") colored lights."
