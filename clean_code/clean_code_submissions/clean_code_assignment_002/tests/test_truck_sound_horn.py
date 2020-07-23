def test_truck_object_sound_horn_when_engine_is_started_returns_honk_honk(capsys, truck):
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
