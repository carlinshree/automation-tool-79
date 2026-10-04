import os
import shutil
from pathlib import Path
from typing import List, Optional

def clean_temp_directories(base_path: str, patterns: List[str]) -> int:
    """Remove temporary directories matching specified patterns."""
    count = 0
    path = Path(base_path)
    if not path.exists():
        return 0

    for item in path.iterdir():
        if item.is_dir() and any(p in item.name for p in patterns):
            shutil.rmtree(item)
            count += 1
    return count

def organize_files_by_extension(target_dir: str) -> None:
    """Group files into subfolders based on extension."""
    root = Path(target_dir)
    if not root.exists():
        return

    for file in root.iterdir():
        if file.is_file():
            ext = file.suffix[1:].lower() or 'no_extension'
            dest_dir = root / ext
            dest_dir.mkdir(exist_ok=True)
            file.rename(dest_dir / file.name)

def get_directory_size(path: str) -> int:
    """Calculate total size of directory in bytes."""
    root = Path(path)
    return sum(f.stat().st_size for f in root.glob('**/*') if f.is_file())