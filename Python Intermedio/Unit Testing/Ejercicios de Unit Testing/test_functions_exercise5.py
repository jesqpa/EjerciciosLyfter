import pytest

import functions_execise5


def test_inverts_string_with_letters():
    # Arrange
    text = "hola"

    # Act
    result = functions_execise5.invert_string(text)

    # Assert
    assert result == "aloh"


def test_inverts_string_with_capital_letters():
    # Arrange
    text = "Python"

    # Act
    result = functions_execise5.invert_string(text)

    # Assert
    assert result == "nohtyP"


def test_raises_error_with_non_string_input():
    # Arrange
    invalid_input = 123

    # Act & Assert
    with pytest.raises(TypeError):
        functions_execise5.invert_string(invalid_input)
