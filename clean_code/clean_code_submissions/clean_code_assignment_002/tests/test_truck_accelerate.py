import pytest


from truck import Truck

def test_truck_object_accelerate_when_engine_is_started_returns_current_speed(truck):
    # Arrange
    truck.start_engine()
    current_speed = 40

    # Act()
    truck.accelerate()

    # Assert
    assert truck.current_speed == current_speed

def test_truck_object_accelerate_when_truck_object_current_speed_is_equal_to_truck_object_max_limit_returns_max_speed(truck):
    # Arrange
    truck.start_engine()
    max_speed = 200

    # Act
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()

    # Assert
    assert truck.current_speed == max_speed

def test_truck_object_accelerate_when_truck_engine_is_stop_returns_start_the_engine_to_accelerate(capsys, truck):
    # Act
    truck.accelerate()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == 'Start the engine to accelerate\n'

@pytest.mark.parametrize(
    """color, max_speed, acceleration,
    tyre_friction, max_cargo_weight""", [
        ('Red', 1, 1, 1, 1), ('Blue', 150, 30, 10, 200),
        ('Black', 200, 40, 10, 180)])
def test_truck_object_accelerate_when_truck_object_current_speed_is_more_than_truck_object_max_limit_returns_max_speed(color, max_speed, acceleration, tyre_friction, max_cargo_weight):
    # Arrange
    truck = Truck(color=color, max_speed=max_speed, acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    truck.start_engine()

    # Act
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()

    # Asset
    assert truck.current_speed == max_speed

def test_truck_object_current_speed_when_truck_object_is_in_idle_postion_intially_returns_zero():
    # Arrange
    truck = Truck(color='Red', max_speed=180, acceleration=45,
                  tyre_friction=4, max_cargo_weight=150)

    # Act
    truck_idle_initial_speed = truck.current_speed

    # Assert
    assert truck_idle_initial_speed == 0

def test_truck_object_current_speed_when_truck_object_is_stop_from_motion_returns_current_speed():
    # Arrange
    truck = Truck(color='Red', max_speed=180, acceleration=45,
                  tyre_friction=4, max_cargo_weight=100)
    truck.start_engine()
    current_speed = 135
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()

    # Act
    truck.stop_engine()

    # Assert
    assert truck.current_speed == current_speed
