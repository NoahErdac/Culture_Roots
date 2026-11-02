def validate_submission_payload(data: dict) -> tuple[bool, str]:
    required_fields = [
        'name', 
        'food_narrative', 'food_query', 
        'history_narrative', 'history_query',
        'culture_narrative', 'culture_query'
    ]
    
    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            return False, f"Missing or empty required field: {field}"
            
    if len(data['name']) > 100:
        return False, "Country name is too long."
        
    return True, "Valid"