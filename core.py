import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-79')

class AutomationCore:
    def __init__(self, config_path):
        self.config_path = config_path

    def execute_task(self, data: dict):
        """Process automation tasks with robust error boundary."""
        try:
            if not data or not isinstance(data, dict):
                raise ValueError("Invalid input data format")
            
            if not os.path.exists(self.config_path):
                raise FileNotFoundError(f"Config missing at {self.config_path}")

            # Simulate core operational logic
            result = data.get('payload') / data.get('divisor', 1)
            return {"status": "success", "value": result}

        except ZeroDivisionError:
            logger.error("Calculation failure: division by zero")
            return {"status": "error", "message": "invalid divisor"}
        except (ValueError, TypeError) as e:
            logger.warning(f"Input validation error: {e}")
            return {"status": "error", "message": str(e)}
        except Exception as e:
            logger.critical(f"Unexpected system failure: {e}", exc_info=True)
            return {"status": "critical", "message": "internal system failure"}

def run_automation(data):
    engine = AutomationCore('config.yaml')
    return engine.execute_task(data)