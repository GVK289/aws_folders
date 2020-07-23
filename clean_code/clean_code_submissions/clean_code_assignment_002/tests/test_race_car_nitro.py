import pytest


from race_car import RaceCar

@pytest.mark.parametrize(
    "value_of_color, value_of_max_speed, value_of_acceleration, value_of_tyre_friction, value_of_current_speed, value_of_nitro_value",
    [('Red', 200, 60, 10, 110, 10), ('Blue', 150, 55, 25, 85, 10),
     ('Black', 21, 5, 5, 5, 0), ('Green', 100, 20, 10, 30, 0)])
def test_nitro_of_race_car_when_race_car_apply_breaks_after_accelerating_half_more_than_max_speed_returns_current_speed(value_of_color, value_of_max_speed, value_of_acceleration, value_of_tyre_friction, value_of_current_speed, value_of_nitro_value):
    # Arrange
    race_car = RaceCar(color=value_of_color, max_speed=value_of_max_speed,
                       acceleration=value_of_acceleration,
                       tyre_friction=value_of_tyre_friction)
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.apply_brakes()

    # Act
    nitro = race_car.nitro

    # Assert
    assert nitro == value_of_nitro_value
    assert race_car.current_speed == value_of_current_speed

@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction, current_speed, nitro_value",
    [('Red', 200, 60, 10, 188, 0), ('Blue', 155, 55, 25, 155, 0)])
def test_nitro_and_current_speed_of_race_car_when_race_car_apply_breaks_after_accelerating_half_more_than_max_speed_and_then_accelerate_returns_current_speed(color, max_speed, acceleration, tyre_friction, current_speed, nitro_value):
    # Arrange
    race_car = RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.apply_brakes()
    race_car.accelerate()

    # Act
    nitro = race_car.nitro

    # Assert
    assert nitro == nitro_value
    assert race_car.current_speed == current_speed
