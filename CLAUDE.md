# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

fx-lib is Frank Xu's personal Python utility library providing common functionality for logging, email, datetime manipulation, string operations, mathematical functions, and list utilities. It's designed as a lightweight collection of helper modules to avoid reimplementing common patterns.

## Development Commands

### Testing
```bash
# Run tests quickly with default Python
python setup.py test

# Run tests with unittest directly
python -m unittest tests.test_fx_lib

# Run all tests across Python versions
tox

# Run specific test file
python -m unittest tests.test_zoho_email
```

### Code Quality
```bash
# Lint code with flake8
flake8 fx_lib tests

# Check code coverage
coverage run --source fx_lib setup.py test
coverage report -m
coverage html
```

### Building and Distribution
```bash
# Clean build artifacts
make clean

# Build distribution packages
make dist
# Equivalent to:
# python3 setup.py sdist
# python3 setup.py bdist_wheel

# Install locally for development
python3 setup.py develop

# Install from source
make install
```

### Documentation
```bash
# Generate Sphinx documentation
make docs

# Serve docs with auto-reload
make servedocs
```

### Version Management
```bash
# Bump version (patch/minor/major)
bumpversion patch
git push
git push --tags
```

## Architecture

### Core Modules

- **fx_lib/log.py**: Logging utilities with YAML configuration support and Zoho SMTP handler
  - `setup_logging()`: Configures logging from YAML files
  - `ZohoSMTPHandler`: Custom logging handler for email notifications
  - Terminal color utilities for console output

- **fx_lib/zoho_email.py**: Email functionality using Zoho SMTP
  - `Email` class: Context manager for sending emails via Zoho
  - Requires `.email_config.yaml` configuration file

- **fx_lib/datetime_ext.py**: Extended datetime classes
  - `Datetime`: Enhanced datetime with custom string formatting methods
  - `Date`: Enhanced date with offset operations and utility methods

- **fx_lib/str_ext.py**: String extensions
  - `StrExt`/`S`: Enhanced string class with utility methods

- **fx_lib/list_ext.py**: List extensions
  - `ListExt`: Enhanced list class with join functionality

- **fx_lib/func.py**: Functional utilities
  - `range1()`: 1-indexed range function
  - `enumerate1()`: 1-indexed enumerate function  
  - `p()`: Function composition utility
  - `convert_size()`: Human-readable file size formatting
  - `chunks()`: Split lists into chunks

- **fx_lib/math.py**: Mathematical utilities
  - `modable()`: Check if number is divisible

### Configuration Files

The project uses several configuration mechanisms:

- **Logging**: Expects YAML config files (see `docs/log_config_example.yaml`)
- **Email**: Requires `.email_config.yaml` in project root or home directory
- **Setup**: Uses `setup.py` with requirements in `requirements_dev.txt`

### Testing Strategy

- Uses Python's built-in `unittest` framework
- Tests located in `tests/` directory
- Minimal test coverage currently - mainly placeholder tests
- Supports testing across multiple Python versions via tox

### Dependencies

- **Runtime**: PyYAML >= 5.4 (only runtime dependency)
- **Development**: flake8, tox, coverage, Sphinx, twine, bumpversion, watchdog

## Development Notes

- Follows traditional Python package structure with setup.py
- Uses reStructuredText for documentation (README.rst, CONTRIBUTING.rst)
- Configured for PyPI distribution
- Supports Python 3.7-3.12
- Uses MIT license
- Email functionality specifically designed for Zoho email service
- Configuration files are expected in specific locations (project root or home directory)