# Contributing to PCB Fault Detection System

Thank you for your interest in contributing!

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/pcb-fault-detection.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Run tests: `pytest`
6. Commit your changes: `git commit -m "Add your feature"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Create a Pull Request

## Development Setup (Windows)

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/ -v

# Check code style
black src/ tests/
flake8 src/ tests/
mypy src/
```

## Code Style

- Follow PEP 8 guidelines
- Use Black for code formatting
- Maximum line length: 100 characters
- Use type hints for function arguments and return values
- Write docstrings for all public functions and classes

## Testing

- Write unit tests for all new features
- Maintain test coverage above 80%
- Use pytest for testing

## Commit Messages

Follow conventional commits format:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Example: `feat: add support for X-ray inspection`

## Questions?

Feel free to open a GitHub Discussion or contact the maintainers.
