import pytest


######## *********** Testing Encapusulation  ***********  ########

def test_encapsulation_of_car_object_color(car):
    # Act
    with pytest.raises(Exception) as exception:
        car.color = 'Black'

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_car_object_acceleration(car):
    # Act
    with pytest.raises(Exception) as exception:
        car.acceleration = 20

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_car_object_max_speed(car):

    # Act
    with pytest.raises(Exception) as exception:
        car.max_speed = 400

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_car_object_tyre_friction(car):
    # Act
    with pytest.raises(Exception) as exception:
        car.tyre_friction = 40

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_car_object_is_engine_started(car):
    # Act
    with pytest.raises(Exception) as exception:
        car.is_engine_started = True

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_car_object_current_speed(car):
    # Act
    with pytest.raises(Exception) as exception:
        car.current_speed = 300

    # Assert
    assert str(exception.value) == "can't set attribute"
