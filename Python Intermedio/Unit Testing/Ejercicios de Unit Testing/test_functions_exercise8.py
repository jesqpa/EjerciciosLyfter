import pytest

import functions_execise8


def test_extracts_prime_numbers_from_mixed_values():
    # Arrange
    numbers = [2, 3, 4, 5, 6]

    # Act
    result = functions_execise8.extract_prime_numbers(numbers)

    # Assert
    assert result == [2, 3, 5]


def test_extracts_prime_numbers_from_only_primes():
    # Arrange
    numbers = [7, 11, 13]

    # Act
    result = functions_execise8.extract_prime_numbers(numbers)

    # Assert
    assert result == [7, 11, 13]


def test_extracts_prime_numbers_from_non_primes():
    # Arrange
    numbers = [1, 4, 8, 9]

    # Act
    result = functions_execise8.extract_prime_numbers(numbers)

    # Assert
    assert result == []
