# automation-tool-79

`automation-tool-79` is a modular Python-based utility designed to streamline repetitive filesystem and network tasks. It provides a lightweight command-line interface to orchestrate complex workflows with minimal configuration.

## Features

*   **Task Scheduling:** Execute custom scripts at precise intervals using a non-blocking internal scheduler.
*   **Log Aggregation:** Automatically captures, rotates, and formats console outputs into structured JSON log files.
*   **Environment Sync:** Synchronize local directory structures with remote storage endpoints via robust API wrappers.
*   **Plugin Architecture:** Extend core functionality by dropping custom `.py` modules into the `plugins/` directory.

## Installation

Ensure you have Python 3.9+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/automation-tool-79.git
cd automation-tool-79
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

The tool operates via a YAML configuration file. Define your tasks in `config.yaml` and execute the runner:

```bash
# Run a specific task defined in your config
python main.py --task sync-assets --verbose

# Run all scheduled tasks in background mode
python main.py --daemonize
```

### Configuration Example (`config.yaml`)
```yaml
tasks:
  sync-assets:
    source: "./data"
    target: "s3://bucket-name/uploads"
    interval: 3600
```

## Contributing
Contributions are welcome. Please fork the repository and submit a pull request with unit tests covering your changes.

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.