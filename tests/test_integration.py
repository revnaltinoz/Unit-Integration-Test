
# Integration test: multiple modules working together
# operations.calculate_expression depends on math_utils.add and math_utils.multiply
from app.operations import calculate_expression

def test_calculate_expression_integration():
    # (2 + 3) * 4 = 20 — verifies add() + multiply() together
    assert calculate_expression(2, 3, 4) == 20
