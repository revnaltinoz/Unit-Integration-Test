
# Unit tests: test single functions in isolation
from app.math_utils import add, multiply

def test_add_basic():
    assert add(2, 3) == 5

def test_multiply_basic():
    assert multiply(4, 5) == 20

def test_add_edge_negative_numbers():
    assert add(-2, -3) == -5

def test_multiply_edge_zero():
    assert multiply(42, 0) == 0
