import os
import shutil
import logging
from typing import List

logger = logging.getLogger(__name__)

def clean_temp_directories(paths: List[str]) -> None:
    """Removes temporary files and directories to free space."""
    for path in paths:
        if os.path.exists(path):
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
                logger.info(f"Successfully removed: {path}")
            except OSError as e:
                logger.error(f"Failed to delete {path}: {e}")

def organize_project_files(target_dir: str, extensions: List[str]) -> None:
    """Groups files by extension into subdirectories."""
    if not os.path.exists(target_dir):
        return

    for filename in os.listdir(target_dir):
        ext = filename.split('.')[-1].lower()
        if ext in extensions:
            dest_folder = os.path.join(target_dir, ext)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(
                os.path.join(target_dir, filename),
                os.path.join(dest_folder, filename)
            )

def validate_path_safety(path: str) -> bool:
    """Ensures path operations stay within intended scope."""
    return not path.startswith('..') and os.path.isabs(path)