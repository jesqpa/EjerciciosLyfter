import pytest

import functions_execise6


def test_counts_upper_and_lower_case_letters_with_mixed_text():
    # Arrange
    text = "Hola"

    # Act
    result = functions_execise6.get_upper_and_lower_case_letters(text)

    # Assert
    assert result == {"uppercase": 1, "lowercase": 3}


def test_counts_upper_and_lower_case_letters_with_all_uppercase():
    # Arrange
    text = "PYTHON"

    # Act
    result = functions_execise6.get_upper_and_lower_case_letters(text)

    # Assert
    assert result == {"uppercase": 6, "lowercase": 0}


def test_raises_error_with_non_string_input():
    # Arrange
    invalid_input = 123

    # Act & Assert
    with pytest.raises(TypeError):
        functions_execise6.get_upper_and_lower_case_letters(invalid_input)
