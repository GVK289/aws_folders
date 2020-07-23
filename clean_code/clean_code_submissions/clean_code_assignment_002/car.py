class Car:
    _horn = 'Beep Beep'

    def __init__(self, max_speed, acceleration, tyre_friction, color=None):
        self._color = color
        self._max_speed = max_speed
        self._acceleration = acceleration
        self._tyre_friction = tyre_friction
        self._is_engine_started = False
        self._current_speed = 0

        self.check_not_string_type(color, "color")
        self.check_negative_zero_and_string_type(max_speed, "max_speed")
        self.check_negative_zero_and_string_type(acceleration, "acceleration")
        self.check_negative_zero_and_string_type(tyre_friction,
                                                 "tyre_friction")

    @property
    def color(self):
        return self._color

    @property
    def max_speed(self):
        return self._max_speed

    @property
    def acceleration(self):
        return self._acceleration

    @property
    def tyre_friction(self):
        return self._tyre_friction

    @property
    def is_engine_started(self):
        return self._is_engine_started

    @property
    def current_speed(self):
        return self._current_speed

    @staticmethod
    def check_not_string_type(attribute, attribute_name):
        if not isinstance(attribute, str):
            raise ValueError('Invalid value for {}'.format(attribute_name))

    def check_negative_zero_and_string_type(self, value, attribute_name):
        if self.is_not_positive_and_not_int(value):
            raise ValueError('Invalid value for {}'.format(attribute_name))

    @staticmethod
    def is_not_positive_and_not_int(value):
        return isinstance(value, str) or value <= 0

    def start_engine(self):
        self._is_engine_started = True

    def stop_engine(self):
        self._is_engine_started = False

    def accelerate(self):
        if self._is_engine_started:
            self._current_speed += self._acceleration
            if self._current_speed >= self._max_speed:
                self._current_speed = self._max_speed
        else:
            print('Start the engine to accelerate')

    def apply_brakes(self):
        if self._current_speed >= self._tyre_friction:
            self._current_speed -= self._tyre_friction
        else:
            self._current_speed = 0

    def sound_horn(self):
        if self._is_engine_started:
            print(self._horn)
        else:
            print('Start the engine to sound_horn')
