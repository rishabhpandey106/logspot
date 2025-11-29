# LogSpot

LogSpot is a lightweight, reusable Flask extension that adds a `/logs` route to your application, allowing you to view, filter, search, and download logs directly from the browser. It also provides a simple logging interface attached to your Flask app instance.

## Features

- **Instant Log Viewer**: Access your application logs at `/logs`.
- **Filtering**: Filter logs by severity level (INFO, DEBUG, WARN, ERROR, CRITICAL).
- **Search**: Search for specific keywords in your logs.
- **Pagination/Limit**: Control the number of log lines displayed.
- **Download**: Download logs as a file for offline analysis.
- **Simple API**: Easy-to-use logging methods attached directly to your Flask `app` object.

## Installation

You can install LogSpot using pip:

```bash
pip install logspot
```

Or install directly from the source:

```bash
pip install git+https://github.com/rishabhpandey106/logspot.git
```

## Quick Start

Here's how to integrate LogSpot into your Flask application:

```python
from flask import Flask
from central_logs_flask import setup_logs

app = Flask(__name__)

# Initialize LogSpot
# This registers the /logs blueprint and attaches logging methods to 'app'
logger = setup_logs(app, service="my_service")

@app.route("/")
def index():
    # Use the attached logging methods
    logger.info("Index page accessed")
    return "Hello, World!"

@app.route("/error")
def trigger_error():
    logger.error("Something went wrong!")
    return "Error logged", 500

if __name__ == "__main__":
    app.run(debug=True)
```

Now, run your app and visit `http://localhost:5000/logs` to see your logs!

## Usage

### Logging Methods

Once initialized, LogSpot attaches the following methods to your Flask app instance:

- `logger.info(message)`
- `logger.debug(message)`
- `logger.warn(message)`
- `logger.error(message)`
- `logger.critical(message)`

### The `/logs` Endpoint

The `/logs` route supports several query parameters to help you find what you need:

| Parameter  | Description                                      | Default | Example                          |
| :---       | :---                                             | :---    | :---                             |
| `limit`    | Number of recent log lines to show               | `200`   | `/logs?limit=50`                 |
| `level`    | Filter by log level (INFO, ERROR, etc.)          | `None`  | `/logs?level=ERROR`              |
| `search`   | Case-insensitive search for a string             | `None`  | `/logs?search=database`          |
| `download` | Set to `true` to download logs as a `.log` file  | `false` | `/logs?download=true`            |

**Examples:**

- **Show last 50 error logs:**
  `GET /logs?limit=50&level=ERROR`

- **Search for "connection failed":**
  `GET /logs?search=connection%20failed`

- **Download all logs:**
  `GET /logs?download=true&limit=0` (Use `limit=0` or a very large number to get all logs, though default is 200)

## License

This project is licensed under the MIT License.
