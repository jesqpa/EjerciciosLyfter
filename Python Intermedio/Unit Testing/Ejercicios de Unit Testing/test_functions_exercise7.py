import pytest

import functions_execise7


def test_reorders_words_with_hyphenated_text():
    # Arrange
    text = "python-variable-funcion-computadora-monitor"

    # Act
    result = functions_execise7.reordered_words(text)

    # Assert
    assert result == "computadora-funcion-monitor-python-variable"


def test_reorders_words_with_three_items():
    # Arrange
    text = "b-a-c"

    # Act
    result = functions_execise7.reordered_words(text)

    # Assert
    assert result == "a-b-c"


def test_raises_error_with_non_string_input():
    # Arrange
    invalid_input = 123

    # Act & Assert
    with pytest.raises((TypeError, AttributeError)):
        functions_execise7.reordered_words(invalid_input)
