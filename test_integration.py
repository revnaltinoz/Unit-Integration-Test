import unittest
from insurance_calculator import calculate_final_quote, calculate_premium

class TestPremiumIntegration(unittest.TestCase):

    # Test 1: Happy Path for Customer 1
    def test_integration_customer_1_full_flow(self):
        customer_id = 1
        
        # Expected Calculation:
        # Premium: 1000.0 (>=25, No Accident)
        # Final Quote: 1000.0 * (1 - (0.85 * 0.1)) = 915.0
        expected_quote = 915.0
        
        actual_quote = calculate_final_quote(customer_id)
        
        # The test passes if the data is fetched correctly and the calculation is applied correctly
        self.assertEqual(actual_quote, expected_quote, "Full quote calculation for Customer 1 failed integration.")

    # Test 2: Error Handling (Checking data fetch failure)
    def test_integration_customer_not_found(self):
        #non-existent ID
        customer_id = 99
        
        # Check if the system correctly raises the expected error
        with self.assertRaises(ValueError) as context:
            calculate_final_quote(customer_id)
            
        self.assertTrue(f"Customer {customer_id} not found." in str(context.exception))

    # Test 3: Complex Flow (Under 25 + Accident)
    def test_integration_customer_2_under_25_high_risk(self):
        """Tests the full flow for a customer with max surcharges."""
        customer_id = 2
        
        # Expected Calculation:
        # Premium: (1000 + 500) * 1.2 = 1800.0
        # Final Quote: 1800.0 * (1 - (0.60 * 0.1)) = 1692.0
        expected_quote = 1692.0
        
        actual_quote = calculate_final_quote(customer_id)
        
        self.assertEqual(actual_quote, expected_quote, "Full quote calculation for Customer 2 (high risk) failed integration.")

    # Test 4: Data Contract Failure
    def test_integration_missing_key_in_data(self):
        """Checks system when data source returns incomplete data """
        # Customer 3 is intentionally set up to miss 'driving_score'
        customer_id = 3
        
        # The test should explicitly look for a KeyError 
        # This proves the system correctly fails when the contract is broken.
        with self.assertRaises(KeyError) as context:
            calculate_final_quote(customer_id)
            
        self.assertTrue("driving_score" in str(context.exception), "Integration did not fail on missing data key.")

# ... (if __name__ == '__main__': unittest.main() can be added here)

# pytest test_integration.py