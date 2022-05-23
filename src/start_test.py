from start import soma, sub
import pytest


def test_soma():
    """Testing soma."""
    result = soma(3, 5)
    assert result == 8


def test_sub():
    """Testing sub."""
    result = sub(5, 2)
    assert result == 3


def test_div():
    """Testing div."""
    pytest.skip("ToDo")


def test_mul():
    """Testing mul."""
    pytest.skip("ToDo")
