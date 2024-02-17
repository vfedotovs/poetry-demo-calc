from poetry_demo_calc.calculator import add, subtract, multiply, divide


def test_add():
    assert add(5, 3) == 8
    assert add(0, 0) == 0
    assert add(-5, 3) == -2


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 0) == 0
    assert subtract(5, -3) == 8


def test_multiply():
    assert multiply(6, 2) == 12
    assert multiply(0, 5) == 0
    assert multiply(-3, -3) == 9


def test_divide():
    assert divide(8, 2) == 4
    assert divide(0, 5) == 0
    assert divide(-6, 2) == -3
    assert divide(10, 0) == "Error: Division by zero"
