
from .math_utils import add, multiply

def calculate_expression(a, b, c):
    """Return (a + b) * c."""
    return multiply(add(a, b), c)
