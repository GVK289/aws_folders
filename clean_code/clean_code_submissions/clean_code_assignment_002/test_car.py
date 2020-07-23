import pytest
from car import Car


########### ******** Testing wether One object is creating ******** ###########

def test_car_creating_one_car_object_with_given_instances_creates_car_object():
    # Arrange
    color = 'Black'
    max_speed = 200
    acceleration = 30
    tyre_friction = 7
    car_obj = Car(color=color, max_speed=max_speed,
                  acceleration=acceleration, tyre_friction=tyre_friction)

    # Act
    result = isinstance(car_obj, Car)

    # Assert
    assert result is True

########### ******** Testing wether Multiple objects are creating ******** ###########

def test_car_creating_multiple_car_objects_with_given_instances_creates_car_objects():
    # Arrange
    car_obj1 = Car(color='Red', max_speed=250, acceleration=50,
                   tyre_friction=10)
    car_obj2 = Car(color='Black', max_speed=200, acceleration=40,
                   tyre_friction=7)

    # Act
    creation_of_car_object1 = isinstance(car_obj1, Car)
    creation_of_car_object2 = isinstance(car_obj2, Car)
    result = car_obj1 == car_obj2

    # Assert
    assert creation_of_car_object1 is True
    assert creation_of_car_object2 is True
    assert result is False

########### Testing the class Atrribute values Formats  ###########

def test_car_object_color_when_color_type_is_invalid_raises_exception():
    """test that exception is raised for invalid color format"""
    # Arrange
    color = 1
    max_speed = 30
    acceleration = 10
    tyre_friction = 3

    # Act
    with pytest.raises(Exception) as e:
        assert Car(color=color, max_speed=max_speed,
                   acceleration=acceleration, tyre_friction=tyre_friction)

    # Assert
    assert str(e.value) == "Invalid value for color"

""" **** Testing Exceptions of class Atrribute values
             if not Positive type and Non-Zero  **** """

@pytest.mark.parametrize("max_speed, acceleration, tyre_friction",
                         [(-1, 10, 3), (0, 30, 10), ('1', 30, 20)])
def test_car_object_max_speed_when_max_speed_value_is_invalid_raises_exception(max_speed, acceleration, tyre_friction):
    # Arrange
    color = 'Red'

    # Act
    with pytest.raises(Exception) as e:
        assert Car(color=color, max_speed=max_speed,
                   acceleration=acceleration, tyre_friction=tyre_friction)

    # Assert
    assert str(e.value) == 'Invalid value for max_speed'

@pytest.mark.parametrize("max_speed, acceleration, tyre_friction",
                         [(210, '10', 3), (100, 0, 10), (180, -30, 20)])
def test_car_object_acceleration_when_acceleration_value_is_invalid_raises_exception(max_speed, acceleration, tyre_friction):
    # Arrange
    color = 'Red'

    # Act
    with pytest.raises(Exception) as e:
        assert Car(color=color, max_speed=max_speed,
                   acceleration=acceleration, tyre_friction=tyre_friction)

    # Assert
    assert str(e.value) == 'Invalid value for acceleration'

@pytest.mark.parametrize("max_speed, acceleration, tyre_friction",
                         [(210, 30, '10'), (100, 20, -1), (180, 40, 0)])
def test_car_object_tyre_friction_when_tyre_friction_value_is_invalid_raises_exception(max_speed, acceleration, tyre_friction):
    # Arrange
    color = 'Red'

    #Act
    with pytest.raises(Exception) as e:
        assert Car(color=color, max_speed=max_speed,
                   acceleration=acceleration, tyre_friction=tyre_friction)

    # Assert
    assert str(e.value) == 'Invalid value for tyre_friction'

########### ******** Multiple Testings ******** ###########

@pytest.fixture
def car():  # Our Fixture function
    # Arrange
    color = 'Red'
    max_speed = 200
    acceleration = 40
    tyre_friction = 10

    car_obj = Car(color=color, max_speed=max_speed,
                  acceleration=acceleration, tyre_friction=tyre_friction)
    return car_obj

def test_car_object_when_engine_is_started_returns_true(car):
    # Arrange
    car.start_engine()

    # Act
    car_engine_start = car.is_engine_started

    # Assert
    assert car_engine_start is True

def test_car_object_when_engine_is_started_twice_returns_true(car):
    # Arrange
    car.start_engine()
    car.start_engine()

    # Act
    car_engine_start = car.is_engine_started

    # Assert
    assert car_engine_start is True

def test_car_object_when_engine_is_stop_returns_false(car):
    # Arrange
    car.stop_engine()

    # Act
    car_engine_stop = car.is_engine_started

    # Assert
    assert car_engine_stop is False

def test_car_object_when_engine_is_stop_twice_returns_false(car):
    # Arrange
    car.stop_engine()
    car.stop_engine()

    # Act
    car_engine_stop = car.is_engine_started

    # Assert
    assert car_engine_stop is False

def test_car_object_accelerate_when_engine_is_started_returns_current_speed(car):
    # Arrange
    car.start_engine()
    current_speed = 40

    # Act
    car.accelerate()

    # Assert
    assert car.current_speed == current_speed

def test_car_object_accelerate_when_car_object_current_speed_is_equal_to_car_object_max_speed_limit_returns_max_speed(car):
    # Arrange
    car.start_engine()
    max_speed = 200
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()

    # Act
    car.accelerate()

    # Assert
    assert car.current_speed == max_speed

# ***** New  capsys terminology ******* #

def test_car_object_accelerate_when_car_engine_is_stop_returns_start_the_engine_to_accelerate(capsys, car):
    # Act
    car.accelerate()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == 'Start the engine to accelerate\n'

def test_car_object_sound_horn_when_engine_is_started_returns_Beep_Beep(capsys, car):
    # Arrange
    car.start_engine()

    # Act
    car.sound_horn()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == 'Beep Beep\n'

def test_car_object_sound_horn_when_engine_is_stop_returns_start_the_engine_to_sound_horn(capsys, car):
    # Act
    car.sound_horn()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == 'Start the engine to sound_horn\n'

######## *********** Testing Encapusulation  ***********  ########

def test_encapsulation_of_car_object_color(car):
    # Act
    with pytest.raises(Exception) as e:
        car.color = 'Black'

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_car_object_acceleration(car):
    # Act
    with pytest.raises(Exception) as e:
        car.acceleration = 20

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_car_object_max_speed(car):

    # Act
    with pytest.raises(Exception) as e:
        car.max_speed = 400

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_car_object_tyre_friction(car):
    # Act
    with pytest.raises(Exception) as e:
        car.tyre_friction = 40

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_car_object_is_engine_started(car):
    # Act
    with pytest.raises(Exception) as e:
        car.is_engine_started = True

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_car_object_current_speed(car):
    # Act
    with pytest.raises(Exception) as e:
        car.current_speed = 300

    # Assert
    assert str(e.value) == "can't set attribute"

#---------------------------------------#

@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction, current_speed", [
        ('Red', 1, 1, 1, 1), ('Blue', 150, 30, 10, 20),
        ('Black', 200, 40, 10, 30)])
def test_car_object_accelerate_when_car_object_current_speed_is_more_than_car_object_max_speed_limit_returns_max_speed(color, max_speed, acceleration, tyre_friction, current_speed):
    # Arrange
    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)
    car.start_engine()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()

    # Act
    car.accelerate()

    # Asset
    assert car.current_speed == max_speed

def test_car_object_current_speed_when_car_object_is_in_idle_postion_intially_returns_zero():
    # Arrange
    car = Car(color='Red', max_speed=180, acceleration=45, tyre_friction=4)

    # Act
    car_idle_initial_speed = car.current_speed

    # Act
    assert car_idle_initial_speed == 0

def test_car_object_current_speed_when_car_object_engine_is_stopped_from_motion_returns_current_speed():
    # Arrange
    car = Car(color='Red', max_speed=180, acceleration=45, tyre_friction=4)
    car.start_engine()
    current_speed = 135
    car.accelerate()
    car.accelerate()
    car.accelerate()

    # Act
    car.stop_engine()

    # Assert
    assert car.current_speed == current_speed

def test_apply_brakes_when_car_object_is_in_motion_returns_current_speed(car):
    # Arrange
    car.start_engine()
    car.accelerate()
    car.accelerate()
    current_speed = 70

    # Act
    car.apply_brakes()

    # Assert
    assert car.current_speed == current_speed

@pytest.mark.parametrize(
    "color,max_speed, acceleration, tyre_friction, current_speed", [
        ('Red', 200, 50, 20, 30), ('Blue', 150, 25, 25, 0)])
def test_apply_breaks_when_car_object_current_speed_is_more_than_or_equal_to_car_object_tyre_friction_returns_current_speed(color, max_speed, acceleration, tyre_friction, current_speed):
    # Arrange
    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)
    car.start_engine()
    car.accelerate()

    # Act
    car.apply_brakes()

    # Assert
    assert car.current_speed == current_speed

def test_apply_breaks_when_car_object_current_speed_is_less_than_car_object_tyre_friction_returns_zero():
    # Arrange
    car = Car(color='Red', max_speed=200, acceleration=40, tyre_friction=15)
    car.start_engine()
    car.accelerate()
    current_speed_when_less_than_tyre_friction = 0
    car.apply_brakes()
    car.apply_brakes()

    # Act
    car.apply_brakes()

    # Assert
    assert car.current_speed == current_speed_when_less_than_tyre_friction

def test_apply_breaks_when_car_object_current_speed_is_equal_to_car_object_tyre_friction_returns_current_speed():
    # Arrange
    car = Car(color='Red', max_speed=200, acceleration=40, tyre_friction=10)
    car.start_engine()
    car.accelerate()
    current_speed = 10
    car.apply_brakes()
    car.apply_brakes()

    # Act
    car.apply_brakes()

    # Assert
    assert car.current_speed == current_speed
