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
