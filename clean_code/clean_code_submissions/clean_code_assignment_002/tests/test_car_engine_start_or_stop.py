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
