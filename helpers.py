import re


def validate_input(data):
    """
    Validates input structure for automation tasks.
    Ensures target and action are present.
    """
    if not isinstance(data, dict):
        return False, "Input must be a dictionary"

    target = data.get("target")
    action = data.get("action")

    if not target or not isinstance(target, str):
        return False, "Invalid or missing target string"

    if not action or action not in ["run", "stop", "restart"]:
        return False, "Invalid action type"

    return True, None


def process_main_loop(queue):
    """
    Main processing loop with integrated validation.
    """
    for item in queue:
        is_valid, error = validate_input(item)
        if not is_valid:
            print(f"Skipping invalid task: {error}")
            continue

        # Execute core business logic here
        target = item['target']
        print(f"Processing task: {item['action']} on {target}")


def sanitize_path(path):
    """
    Sanitizes paths to prevent directory traversal.
    """
    if not path or ".." in path:
        return ""
    return re.sub(r'[^a-zA-Z0-9_/.-]', '', path)