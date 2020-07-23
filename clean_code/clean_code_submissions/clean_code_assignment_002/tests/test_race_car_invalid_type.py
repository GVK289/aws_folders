import pytest


from race_car import RaceCar

## Testing Exceptions of Atrribute values if not Positive type and Non-Zero ##

@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [
        (-1, 10, 3), (0, 30, 10), ('1', 30, 20)])
def test_race_car_object_max_speed_when_max_speed_value_is_invalid_raises_exception(max_speed, acceleration, tyre_friction):
    # Arrange
    color = 'Red'

    # Act
    with pytest.raises(Exception) as exception:
        assert RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)

    # Assert
    assert str(exception.value) == 'Invalid value for max_speed'

@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [
        (210, '10', 3), (100, 0, 10), (180, -30, 20)])
def test_race_car_object_acceleration_when_acceleration_value_is_invalid_raises_exception(max_speed, acceleration, tyre_friction):
    # Arrange
    color = 'Red'

    # Act
    with pytest.raises(Exception) as exception:
        assert RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)

    # Assert
    assert str(exception.value) == 'Invalid value for acceleration'

@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [
        (210, 30, '10'), (100, 20, -1), (180, 40, 0)])
def test_race_car_object_tyre_friction_when_tyre_friction_value_is_invalid_raises_exception(max_speed, acceleration, tyre_friction):
    # Arrange
    color = 'Red'

    # Act
    with pytest.raises(Exception) as exception:
        assert RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)

    # Assert
    assert str(exception.value) == 'Invalid value for tyre_friction'
