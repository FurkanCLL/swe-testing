import pytest
from src.quick_calc.engine import CalculatorEngine


def setup_engine():
    return CalculatorEngine()


def test_addition():
    engine = setup_engine()
    assert engine.add(5, 3) == 8


def test_subtraction():
    engine = setup_engine()
    assert engine.subtract(10, 4) == 6


def test_multiplication():
    engine = setup_engine()
    assert engine.multiply(6, 7) == 42


def test_division():
    engine = setup_engine()
    assert engine.divide(20, 5) == 4


def test_division_by_zero():
    engine = setup_engine()
    with pytest.raises(ZeroDivisionError):
        engine.divide(10, 0)


def test_negative_numbers():
    engine = setup_engine()
    assert engine.add(-5, -3) == -8


def test_decimal_numbers():
    engine = setup_engine()
    assert engine.divide(5.0, 2.0) == 2.5


def test_clear():
    engine = setup_engine()
    assert engine.clear() == 0