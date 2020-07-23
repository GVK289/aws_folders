import pytest


from car import Car

def test_apply_brakes_when_car_object_is_in_motion_returns_current_speed(car):
    # Arrange
    car.start_engine()
    car.accelerate()
    car.accelerate()
    current_speed = 70

    # Act
    car.apply_brakes()

    # Assert
    assert car.current_speed == current_speed

@pytest.mark.parametrize(
    "color,max_speed, acceleration, tyre_friction, current_speed", [
        ('Red', 200, 50, 20, 30), ('Blue', 150, 25, 25, 0)])
def test_apply_breaks_when_car_object_current_speed_is_more_than_or_equal_to_car_object_tyre_friction_returns_current_speed(color, max_speed, acceleration, tyre_friction, current_speed):
    # Arrange
    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)
    car.start_engine()
    car.accelerate()

    # Act
    car.apply_brakes()

    # Assert
    assert car.current_speed == current_speed

def test_apply_breaks_when_car_object_current_speed_is_less_than_car_object_tyre_friction_returns_zero():
    # Arrange
    car = Car(color='Red', max_speed=200, acceleration=40, tyre_friction=15)
    car.start_engine()
    car.accelerate()
    current_speed_when_less_than_tyre_friction = 0

    # Act
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()

    # Assert
    assert car.current_speed == current_speed_when_less_than_tyre_friction

def test_apply_breaks_when_car_object_current_speed_is_equal_to_car_object_tyre_friction_returns_current_speed():
    # Arrange
    car = Car(color='Red', max_speed=200, acceleration=40, tyre_friction=10)
    car.start_engine()
    car.accelerate()
    current_speed = 10

    # Act
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()

    # Assert
    assert car.current_speed == current_speed
