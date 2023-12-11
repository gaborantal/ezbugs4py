class LightString(object):
    def __init__(self, length=0, _lights=None):
        self.length = length
        self.lights = _lights or list()

    @property
    def lights(self):
        return list(self._lights)

    @lights.setter
    def lights(self, lights: list):
        if not isinstance(lights, list):
            raise TypeError("The lights can only be a list!")
        self._lights = list(lights)

    def add_light(self, text: str):
        if text in ["cold_white", "warm_white", "red", "green", "blue", "yellow"]:
            self._lights.append(text)

    def __lt__(self, other):
        if not isinstance(other, LightString):
            return False
        return self.length < other.length

    def __str__(self):
        different_colors = ""
        color_set = set(self.lights)
        color_set = sorted(color_set)
        for i in range(len(color_set)):
            different_colors += color_set[i] + ", "
        different_colors = different_colors[:-2]
        return f"{self.length} centimeter long light string, {len(self.lights)} pieces ({different_colors}) colored lights."

    def __eq__(self, other):
        if not isinstance(other, LightString):
            return False
        return self.length == other.length and self.lights == other.lights
