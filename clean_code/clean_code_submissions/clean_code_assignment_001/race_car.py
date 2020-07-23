import math
from car import Car


class RaceCar(Car):

    _horn = 'Peep Peep\nBeep Beep'

    def __init__(self, max_speed, acceleration, tyre_friction, color=None):
        super().__init__(max_speed, acceleration, tyre_friction, color)
        self._nitro = 0

    @property
    def nitro(self):
        return self._nitro

    def accelerate(self):
        super().accelerate()
        if self._nitro:
            self._current_speed += math.ceil(self._acceleration * 0.3)
            if self._current_speed >= self._max_speed:
                self._current_speed = self._max_speed
            self._nitro -= 10

    def apply_brakes(self):
        if self._current_speed > (self._max_speed//2):
            self._nitro += 10
        super().apply_brakes()
