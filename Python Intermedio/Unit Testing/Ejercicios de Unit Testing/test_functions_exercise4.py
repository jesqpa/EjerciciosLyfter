import pytest

import functions_execise4


def test_sums_numbers_with_positive_values():
    # Arrange
    numbers = [1, 2, 3]

    # Act
    result = functions_execise4.sum_numbers_list(numbers)

    # Assert
    assert result == 6


def test_sums_numbers_with_mixed_values():
    # Arrange
    numbers = [10, -5, 3]

    # Act
    result = functions_execise4.sum_numbers_list(numbers)

    # Assert
    assert result == 8


def test_raises_error_with_non_iterable_input():
    # Arrange
    invalid_input = 123

    # Act & Assert
    with pytest.raises(TypeError):
        functions_execise4.sum_numbers_list(invalid_input)
