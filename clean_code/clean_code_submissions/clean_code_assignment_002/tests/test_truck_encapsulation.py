import pytest


######## *********** Testing Encapusulation  ***********  ########

def test_encapsulation_of_truck_object_color(truck):
    # Act
    with pytest.raises(Exception) as exception:
        truck.color = 'Black'

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_truck_object_acceleration(truck):
    # Act
    with pytest.raises(Exception) as exception:
        truck.acceleration = 20

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_truck_object_max_speed(truck):

    # Act
    with pytest.raises(Exception) as exception:
        truck.max_speed = 400

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_truck_object_tyre_friction(truck):
    # Act
    with pytest.raises(Exception) as exception:
        truck.tyre_friction = 40

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_truck_object_max_cargo_weight(truck):
    # Act
    with pytest.raises(Exception) as exception:
        truck.max_cargo_weight = 300

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_truck_object_is_engine_started(truck):
    # Act
    with pytest.raises(Exception) as exception:
        truck.is_engine_started = True

    # Assert
    assert str(exception.value) == "can't set attribute"

def test_encapsulation_of_truck_object_current_speed(truck):
    # Act
    with pytest.raises(Exception) as exception:
        truck.current_speed = 300

    # Assert
    assert str(exception.value) == "can't set attribute"
