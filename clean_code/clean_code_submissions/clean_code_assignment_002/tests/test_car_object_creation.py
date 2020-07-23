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
