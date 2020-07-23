import pytest


######## *********** Testing Encapusulation  ***********  ########

def test_encapsulation_of_race_car_object_color(race_car):
    # Act
    with pytest.raises(Exception) as exception:
        race_car.color = 'Black'

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_race_car_object_acceleration(race_car):
    # Act
    with pytest.raises(Exception) as exception:
        race_car.acceleration = 20

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_race_car_object_max_speed(race_car):
    # Act
    with pytest.raises(Exception) as exception:
        race_car.max_speed = 400

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_race_car_object_tyre_friction(race_car):
    # Act
    with pytest.raises(Exception) as exception:
        race_car.tyre_friction = 40

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_race_car_object_is_engine_started(race_car):
    # Act
    with pytest.raises(Exception) as exception:
        race_car.is_engine_started = True

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_race_car_object_current_speed(race_car):
    # Act
    with pytest.raises(Exception) as exception:
        race_car.current_speed = 300

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_race_car_object_nitro(race_car):
    # Act
    with pytest.raises(Exception) as exception:
        race_car.nitro = 100

    # Assert
    assert str(exception.value) == "can't set attribute"
