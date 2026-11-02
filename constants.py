import os
from pathlib import Path

# Project path definitions
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"

# Execution constraints
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30

# System default configurations
DEFAULT_ENCODING = "utf-8"
SUPPORTED_EXTENSIONS = {".json", ".csv", ".txt"}

# Environment variable keys
ENV_PREFIX = "AUTO_TOOL"
DB_CONNECTION_STRING = os.getenv(f"{ENV_PREFIX}_DB_URL", "sqlite:///default.db")

# Logging format and levels
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = os.getenv(f"{ENV_PREFIX}_LOG_LEVEL", "INFO")

# Security and validation thresholds
MAX_FILE_SIZE_MB = 10
API_KEY_HEADER = "X-Automation-Key"

def ensure_directories():
    """Initializes file system structure."""
    for directory in [LOG_DIR, DATA_DIR]:
        directory.mkdir(parents=True, exist_ok=True)