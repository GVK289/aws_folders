import pytest
from car import Car
from truck import Truck
from race_car import RaceCar

@pytest.fixture
def car():  # Car Fixture function
    # Arrange
    color = 'Red'
    max_speed = 200
    acceleration = 40
    tyre_friction = 10

    car_obj = Car(color=color, max_speed=max_speed,
                  acceleration=acceleration, tyre_friction=tyre_friction)
    return car_obj

@pytest.fixture
def truck():  # Truck Fixture function
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

@pytest.fixture
def race_car():  # RaceCar Fixture function
    # Arrange
    color = 'Red'
    max_speed = 200
    acceleration = 40
    tyre_friction = 10

    race_car_obj = RaceCar(color=color, max_speed=max_speed,
                           acceleration=acceleration,
                           tyre_friction=tyre_friction)
    return race_car_obj
