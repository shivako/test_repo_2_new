# Python Project Skeleton

This is a basic Python project structure that can be used as a starting point for Python applications.

## Project Structure

```
.
├── main.py                 # Entry point for the application
├── my_package/            # Main package directory
│   ├── __init__.py        # Makes my_package a Python package
│   ├── module1.py         # Example module
│   └── module2.py         # Another example module
├── tests/                 # Test directory
│   ├── __init__.py        # Makes tests a Python package
│   └── test_basic.py      # Example test file
├── requirements.txt       # Project dependencies
├── setup.py              # Setup script for the package
└── README.md             # Project documentation
```

## Installation

```bash
# Clone the repository
git clone https://github.com/shivako/test_repo_2_new.git
cd test_repo_2_new

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package in development mode
pip install -e .
```

## Usage

```bash
# Run the main application
python main.py

# Run tests
python -m unittest discover tests
```
