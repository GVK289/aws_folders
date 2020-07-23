def test_car_object_sound_horn_when_engine_is_started_returns_beep_beep(capsys, car):
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
