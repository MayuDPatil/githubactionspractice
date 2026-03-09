# Python Project

A simple Python project for practicing GitHub Actions.

## Project Structure

```
├── main.py              # Main application module
├── test_main.py         # Unit tests
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

```bash
python main.py
```

### Running Tests

```bash
pytest test_main.py
```

Or with coverage:

```bash
pytest --cov=. test_main.py
```

## Code Quality

Format code with Black:

```bash
black main.py test_main.py
```

Check style with Flake8:

```bash
flake8 main.py test_main.py
```

## License

MIT
