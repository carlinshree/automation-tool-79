import logging

def process_input(user_input):
    """Validate and process individual input string."""
    if not isinstance(user_input, str):
        raise ValueError("input must be a string")
    
    stripped = user_input.strip()
    if not stripped:
        raise ValueError("input cannot be empty or whitespace")
    
    return stripped.upper()

def run_main_loop(data_list):
    """
    Main processing loop with integrated input validation.
    Handles iteration over raw data and processes valid entries.
    """
    processed_results = []
    
    for item in data_list:
        try:
            validated = process_input(item)
            processed_results.append(validated)
            logging.info(f"successfully processed: {validated}")
        except (ValueError, TypeError) as e:
            logging.warning(f"skipping invalid item {item}: {e}")
            continue
            
    return processed_results

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    test_data = ["task1", "", 123, "task2", "  "]
    results = run_main_loop(test_data)
    print(f"Final list: {results}")