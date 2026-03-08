import pytest
from app import calculate_average, find_highest, find_lowest, is_pass


def test_calculate_average():
    marks = [60, 70, 80]
    assert calculate_average(marks) == 70


def test_highest_mark():
    marks = [45, 88, 67, 92]
    assert find_highest(marks) == 92


def test_lowest_mark():
    marks = [45, 88, 67, 92]
    assert find_lowest(marks) == 45


def test_student_pass():
    avg = 55
    assert is_pass(avg) == True


def test_student_fail():
    avg = 25
    assert is_pass(avg) == False