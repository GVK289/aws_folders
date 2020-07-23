import pytest


from truck import Truck

def test_unload_in_truck_when_truck_is_in_motion_returns_cannot_unload_cargo_during_motion(capsys, truck):
    # Arrange
    truck.start_engine()
    truck.accelerate()
    unload_cargo_weight = 40

    #  Act
    truck.unload(unload_cargo_weight)
    captured = capsys.readouterr()

    # Asset
    assert captured.out == 'Cannot unload cargo during motion\n'

@pytest.mark.parametrize(
    """color, max_speed, acceleration, tyre_friction, max_cargo_weight,
    unload_cargo_weight""", [
        ('Red', 200, 50, 20, 180, 1), ('Blue', 150, 25, 25, 100, 1),
        ('Black', 250, 20, 30, 100, 90)])
def test_unload_in_truck_when_truck_engine_is_started_and_not_in_motion_and_truck_is_unloaded_without_load_with_given_unload_weight_returns_zeo(color, max_speed, acceleration, tyre_friction, max_cargo_weight, unload_cargo_weight):
    # Arrange
    truck = Truck(color=color, max_speed=max_speed, acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    truck.start_engine()

    # Act
    truck.unload(unload_cargo_weight)

    # Assert
    assert truck.cargo_weight == 0

@pytest.mark.parametrize(
    """max_speed, acceleration, max_cargo_weight,
    load_cargo_weight, unload_cargo_weight, remained_cargo_weight""", [
        (300, 70, 190, 100, 90, 10),
        (250, 20, 150, 1, 1, 0)])
def test_unload_in_loaded_truck_when_truck_is_not_in_motion_with_decrease_of_load_with_given_unload_cargo_weight_returns_remained_cargo_weight_in_truck(max_speed, acceleration, max_cargo_weight, load_cargo_weight, unload_cargo_weight, remained_cargo_weight):
    # Arrange
    color = 'Red'
    tyre_friction = 30
    truck = Truck(color=color, max_speed=max_speed, acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    truck.start_engine()
    truck.load(load_cargo_weight)

    # Act
    truck.unload(unload_cargo_weight)

    # Assert
    assert truck.cargo_weight == remained_cargo_weight

def test_unload_in_loaded_truck_when_truck_is_not_in_motion_with_decrease_of_load_with_given_unload_cargo_weight_more_than_load_in_truck_returns_cannot_unload_cargo_as_load_in_truck_is_less_than_given_unload_cargo_weight(capsys):
    # Arrange
    color = 'Blue'
    max_speed = 150
    acceleration = 30
    tyre_friction = 10
    max_cargo_weight = 100
    load_cargo_weight = 80
    unload_cargo_weight = 100
    truck = Truck(color=color, max_speed=max_speed, acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    limit_message = "Can't unload cargo less than given unload cargo weight\n"
    truck.load(load_cargo_weight)

    # Act
    truck.unload(unload_cargo_weight)
    captured = capsys.readouterr()

    # Assert
    assert captured.out == limit_message
