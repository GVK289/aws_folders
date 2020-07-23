import pytest


from truck import Truck

###########  Testing the class Atrribute values Formats  ###########

def test_truck_object_color_when_color_type_is_invalid_raises_exception():
    """test that exception is raised for invalid color format"""
    # Arrange
    color = 1
    max_speed = 30
    acceleration = 10
    tyre_friction = 3
    max_cargo_weight = 150

    # Act
    with pytest.raises(Exception) as exception:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration, tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)

    # Assert
    assert str(exception.value) == "Invalid value for color"

# Testing Exceptions of Atrribute values if not Positive type and Non-Zero #

@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction, max_cargo_weight", [
        (-1, 10, 3, 200), (0, 30, 10, 150), ('1', 30, 20, 200)])
def test_truck_object_max_speed_when_max_speed_value_is_invalid_raises_exception(max_speed, acceleration, tyre_friction, max_cargo_weight):
    # Arrange
    color = 'Red'

    # Act
    with pytest.raises(Exception) as exception:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration, tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)

    # Assert
    assert str(exception.value) == 'Invalid value for max_speed'

@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction, max_cargo_weight", [
        (210, '10', 3, 150), (100, 0, 10, 180), (180, -30, 20, 170)])
def test_truck_object_acceleration_when_acceleration_value_is_invalid_raises_exception(max_speed, acceleration, tyre_friction, max_cargo_weight):
    # Arrange
    color = 'Red'

    # Act
    with pytest.raises(Exception) as exception:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration, tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)
    # Assert
    assert str(exception.value) == 'Invalid value for acceleration'

@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction, max_cargo_weight", [
        (210, 30, '10', 160), (100, 20, -1, 200), (180, 40, 0, 100)])
def test_truck_object_tyre_friction_when_tyre_friction_value_is_invalid_raises_exception(max_speed, acceleration, tyre_friction, max_cargo_weight):
    # Arrange
    color = 'Red'

    # Act
    with pytest.raises(Exception) as exception:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration, tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)

    # Assert
    assert str(exception.value) == 'Invalid value for tyre_friction'

@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction, max_cargo_weight", [
        (210, 30, 10, '160'), (100, 20, 1, -1), (180, 40, 10, 0)])
def test_truck_object_max_cargo_when_max_cargo_type_is_invalid_raises_exception(max_speed, acceleration, tyre_friction, max_cargo_weight):
    # Arrange
    color = 'Red'

    # Act
    with pytest.raises(Exception) as exception:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration, tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)

    # Assert
    assert str(exception.value) == 'Invalid value for max_cargo_weight'
