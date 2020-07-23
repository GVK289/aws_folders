import pytest


from truck import Truck

def test_apply_brakes_when_truck_object_is_in_motion_returns_current_speed(truck):
    # Arrange
    truck.start_engine()
    truck.accelerate()
    truck.accelerate()
    current_speed = 70

    # Act
    truck.apply_brakes()

    # Assert
    assert truck.current_speed == current_speed

@pytest.mark.parametrize(
    """color, max_speed, acceleration, tyre_friction,
    max_cargo_weight, current_speed""", [
        ('Red', 200, 50, 20, 180, 30), ('Blue', 150, 25, 25, 100, 0),
        ('Black', 250, 20, 30, 100, 0)])
def test_apply_breaks_when_truck_object_current_speed_is_more_than_or_equal_to_truck_object_tyre_friction_returns_current_speed(color, max_speed, acceleration, tyre_friction, max_cargo_weight, current_speed):
    # Arrange
    truck = Truck(color=color, max_speed=max_speed, acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    truck.start_engine()
    truck.accelerate()

    # Act
    truck.apply_brakes()

    # Assert
    assert truck.current_speed == current_speed

def test_apply_breaks_when_truck_object_current_speed_is_less_than_truck_object_tyre_friction_returns_zero():
    # Arrange
    truck = Truck(color='Red', max_speed=200, acceleration=40,
                  tyre_friction=15, max_cargo_weight=80)
    truck.start_engine()
    truck.accelerate()
    current_speed_when_less_than_tyre_friction = 0

    # Act
    truck.apply_brakes()
    truck.apply_brakes()
    truck.apply_brakes()

    # Assert
    assert truck.current_speed == current_speed_when_less_than_tyre_friction

def test_apply_breaks_when_truck_object_current_speed_is_equal_to_truck_object_tyre_friction_returns_current_speed():
    # Arrange
    truck = Truck(color='Red', max_speed=200, acceleration=40,
                  tyre_friction=10, max_cargo_weight=90)
    truck.start_engine()
    truck.accelerate()
    current_speed = 10

    # Act
    truck.apply_brakes()
    truck.apply_brakes()
    truck.apply_brakes()

    # Assert
    assert truck.current_speed == current_speed
