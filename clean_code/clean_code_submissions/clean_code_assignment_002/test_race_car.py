import pytest


from race_car import RaceCar
@pytest.fixture
def race_car():  # Our Fixture function
    # Arrange
    color = 'Red'
    max_speed = 200
    acceleration = 40
    tyre_friction = 10

    race_car_obj = RaceCar(color=color, max_speed=max_speed,
                           acceleration=acceleration,
                           tyre_friction=tyre_friction)
    return race_car_obj

###########  Testing wether One object is creating  ###########

def test_race_car_creating_one_race_car_object_with_given_instances_creates_race_car_object():
    # Arrange
    color = 'Black'
    max_speed = 200
    acceleration = 30
    tyre_friction = 7
    car_obj = RaceCar(color=color, max_speed=max_speed,
                      acceleration=acceleration,
                      tyre_friction=tyre_friction)

    # Act
    result = isinstance(car_obj, RaceCar)

    # Assert
    assert result is True

########### Testing wether Multiple objects are creating  ###########

def test_race_car_creating_multiple_race_car_objects_with_given_instances_creates_race_car_objects():
    # Arrange
    race_car_obj1 = RaceCar(color='Red', max_speed=250, acceleration=50,
                            tyre_friction=10)
    race_car_obj2 = RaceCar(color='Black', max_speed=200, acceleration=40,
                            tyre_friction=7)

    # Act
    creation_of_race_car_object1 = isinstance(race_car_obj1, RaceCar)
    creation_of_race_car_object2 = isinstance(race_car_obj2, RaceCar)
    result = race_car_obj1 == race_car_obj2

    # Assert
    assert creation_of_race_car_object1 is True
    assert creation_of_race_car_object2 is True
    assert result is False

########### Testing the class Atrribute values Formats  ###########

def test_race_car_object_color_when_color_type_is_invalid_raises_exception():
    """test that exception is raised for invalid color format"""
    # Arrange
    from  race_car import RaceCar
    color = 1
    max_speed = 30
    acceleration = 10
    tyre_friction = 3

    # Act
    with pytest.raises(Exception) as e:
        assert RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)

    # Assert
    assert str(e.value) == "Invalid value for color"

## Testing Exceptions of Atrribute values if not Positive type and Non-Zero ##

@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [
        (-1, 10, 3), (0, 30, 10), ('1', 30, 20)])
def test_race_car_object_max_speed_when_max_speed_value_is_invalid_raises_exception(max_speed, acceleration, tyre_friction):
    # Arrange
    color = 'Red'

    # Act
    with pytest.raises(Exception) as e:
        assert RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)

    # Assert
    assert str(e.value) == 'Invalid value for max_speed'

@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [
        (210, '10', 3), (100, 0, 10), (180, -30, 20)])
def test_race_car_object_acceleration_when_acceleration_value_is_invalid_raises_exception(max_speed, acceleration, tyre_friction):
    # Arrange
    color = 'Red'

    # Act
    with pytest.raises(Exception) as e:
        assert RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)

    # Assert
    assert str(e.value) == 'Invalid value for acceleration'

@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [
        (210, 30, '10'), (100, 20, -1), (180, 40, 0)])
def test_race_car_object_tyre_friction_when_tyre_friction_value_is_invalid_raises_exception(max_speed, acceleration, tyre_friction):
    # Arrange
    color = 'Red'

    # Act
    with pytest.raises(Exception) as e:
        assert RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)

    # Assert
    assert str(e.value) == 'Invalid value for tyre_friction'

########### ******** Multiple Testings ******** ###########

def test_race_car_object_when_engine_is_started_returns_true(race_car):
    # Arrange
    race_car.start_engine()

    # Act
    car_engine_start = race_car.is_engine_started

    # Assert
    assert car_engine_start is True

def test_race_car_object_when_engine_is_started_twice_returns_true(race_car):
    # Arrange
    race_car.start_engine()
    race_car.start_engine()

    # Act
    car_engine_start = race_car.is_engine_started

    # Assert
    assert car_engine_start is True

def test_race_car_object_when_engine_is_stop_returns_false(race_car):
    # Arrange
    race_car.stop_engine()

    # Act
    car_engine_stop = race_car.is_engine_started

    # Assert
    assert car_engine_stop is False

def test_race_car_object_when_engine_is_stop_twice_returns_false(race_car):
    # Arrange
    race_car.stop_engine()
    race_car.stop_engine()

    # Act
    car_engine_stop = race_car.is_engine_started

    # Assert
    assert car_engine_stop is False

def test_race_car_object_accelerate_when_engine_is_started_returns_current_speed(race_car):
    # Arrange
    race_car.start_engine()
    current_speed = 40

    # Act
    race_car.accelerate()

    # Assert
    assert race_car.current_speed == current_speed

def test_race_car_object_accelerate_when_race_car_object_current_speed_is_equal_to_race_car_object_max_speed_limit_returns_max_speed(race_car):
    # Arrange
    race_car.start_engine()
    max_speed = 200
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()

    # Act
    race_car.accelerate()

    # Assert
    assert race_car.current_speed == max_speed

# ***** New  capsys terminology ******* #


def test_race_car_object_accelerate_when_race_car_engine_is_stop_returns_start_the_engine_to_accelerate(capsys, race_car):
    # Act
    race_car.accelerate()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == 'Start the engine to accelerate\n'

def test_race_car_object_sound_horn_when_engine_is_started_returns_Beep_Beep(capsys, race_car):
    # Arrange
    race_car.start_engine()

    # Act
    race_car.sound_horn()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == 'Peep Peep\nBeep Beep\n'

def test_race_car_object_sound_horn_when_engine_is_stop_returns_start_the_engine_to_sound_horn(capsys, race_car):
    # Act
    race_car.sound_horn()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == 'Start the engine to sound_horn\n'


######## *********** Testing Encapusulation  ***********  ########

def test_encapsulation_of_race_car_object_color(race_car):
    # Act
    with pytest.raises(Exception) as e:
        race_car.color = 'Black'

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_race_car_object_acceleration(race_car):
    # Act
    with pytest.raises(Exception) as e:
        race_car.acceleration = 20

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_race_car_object_max_speed(race_car):
    # Act
    with pytest.raises(Exception) as e:
        race_car.max_speed = 400

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_race_car_object_tyre_friction(race_car):
    # Act
    with pytest.raises(Exception) as e:
        race_car.tyre_friction = 40

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_race_car_object_is_engine_started(race_car):
    # Act
    with pytest.raises(Exception) as e:
        race_car.is_engine_started = True

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_race_car_object_current_speed(race_car):
    # Act
    with pytest.raises(Exception) as e:
        race_car.current_speed = 300

    # Assert
    assert str(e.value) == "can't set attribute"

def test_encapsulation_of_race_car_object_nitro(race_car):
    # Act
    with pytest.raises(Exception) as e:
        race_car.nitro = 100

    # Assert
    assert str(e.value) == "can't set attribute"

#-------------------------------------------------------#

@pytest.mark.parametrize(
    "color,  max_speed, acceleration, tyre_friction, current_speed", [
        ('Red', 1, 1, 1, 1), ('Blue', 150, 30, 10, 20),
        ('Black', 200, 40, 10, 30)])
def test_race_car_object_accelerate_when_race_car_object_current_speed_is_more_than_race_car_object_max_speed_limit_and_nitro_is_zero_returns_max_speed(color, max_speed, acceleration, tyre_friction, current_speed):
    # Arrange
    race_car = RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()

    # Act
    race_car.accelerate()

    # Asset
    assert race_car.current_speed == max_speed

def test_race_car_object_current_speed_when_race_car_object_is_in_idle_postion_intially_and_nitro_is_zero_returns_zero():
    # Arrange
    race_car = RaceCar(color='Red', max_speed=180, acceleration=45,
                       tyre_friction=4)

    # Act
    race_car_idle_initial_speed = race_car.current_speed

    # Act
    assert race_car_idle_initial_speed == 0

def test_race_car_object_current_speed_when_race_car_object_engine_is_stopped_from_motion_and_nitro_is_zero_returns_current_speed():
    # Arrange
    race_car = RaceCar(color='Red', max_speed=180, acceleration=45,
                       tyre_friction=4)
    race_car.start_engine()
    current_speed = 135
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()

    # Act
    race_car.stop_engine()

    # Assert
    assert race_car.current_speed == current_speed

def test_apply_brakes_when_race_car_object_is_in_motion_returns_current_speed(race_car):
    # Arrange
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    current_speed = 70

    # Act
    race_car.apply_brakes()

    # Assert
    assert race_car.current_speed == current_speed

@pytest.mark.parametrize(
    "color,max_speed, acceleration, tyre_friction, current_speed", [
        ('Red', 200, 50, 20, 30), ('Blue', 150, 25, 25, 0)])
def test_apply_breaks_when_race_car_object_current_speed_is_more_than_or_equal_to_race_car_object_tyre_friction_returns_current_speed(color, max_speed, acceleration, tyre_friction, current_speed):
    # Arrange
    race_car = RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()

    # Act
    race_car.apply_brakes()

    # Assert
    assert race_car.current_speed == current_speed

def test_apply_breaks_when_race_car_object_current_speed_is_less_than_race_car_object_tyre_friction_returns_zero():
    # Arrange
    race_car = RaceCar(color='Red', max_speed=200, acceleration=40,
                       tyre_friction=15)
    race_car.start_engine()
    race_car.accelerate()
    current_speed_when_less_than_tyre_friction = 0
    race_car.apply_brakes()
    race_car.apply_brakes()

    # Act
    race_car.apply_brakes()

    # Assert
    assert race_car.current_speed == current_speed_when_less_than_tyre_friction

def test_apply_breaks_when_race_car_object_current_speed_is_equal_to_race_car_object_tyre_friction_returns_current_speed():
    # Arrange
    race_car = RaceCar(color='Red', max_speed=200, acceleration=40,
                       tyre_friction=10)
    race_car.start_engine()
    race_car.accelerate()
    current_speed = 10
    race_car.apply_brakes()
    race_car.apply_brakes()

    # Act
    race_car.apply_brakes()

    # Assert
    assert race_car.current_speed == current_speed

@pytest.mark.parametrize(
    "color,max_speed, acceleration, tyre_friction, current_speed, nitro_value",
    [('Red', 200, 60, 10, 110, 10), ('Blue', 150, 55, 25, 85, 10),
     ('Black', 21, 5, 5, 5, 0), ('Green', 100, 20, 10, 30, 0)])
def test_nitro_of_race_car_when_race_car_apply_breaks_after_accelerating_half_more_than_max_speed_returns_current_speed(color, max_speed, acceleration, tyre_friction, current_speed, nitro_value):
    # Arrange
    race_car = RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.apply_brakes()

    # Act
    nitro = race_car._nitro

    # Assert
    assert nitro == nitro_value
    assert race_car.current_speed == current_speed

@pytest.mark.parametrize(
    "color,max_speed, acceleration, tyre_friction, current_speed, nitro_value",
    [('Red', 200, 60, 10, 188, 0), ('Blue', 155, 55, 25, 155, 0)])
def test_nitro_and_current_speed_of_race_car_when_race_car_apply_breaks_after_accelerating_half_more_than_max_speed_and_then_accelerate_returns_current_speed(color, max_speed, acceleration, tyre_friction, current_speed, nitro_value):
    # Arrange
    race_car = RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.apply_brakes()
    race_car.accelerate()

    # Act
    nitro = race_car._nitro

    # Assert
    assert nitro == nitro_value
    assert race_car.current_speed == current_speed
