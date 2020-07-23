import pytest


from race_car import RaceCar

def test_race_car_object_accelerate_when_engine_is_started_returns_current_speed(race_car):
    # Arrange
    race_car.start_engine()
    current_speed = 40

    # Act
    race_car.accelerate()

    # Assert
    assert race_car.current_speed == current_speed

def test_race_car_object_accelerate_when_race_car_object_current_speed_is_equal_to_race_car_object_max_speed_limit_returns_max_speed(race_car):
    # Arrange
    race_car.start_engine()
    max_speed = 200

    # Act
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()

    # Assert
    assert race_car.current_speed == max_speed


def test_race_car_object_accelerate_when_race_car_engine_is_stop_returns_start_the_engine_to_accelerate(capsys, race_car):
    # Act
    race_car.accelerate()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == 'Start the engine to accelerate\n'

@pytest.mark.parametrize(
    "color,  max_speed, acceleration, tyre_friction", [
        ('Red', 1, 1, 1), ('Blue', 150, 30, 10),
        ('Black', 200, 40, 10)])
def test_race_car_object_accelerate_when_race_car_object_current_speed_is_more_than_race_car_object_max_speed_limit_and_nitro_is_zero_returns_max_speed(color, max_speed, acceleration, tyre_friction):
    # Arrange
    race_car = RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)
    race_car.start_engine()

    # Act
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()

    # Asset
    assert race_car.current_speed == max_speed

def test_race_car_object_current_speed_when_race_car_object_is_in_idle_postion_intially_and_nitro_is_zero_returns_zero():
    # Arrange
    race_car = RaceCar(color='Red', max_speed=180, acceleration=45,
                       tyre_friction=4)

    # Act
    race_car_idle_initial_speed = race_car.current_speed

    # Act
    assert race_car_idle_initial_speed == 0

def test_race_car_object_current_speed_when_race_car_object_engine_is_stopped_from_motion_and_nitro_is_zero_returns_current_speed():
    # Arrange
    race_car = RaceCar(color='Red', max_speed=180, acceleration=45,
                       tyre_friction=4)
    race_car.start_engine()
    current_speed = 135
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()

    # Act
    race_car.stop_engine()

    # Assert
    assert race_car.current_speed == current_speed
