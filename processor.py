import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles bulk processing and cleanup of task records."""

    def __init__(self, batch_size: int = 100):
        self.batch_size = batch_size

    def filter_active_tasks(self, tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Removes inactive or malformed task entries."""
        return [t for t in tasks if t.get('status') == 'active' and 'id' in t]

    def reorganize_payloads(self, tasks: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Groups tasks by priority category."""
        organized = {'high': [], 'normal': []}
        for task in tasks:
            priority = task.get('priority', 'normal')
            if priority in organized:
                organized[priority].append(task)
            else:
                organized['normal'].append(task)
        return organized

    def process_batch(self, raw_data: List[Dict[str, Any]]) -> None:
        """Executes full cleanup and organization workflow."""
        if not raw_data:
            return

        valid_tasks = self.filter_active_tasks(raw_data)
        result = self.reorganize_payloads(valid_tasks)
        
        logger.info(f"Processed {len(valid_tasks)} tasks into {len(result)} categories")

def run_cleanup(data: List[Dict[str, Any]]):
    processor = DataProcessor()
    processor.process_batch(data)