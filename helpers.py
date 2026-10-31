import os
import shutil
from pathlib import Path
from typing import List, Union


def sanitize_path(path_input: Union[str, Path]) -> Path:
    """Convert string path or Path to a resolved Path object."""
    return Path(path_input).expanduser().resolve()


def clean_empty_directories(root_dir: Union[str, Path]) -> List[Path]:
    """Remove empty directories recursively starting from root_dir."""
    target = sanitize_path(root_dir)
    removed_dirs: List[Path] = []

    if not target.exists() or not target.is_dir():
        return removed_dirs

    # Walk bottom-up to ensure nested empty dirs are handled
    for dirpath, _, _ in os.walk(target, topdown=False):
        current = Path(dirpath)
        if current.is_dir() and not os.listdir(current) and current != target:
            current.rmdir()
            removed_dirs.append(current)

    return removed_dirs


def reorganize_files_by_extension(source_dir: Union[str, Path]) -> int:
    """Group files into subdirectories based on file extension."""
    target = sanitize_path(source_dir)
    if not target.exists() or not target.is_dir():
        return 0

    moved_count = 0
    for item in target.iterdir():
        if item.is_file() and not item.name.startswith('.'):
            ext = item.suffix.lower().lstrip('.') or 'no_extension'
            dest_dir = target / ext
            dest_dir.mkdir(exist_ok=True)

            shutil.move(str(item), str(dest_dir / item.name))
            moved_count += 1

    return moved_count
