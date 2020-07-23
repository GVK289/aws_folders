from truck import Truck

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
