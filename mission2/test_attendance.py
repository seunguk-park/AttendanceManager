import pytest
from unittest.mock import call, MagicMock, patch
from attendance import AttendanceManager


def test_input_file_with_normal_case():
    # Arrange
    manager = AttendanceManager()

    # Act
    manager.input_file("attendance_weekday_500.txt")

    # Assert
    assert manager.id_count == 19

def test_input_file_with_abnormal_case():
    # Arrange
    manager = AttendanceManager()

    # Act
    manager.input_file("attendance_weekday_0.txt")

    # Assert
    assert manager.id_count == 0

def test_add_bonus_point():
    # Arrange
    manager = AttendanceManager()

    # Act
    manager.input_file("attendance_weekday_500.txt")
    manager.add_bonus_point()

    # Assert
    assert manager.total_points[manager.player_id_list["Umar"]] == 48
    assert manager.total_points[manager.player_id_list["Hannah"]] == 127
    assert manager.total_points[manager.player_id_list["Bob"]] == 8

def test_update_grade():
    # Arrange
    manager = AttendanceManager()

    # Act
    manager.input_file("attendance_weekday_500.txt")
    manager.add_bonus_point()
    manager.update_grade()

    # Assert
    assert manager.grade[manager.player_id_list["Umar"]] == 2
    assert manager.grade[manager.player_id_list["Hannah"]] == 1
    assert manager.grade[manager.player_id_list["Bob"]] == 0

def test_print_points_and_grade(mocker):
    # Arrange
    mock_print = mocker.patch('builtins.print')
    manager = AttendanceManager()

    # Act
    manager.input_file("attendance_weekday_500.txt")
    manager.add_bonus_point()
    manager.update_grade()
    manager.print_points_and_grade()

    # Assert
    mock_print.assert_any_call("GOLD")
    mock_print.assert_any_call("SILVER")
    mock_print.assert_any_call("NORMAL")

def test_print_removed_player(mocker):
    # Arrange
    mock_print = mocker.patch('builtins.print')
    manager = AttendanceManager()

    # Act
    manager.input_file("attendance_weekday_500.txt")
    manager.add_bonus_point()
    manager.update_grade()
    manager.print_removed_player()

    # Assert
    mock_print.assert_any_call("Bob")
    mock_print.assert_any_call("Zane")
