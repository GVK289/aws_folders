import pytest


from race_car import RaceCar

def test_apply_brakes_when_race_car_object_is_in_motion_returns_current_speed(race_car):
    # Arrange
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    current_speed = 70

    # Act
    race_car.apply_brakes()

    # Assert
    assert race_car.current_speed == current_speed

@pytest.mark.parametrize(
    """color_value, max_speed_value, acceleration_value, tyre_friction_value,
    current_speed_value""", [
        ('Red', 200, 50, 20, 30), ('Blue', 150, 25, 25, 0)])
def test_apply_breaks_when_race_car_object_current_speed_is_more_than_or_equal_to_race_car_object_tyre_friction_returns_current_speed(color_value, max_speed_value, acceleration_value, tyre_friction_value, current_speed_value):
    # Arrange
    race_car = RaceCar(color=color_value, max_speed=max_speed_value,
                       acceleration=acceleration_value,
                       tyre_friction=tyre_friction_value)
    race_car.start_engine()
    race_car.accelerate()

    # Act
    race_car.apply_brakes()

    # Assert
    assert race_car.current_speed == current_speed_value

def test_apply_breaks_when_race_car_object_current_speed_is_less_than_race_car_object_tyre_friction_returns_zero():
    # Arrange
    race_car = RaceCar(color='Red', max_speed=200, acceleration=40,
                       tyre_friction=15)
    race_car.start_engine()
    race_car.accelerate()
    current_speed_when_less_than_tyre_friction = 0

    # Act
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()

    # Assert
    assert race_car.current_speed == current_speed_when_less_than_tyre_friction

def test_apply_breaks_when_race_car_object_current_speed_is_equal_to_race_car_object_tyre_friction_returns_current_speed():
    # Arrange
    race_car = RaceCar(color='Red', max_speed=200, acceleration=40,
                       tyre_friction=10)
    race_car.start_engine()
    race_car.accelerate()
    current_speed = 10

    # Act
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()

    # Assert
    assert race_car.current_speed == current_speed
