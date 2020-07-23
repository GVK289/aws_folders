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
