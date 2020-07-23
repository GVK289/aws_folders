import pytest


from truck import Truck

def test_load_to_truck_when_truck_is_in_motion_returns_cannot_load_cargo_during_motion(capsys, truck):
    # Arrange
    truck.start_engine()
    truck.accelerate()
    load_cargo_weight = 40

    #  Act
    truck.load(load_cargo_weight)
    captured = capsys.readouterr()

    # Asset
    assert captured.out == 'Cannot load cargo during motion\n'

@pytest.mark.parametrize(
    """color, max_speed, acceleration, tyre_friction, max_cargo_weight,
    load_cargo_weight""", [
        ('Red', 200, 50, 20, 180, 30), ('Blue', 150, 25, 25, 100, 1),
        ('Black', 250, 20, 30, 100, 90)])
def test_load_to_truck_when_truck_is_idle_and_truck_cargo_weight_is_less_than_max_cargo_weight_then_truck_is_loaded_with_given_load_returns_load_cargo_weight(color, max_speed, acceleration, tyre_friction, max_cargo_weight, load_cargo_weight):
    # Arrange
    truck = Truck(color=color, max_speed=max_speed, acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    truck.start_engine()

    # Act
    truck.load(load_cargo_weight)

    # Assert
    assert truck.cargo_weight == load_cargo_weight

@pytest.mark.parametrize(
    """color, max_speed, acceleration, tyre_friction, max_cargo_weight,
    load_cargo_weight""", [
        ('Red', 200, 50, 20, 180, 30), ('Blue', 150, 25, 25, 100, 1),
        ('Black', 250, 20, 30, 100, 90), ('Green', 200, 50, 20, 180, 180)])
def test_load_to_truck_when_truck_engine_is_started_and_not_in_motion_and_truck_cargo_weight_is_less_than_max_cargo_weight_then_truck_is_loaded_with_given_load_returns_load_cargo_weight(color, max_speed, acceleration, tyre_friction, max_cargo_weight, load_cargo_weight):
    # Arrange
    truck = Truck(color=color, max_speed=max_speed, acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    truck.start_engine()

    # Act
    truck.load(load_cargo_weight)

    # Assert
    assert truck.cargo_weight == load_cargo_weight

@pytest.mark.parametrize(
    """max_speed, acceleration, tyre_friction, max_cargo_weight,
    load_cargo_weight""", [
        (200, 50, 20, 180, 95), (150, 25, 25, 100, 60)])
def test_load_to_truck_when_truck_is_idle_and_truck_cargo_weight_is_more_than_max_cargo_weight_then_truck_is_loaded_with_given_load_returns_max_cargo_weight(max_speed, acceleration, tyre_friction, max_cargo_weight, load_cargo_weight, capsys):
    # Arrange
    color = 'Red'
    truck = Truck(color=color, max_speed=max_speed, acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    limit_message = 'Cannot load cargo more than max limit: {}\n'.format(
        max_cargo_weight)

    # Act
    truck.load(load_cargo_weight)
    truck.load(load_cargo_weight)
    captured = capsys.readouterr()

    # Assert
    assert captured.out == limit_message

def test_load_to_truck_when_truck_is_idle_and_truck_cargo_weight_is_equal_to_max_cargo_weight_then_truck_is_loaded_with_given_load_returns_max_cargo_weight(capsys, truck):
    # Arrange
    truck = Truck(color='Blue', max_speed=150, acceleration=25,
                  tyre_friction=25, max_cargo_weight=100)
    load_cargo_weight = 150
    limit_message = 'Cannot load cargo more than max limit: {}\n'.format(
        truck.max_cargo_weight)

    # Act
    truck.load(load_cargo_weight)
    captured = capsys.readouterr()

    # Assert
    assert captured.out == limit_message
