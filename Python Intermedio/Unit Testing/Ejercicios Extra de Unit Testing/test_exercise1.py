import pytest

from exercise1 import NumberOperations


def test_positive_numbers():
    # Arrange
    operations = NumberOperations([2, 4, 6])

    # Act
    total = operations.sum_values()
    average = operations.average_values()
    product = operations.multiply_values()

    # Assert
    assert total == 12
    assert average == 4
    assert product == 48


def test_negative_numbers():
    # Arrange
    operations = NumberOperations([-2, -4, -6])

    # Act
    total = operations.sum_values()
    average = operations.average_values()
    product = operations.multiply_values()

    # Assert
    assert total == -12
    assert average == -4
    assert product == -48


def test_with_zeros():
    # Arrange
    operations = NumberOperations([0, 5, 10])

    # Act
    total = operations.sum_values()
    average = operations.average_values()
    product = operations.multiply_values()

    # Assert
    assert total == 15
    assert average == 5
    assert product == 0


def test_with_positive_and_negative_numbers():
    # Arrange
    operations = NumberOperations([3, -2, 5, -1])

    # Act
    total = operations.sum_values()
    average = operations.average_values()
    product = operations.multiply_values()

    # Assert
    assert total == 5
    assert average == 1.25
    assert product == 30
