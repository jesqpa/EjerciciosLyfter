import pytest

import functions_execise3


def test_sets_name_with_one_value():
    # Arrange
    new_name = "Ana"

    # Act
    result = functions_execise3.set_name(new_name)

    # Assert
    assert result == "Ana"
    assert functions_execise3.name == "Ana"


def test_sets_name_with_longer_value():
    # Arrange
    new_name = "Luis Alberto Morales Perez"

    # Act
    result = functions_execise3.set_name(new_name)

    # Assert
    assert result == "Luis Alberto Morales Perez"
    assert functions_execise3.name == "Luis Alberto Morales Perez"


def test_sets_name_with_empty_value():
    # Arrange
    new_name = ""

    # Act & Assert
    with pytest.raises(ValueError):
        functions_execise3.set_name(new_name)
