def test_race_car_object_sound_horn_when_engine_is_started_returns_peep_peep_and_beep_beep(capsys, race_car):
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
