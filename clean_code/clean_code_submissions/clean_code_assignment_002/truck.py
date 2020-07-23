from car import Car


class Truck(Car):

    _horn = 'Honk Honk'

    def __init__(self, max_speed, acceleration, tyre_friction,
                 max_cargo_weight, color=None):
        super().__init__(max_speed, acceleration, tyre_friction, color)
        self._max_cargo_weight = max_cargo_weight
        self._cargo_weight = 0
        super().check_negative_zero_and_string_type(max_cargo_weight,
                                                    'max_cargo_weight')

    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight

    @property
    def cargo_weight(self):
        return self._cargo_weight

    def load(self, load_cargo_weight):
        super().check_negative_zero_and_string_type(load_cargo_weight,
                                                    'cargo_weight')
        if self._current_speed != 0:
            print('Cannot load cargo during motion')
        else:
            cargo_weight_with_load = self._cargo_weight + load_cargo_weight
            if cargo_weight_with_load <= self._max_cargo_weight:
                self._cargo_weight += load_cargo_weight
            else:
                comment_to_be_raised = self.cannot_load_cargo_weight()
                print(comment_to_be_raised)

    def cannot_load_cargo_weight(self):
        max_cargo_weight = self._max_cargo_weight
        return 'Cannot load cargo more than max limit: {}'.format(
            max_cargo_weight)

    def unload(self, unload_cargo_weight):
        super().check_negative_zero_and_string_type(unload_cargo_weight,
                                                    'cargo_weight')
        if self._current_speed != 0:
            print('Cannot unload cargo during motion')
        else:
            if self._cargo_weight >= unload_cargo_weight:
                self._cargo_weight -= unload_cargo_weight
            else:
                print("Can't unload cargo less than given unload cargo weight")
