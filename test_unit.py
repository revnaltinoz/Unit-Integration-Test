import unittest
from insurance_calculator import calculate_premium

class TestPremiumCalculator(unittest.TestCase):
    
    # Test Case 1: <25 Age AND Has Accident History
    def test_under_25_with_accident(self):
        age = 23
        has_accident_history = True
        
        # Expected Calculation: (1000 + 500) * 1.2 = 1800.0
        expected_premium = 1800.0 

        actual_premium = calculate_premium(age, has_accident_history)

        # Assert
        self.assertEqual(actual_premium, expected_premium, "Premium calculation for <25 with accident is incorrect.")

    # Test Case 2: >=25 Age AND Has Accident History
    def test_over_25_with_accident(self):
        age = 30
        has_accident_history = True
        
        # Expected Calculation: 1000 * 1.2 = 1200.0
        expected_premium = 1200.0 

        actual_premium = calculate_premium(age, has_accident_history)

        # Assert
        self.assertEqual(actual_premium, expected_premium, "Premium calculation for >=25 with accident is incorrect.")

    # Test Case 3: <25 Age AND NO Accident History
    def test_under_25_without_accident(self):
        age = 22
        has_accident_history = False
        
        # Expected Calculation: 1000 + 500 = 1500.0
        expected_premium = 1500.0 

        actual_premium = calculate_premium(age, has_accident_history)

        # Assert
        self.assertEqual(actual_premium, expected_premium, "Premium calculation for <25 without accident is incorrect.")

    # Test Case 4: >=25 Age AND NO Accident History
    def test_over_25_without_accident(self):
        age = 30
        has_accident_history = False
        
        # Expected Calculation: 1000.0 
        expected_premium = 1000.0

        actual_premium = calculate_premium(age, has_accident_history)

        # Assert
        self.assertEqual(actual_premium, expected_premium, "Premium calculation for >=25 without accident is incorrect.")

    # Test 5: Testing the Boundary Condition 
    def test_exact_25_border_case(self):
        age = 25
        has_accident_history = False
        
        # Expected Calculation: 1000.0 (No surcharge)
        expected_premium = 1000.0 

        actual_premium = calculate_premium(age, has_accident_history)

        # Assert
        self.assertEqual(actual_premium, expected_premium, "The 25-year boundary test failed (age surcharge applied incorrectly).")


# pytest test_unit.py
