def calculate_premium(age: int, has_accident_history: bool) -> float:
    """
    Calculates the base insurance premium based on age and accident history.
    """
    BASE_PREMIUM = 1000.0
    AGE_SURCHARGE = 500.0
    ACCIDENT_MULTIPLIER = 1.2

    premium = BASE_PREMIUM

    if age < 25:
        premium += AGE_SURCHARGE

    if has_accident_history:
        premium *= ACCIDENT_MULTIPLIER

    return premium


def get_customer_data(customer_id: int) -> dict:
    """Simulates fetching customer data from a database or API."""
    if customer_id == 1:
        return {"age": 28, "accident_history": False, "driving_score": 0.85}
    elif customer_id == 2:
        return {"age": 20, "accident_history": True, "driving_score": 0.60}
    elif customer_id == 3:
        # Simulates a data source error where a critical key is missing
        return {"age": 40, "accident_history": False} 
    else:
        raise ValueError(f"Customer {customer_id} not found.")

def calculate_final_quote(customer_id: int) -> float:
    """Integrates data loading and premium calculation."""
    data = get_customer_data(customer_id)
    
    # Premium Calculation
    base_premium = calculate_premium(data["age"], data["accident_history"])
    
    # ML/Score Adjustment
    final_quote = base_premium * (1 - (data["driving_score"] * 0.1)) 
    
    return round(final_quote, 2)