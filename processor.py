import os
import shutil
import logging
from datetime import datetime, timedelta
from typing import Dict

logger = logging.getLogger(__name__)


class DataProcessor:
    """Handles workspace data execution, temp cleanup, and output file reorganization."""

    def __init__(self, work_dir: str, retention_days: int = 7):
        self.work_dir = os.path.abspath(work_dir)
        self.retention_days = retention_days
        self._ensure_directories()

    def _ensure_directories(self) -> None:
        """Create required workspace subdirectories if missing."""
        for sub_dir in ["incoming", "processed", "archive", "temp"]:
            path = os.path.join(self.work_dir, sub_dir)
            os.makedirs(path, exist_ok=True)

    def cleanup_temp_files(self) -> int:
        """Remove temporary files older than the retention threshold."""
        temp_dir = os.path.join(self.work_dir, "temp")
        removed_count = 0
        cutoff = datetime.now() - timedelta(days=self.retention_days)

        for root, _, files in os.walk(temp_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                if file_mtime < cutoff:
                    try:
                        os.remove(file_path)
                        removed_count += 1
                    except OSError as err:
                        logger.error(f"Failed to delete {file_path}: {err}")

        return removed_count

    def reorganize_outputs(self, category_map: Dict[str, str]) -> Dict[str, int]:
        """Move processed files into category-specific archive subfolders."""
        processed_dir = os.path.join(self.work_dir, "processed")
        results = {"moved": 0, "errors": 0}

        for file_name in os.listdir(processed_dir):
            source_path = os.path.join(processed_dir, file_name)
            if not os.path.isfile(source_path):
                continue

            ext = os.path.splitext(file_name)[1].lstrip(".").lower()
            target_folder = category_map.get(ext, "misc")
            target_dir = os.path.join(self.work_dir, "archive", target_folder)
            os.makedirs(target_dir, exist_ok=True)

            try:
                shutil.move(source_path, os.path.join(target_dir, file_name))
                results["moved"] += 1
            except (OSError, shutil.Error) as err:
                logger.error(f"Failed to move file {file_name}: {err}")
                results["errors"] += 1

        return results
