import os
from pathlib import Path

# Project path definitions
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"

# Application configuration defaults
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
CHUNK_SIZE = 1024 * 1024

# Environment variable keys
ENV_API_KEY = "AUTOMATION_API_KEY"
ENV_LOG_LEVEL = "AUTOMATION_LOG_LEVEL"

# Supported file extensions
ALLOWED_EXTENSIONS = {'.json', '.csv', '.yaml', '.txt'}

# Operation status strings
STATUS_SUCCESS = "SUCCESS"
STATUS_FAILED = "FAILED"
STATUS_PENDING = "PENDING"

# Ensure base directories exist on load
for directory in [LOG_DIR, DATA_DIR]:
    directory.mkdir(exist_ok=True)
