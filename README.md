![Python application](https://github.com/Robbe7730/RSSReader/workflows/Python%20application/badge.svg)

# RSS reader that is yet to be named

You can find the OpenAPI 3.0 specification under `docs/`

## Dev Setup

### 1. Create a `config.py`

```python
"""
Configuration for the Flask app
"""

# Define the application directory
import os

# Statement for enabling the development environment
DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
```

### 2. Setup your virtual environment

```bash
virtualenv -p python3 venv
. venv/bin/activate
```

### 3. Run run.py

```bash
python run.py
```

## Testing

Test can be run with `tox`. Tests are currently ran on python 3.8 (see tox.ini)
