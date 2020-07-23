import pytest


from truck import Truck
@pytest.fixture
def truck():  # Our Fixture function
    # Arrange
    color = 'Red'
    max_speed = 200
    acceleration = 40
    tyre_friction = 10
    max_cargo_weight = 180

    truck_obj = Truck(color=color, max_speed=max_speed,
                      acceleration=acceleration, tyre_friction=tyre_friction,
                      max_cargo_weight=max_cargo_weight)
    return truck_obj

########### Testing wether One object is creating ###########

def test_truck_creating_one_truck_object_with_given_instances_creates_truck_object():
    # Arrange
    color = 'Black'
    max_speed = 200
    acceleration = 30
    tyre_friction = 7
    max_cargo_weight = 150
    truck_obj = Truck(color=color, max_speed=max_speed,
                      acceleration=acceleration, tyre_friction=tyre_friction,
                      max_cargo_weight=max_cargo_weight)

    # Act
    result = isinstance(truck_obj, Truck)

    # Assert
    assert result is True

########### Testing wether Multiple objects are creating ###########

def test_truck_creating_multiple_truck_objects_with_given_instances_creates_truck_objects():
    # Arrange
    truck_obj1 = Truck(color='Red', max_speed=250, acceleration=50,
                       tyre_friction=10, max_cargo_weight=300)
    truck_obj2 = Truck(color='Black', max_speed=200, acceleration=40,
                       tyre_friction=7, max_cargo_weight=250)

    # Act
    creation_of_truck_object1 = isinstance(truck_obj1, Truck)
    creation_of_truck_object2 = isinstance(truck_obj2, Truck)
    result = truck_obj1 == truck_obj2

    # Assert
    assert creation_of_truck_object1 is True
    assert creation_of_truck_object2 is True
    assert result is False

###########  Testing the class Atrribute values Formats  ###########

def test_truck_object_color_when_color_type_is_invalid_raises_exception():
    """test that exception is raised for invalid color format"""
    # Arrange
    from  truck import Truck
    color = 1
    max_speed = 30
    acceleration = 10
    tyre_friction = 3
    max_cargo_weight = 150

    # Act
    with pytest.raises(Exception) as e:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration, tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)

    # Assert
    assert str(e.value) == "Invalid value for color"

'Testing Exceptions of Atrribute values if not Positive type and Non-Zero'


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction, max_cargo_weight", [
        (-1, 10, 3, 200), (0, 30, 10, 150), ('1', 30, 20, 200)])
def test_truck_object_max_speed_when_max_speed_value_is_invalid_raises_exception(max_speed, acceleration, tyre_friction, max_cargo_weight):
    # Arrange
    color = 'Red'

    # Act
    with pytest.raises(Exception) as e:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration, tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)

    # Assert
    assert str(e.value) == 'Invalid value for max_speed'

@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction, max_cargo_weight", [
        (210, '10', 3, 150), (100, 0, 10, 180), (180, -30, 20, 170)])
def test_truck_object_acceleration_when_acceleration_value_is_invalid_raises_exception(max_speed, acceleration, tyre_friction, max_cargo_weight):
    # Arrange
    color = 'Red'

    # Act
    with pytest.raises(Exception) as e:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration, tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)
    # Assert
    assert str(e.value) == 'Invalid value for acceleration'

@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction, max_cargo_weight", [
        (210, 30, '10', 160), (100, 20, -1, 200), (180, 40, 0, 100)])
def test_truck_object_tyre_friction_when_tyre_friction_value_is_invalid_raises_exception(max_speed, acceleration, tyre_friction, max_cargo_weight):
    # Arrange
    color = 'Red'

    # Act
    with pytest.raises(Exception) as e:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration, tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)

    # Assert
    assert str(e.value) == 'Invalid value for tyre_friction'

@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction, max_cargo_weight", [
        (210, 30, 10, '160'), (100, 20, 1, -1), (180, 40, 10, 0)])
def test_truck_object_max_cargo_when_max_cargo_type_is_invalid_raises_exception(max_speed, acceleration, tyre_friction, max_cargo_weight):
    # Arrange
    color = 'Red'

    # Act
    with pytest.raises(Exception) as e:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration, tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)

    # Assert
    assert str(e.value) == 'Invalid value for max_cargo_weight'

########### ******** Multiple Testings ******** ###########

def test_truck_object_when_engine_is_started_returns_true(truck):
    # Arrange
    truck.start_engine()

    # Act
    result = truck.is_engine_started

    # Assert
    assert result is True

def test_truck_object_when_engine_is_started_twice_returns_true(truck):
    # Arrange
    truck.start_engine()
    truck.start_engine()

    # Act
    result = truck.is_engine_started

    # Assert
    assert result is True

def test_truck_object_when_engine_is_stop_returns_false(truck):
    # Arrange
    truck.stop_engine()

    # Act
    result = truck.is_engine_started

    # Assert
    assert result is False

def test_truck_object_when_engine_is_stop_twice_returns_false(truck):
    # Arrange
    truck.stop_engine()
    truck.stop_engine()

    # Act
    result = truck.is_engine_started

    # Assert
    assert result is False

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
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()

    # Act
    truck.accelerate()

    # Assert
    assert truck.current_speed == max_speed

# ***** New  capsys terminology ******* #

def test_truck_object_accelerate_when_truck_engine_is_stop_returns_start_the_engine_to_accelerate(capsys, truck):
    # Act
    truck.accelerate()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == 'Start the engine to accelerate\n'

def test_truck_object_sound_horn_when_engine_is_started_returns_Honk_Honk(capsys, truck):
    # Arrange
    truck.start_engine()

    # Act
    truck.sound_horn()
    captured = capsys.readouterr()

    # Asset
    assert captured.out == 'Honk Honk\n'

def test_truck_object_sound_horn_when_engine_is_stop_returns_start_the_engine_to_sound_hor(capsys, truck):
    # Act
    truck.sound_horn()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == 'Start the engine to sound_horn\n'

######## *********** Testing Encapusulation  ***********  ########

def test_encapsulation_of_truck_object_color(truck):
    # Act
    with pytest.raises(Exception) as e:
        truck.color = 'Black'

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_truck_object_acceleration(truck):
    # Act
    with pytest.raises(Exception) as e:
        truck.acceleration = 20

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_truck_object_max_speed(truck):

    # Act
    with pytest.raises(Exception) as e:
        truck.max_speed = 400

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_truck_object_tyre_friction(truck):
    # Act
    with pytest.raises(Exception) as e:
        truck.tyre_friction = 40

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_truck_object_max_cargo_weight(truck):
    # Act
    with pytest.raises(Exception) as e:
        truck.max_cargo_weight = 300

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_truck_object_is_engine_started(truck):
    # Act
    with pytest.raises(Exception) as e:
        truck.is_engine_started = True

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_truck_object_current_speed(truck):
    # Act
    with pytest.raises(Exception) as e:
        truck.current_speed = 300

    # Assert
    assert str(e.value) == "can't set attribute"

#---------------------------------------------------------------------#

@pytest.mark.parametrize(
    """color, max_speed, acceleration,
    tyre_friction, max_cargo_weight, current_speed""", [
        ('Red', 1, 1, 1, 1, 1), ('Blue', 150, 30, 10, 200, 20),
        ('Black', 200, 40, 10, 180, 30)])
def test_truck_object_accelerate_when_truck_object_current_speed_is_more_than_truck_object_max_limit_returns_max_speed(color, max_speed, acceleration, tyre_friction, max_cargo_weight, current_speed):
    # Arrange
    truck = Truck(color=color, max_speed=max_speed, acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    truck.start_engine()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()

    # Act
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
    truck.apply_brakes()
    truck.apply_brakes()

    # Act
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
    truck.apply_brakes()
    truck.apply_brakes()

    # Act
    truck.apply_brakes()

    # Assert
    assert truck.current_speed == current_speed

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
    assert truck._cargo_weight == load_cargo_weight

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
    assert truck._cargo_weight == load_cargo_weight

@pytest.mark.parametrize(
    """color, max_speed, acceleration, tyre_friction, max_cargo_weight,
    load_cargo_weight""", [
        ('Red', 200, 50, 20, 180, 95), ('Blue', 150, 25, 25, 100, 60)])
def test_load_to_truck_when_truck_is_idle_and_truck_cargo_weight_is_more_than_max_cargo_weight_then_truck_is_loaded_with_given_load_returns_max_cargo_weight(color, max_speed, acceleration, tyre_friction, max_cargo_weight, load_cargo_weight, capsys):
    # Arrange
    truck = Truck(color=color, max_speed=max_speed, acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    limit_message = 'Cannot load cargo more than max limit: {}\n'.format(
        max_cargo_weight)
    truck.load(load_cargo_weight)

    # Act
    truck.load(load_cargo_weight)
    captured = capsys.readouterr()

    # Assert
    assert captured.out == limit_message

@pytest.mark.parametrize(
    """color, max_speed, acceleration, tyre_friction, max_cargo_weight,
    load_cargo_weight""", [('Blue', 150, 25, 25, 100, 150)])
def test_load_to_truck_when_truck_is_idle_and_truck_cargo_weight_is_equal_to_max_cargo_weight_then_truck_is_loaded_with_given_load_returns_max_cargo_weight(color, max_speed, acceleration, tyre_friction, max_cargo_weight, load_cargo_weight, capsys):

    # Arrange
    truck = Truck(color=color, max_speed=max_speed, acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    limit_message = 'Cannot load cargo more than max limit: {}\n'.format(
        max_cargo_weight)

    # Act
    truck.load(load_cargo_weight)
    captured = capsys.readouterr()

    # Assert
    assert captured.out == limit_message

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
    assert truck._cargo_weight == 0

@pytest.mark.parametrize(
    """color, max_speed, acceleration, tyre_friction, max_cargo_weight,
    load_cargo_weight, unload_cargo_weight, remained_cargo_weight""", [
        ('Red', 300, 70, 20, 190, 100, 90, 10),
        ('Black', 250, 20, 30, 150, 1, 1, 0)])
def test_unload_in_loaded_truck_when_truck_is_not_in_motion_with_decrease_of_load_with_given_unload_cargo_weight_returns_remained_cargo_weight_in_truck(color, max_speed, acceleration, tyre_friction, max_cargo_weight, load_cargo_weight, unload_cargo_weight, remained_cargo_weight):
    # Arrange
    truck = Truck(color=color, max_speed=max_speed, acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    truck.start_engine()
    truck.load(load_cargo_weight)

    # Act
    truck.unload(unload_cargo_weight)

    # Assert
    assert truck._cargo_weight == remained_cargo_weight

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
