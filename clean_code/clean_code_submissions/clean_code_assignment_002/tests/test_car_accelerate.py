import pytest


from car import Car

def test_car_object_accelerate_when_engine_is_started_returns_current_speed(car):
    # Arrange
    car.start_engine()
    current_speed = 40

    # Act
    car.accelerate()

    # Assert
    assert car.current_speed == current_speed

def test_car_object_accelerate_when_car_object_current_speed_is_equal_to_car_object_max_speed_limit_returns_max_speed(car):
    # Arrange
    car.start_engine()
    max_speed = 200

    # Act
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()

    # Assert
    assert car.current_speed == max_speed

def test_car_object_accelerate_when_car_engine_is_stop_returns_start_the_engine_to_accelerate(capsys, car):
    # Act
    car.accelerate()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == 'Start the engine to accelerate\n'

@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction", [
        ('Red', 1, 1, 1), ('Blue', 150, 30, 10),
        ('Black', 200, 40, 10)])
def test_car_object_accelerate_when_car_object_current_speed_is_more_than_car_object_max_speed_limit_returns_max_speed(color, max_speed, acceleration, tyre_friction):
    # Arrange
    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)
    car.start_engine()

    # Act
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()

    # Asset
    assert car.current_speed == max_speed

def test_car_object_current_speed_when_car_object_is_in_idle_postion_intially_returns_zero():
    # Arrange
    car = Car(color='Red', max_speed=180, acceleration=45, tyre_friction=4)

    # Act
    car_idle_initial_speed = car.current_speed

    # Act
    assert car_idle_initial_speed == 0

def test_car_object_current_speed_when_car_object_engine_is_stopped_from_motion_returns_current_speed():
    # Arrange
    car = Car(color='Red', max_speed=180, acceleration=45, tyre_friction=4)
    car.start_engine()
    current_speed = 135
    car.accelerate()
    car.accelerate()
    car.accelerate()

    # Act
    car.stop_engine()

    # Assert
    assert car.current_speed == current_speed
