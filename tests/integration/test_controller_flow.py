from src.quick_calc.controller import CalculatorController


def test_full_flow_addition():
    c = CalculatorController()
    c.press("5")
    c.press("+")
    c.press("3")
    out = c.press("=")
    assert out == "8"


def test_clear_resets_display():
    c = CalculatorController()
    c.press("9")
    c.press("*")
    c.press("9")
    c.press("=")
    out = c.press("C")
    assert out == "0"