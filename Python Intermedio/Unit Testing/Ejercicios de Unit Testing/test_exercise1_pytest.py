import pytest

from exercise1 import bubble_sort


def test_works_with_small_list():
    #Arrange
    numbers = [64, 34, 25, 12, 22, 11, 90]
    #Act
    result = bubble_sort(numbers)
    #Assert
    assert result == [11, 12, 22, 25, 34, 64, 90]


def test_works_with_large_list():
    #Arrange
    numbers = list(range(200, 0, -1))
    #Act
    result = bubble_sort(numbers)
    #Assert
    assert result == list(range(1, 201))


def test_works_with_empty_list():
    #Arrange
    numbers = []
    #Act
    result = bubble_sort(numbers)
    #Assert
    assert result == []


def test_fails_with_non_list_parameters():
    #Arrange
    not_a_list = "not a list"
    #Act & Assert
    with pytest.raises((TypeError, AttributeError)):
        bubble_sort(not_a_list)
