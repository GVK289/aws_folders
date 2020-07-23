from race_car import RaceCar

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
