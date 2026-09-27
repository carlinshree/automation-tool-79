import os
import shutil
from typing import List, Any, Generator

def sanitize_filename(filename: str) -> str:
    """Removes invalid characters from a filename to make it safe."""
    keep_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.- "
    cleaned = "".join(c for c in filename if c in keep_chars)
    return cleaned.strip()

def safe_delete_file(file_path: str) -> bool:
    """Safely attempts to delete a file, returning True if successful."""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
    except OSError:
        pass
    return False

def chunk_generator(data: List[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    """Yields successive chunks of a list based on chunk size."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    for i in range(0, len(data), chunk_size):
        yield data[i : i + chunk_size]

def clear_directory(directory_path: str) -> bool:
    """Deletes all contents inside a directory without deleting the directory."""
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        return False
    
    success = True
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        try:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
        except OSError:
            success = False
    return success