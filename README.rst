======
fx-lib
======

.. image:: https://img.shields.io/pypi/v/fx-lib.svg
   :target: https://pypi.org/project/fx-lib/
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/fx-lib.svg
   :target: https://pypi.org/project/fx-lib/
   :alt: Python Versions

.. image:: https://img.shields.io/pypi/l/fx-lib.svg
   :target: https://github.com/frankyxhl/fx_lib/blob/main/LICENSE
   :alt: License

.. image:: https://img.shields.io/github/actions/workflow/status/frankyxhl/fx_lib/main.yml
   :target: https://github.com/frankyxhl/fx_lib/actions
   :alt: Build Status

Frank Xu's personal Python utility library providing common functionality for logging, email, datetime manipulation, string operations, mathematical functions, and list utilities.

**PyPI**: https://pypi.org/project/fx-lib/

**GitHub**: https://github.com/frankyxhl/fx_lib

Features
--------

- **Comprehensive Logging**: YAML-based configuration with color terminal output and email handlers
- **Zoho Email Integration**: Simple email sending with context manager support
- **Enhanced DateTime**: Extended datetime/date classes with convenient formatting and arithmetic operations
- **String & List Extensions**: Enhanced string and list classes with utility methods
- **Functional Utilities**: Practical functions like 1-indexed ranges, function composition, and size formatting
- **Mathematical Helpers**: Common mathematical operations and checks
- **Fully Tested**: 150+ unit tests with >80% coverage
- **Modern Python**: Type hints, f-strings, proper exception handling
- **Python 3.7-3.12 Support**: Tested across multiple Python versions

Installation
------------

Install from PyPI:

.. code-block:: bash

    pip install fx-lib

Or install from GitHub:

.. code-block:: bash

    pip install git+https://github.com/frankyxhl/fx_lib.git

Quick Start
-----------

Logging Module
**************

Configure logging with YAML files and colored terminal output:

.. code-block:: python

    import logging
    from fx_lib.log import setup_logging

    # Setup logging from YAML configuration
    setup_logging("logging.yaml", default_level=logging.DEBUG)
    log = logging.getLogger("my_app")

    # Use colored terminal output
    from fx_lib.log import green, red, yellow
    print(green("Success!"))
    print(yellow("Warning!"))
    print(red("Error!"))

Email Module
************

Send emails via Zoho SMTP with simple context manager:

.. code-block:: python

    from fx_lib.zoho_email import Email

    # Automatically reads configuration from .email_config.yaml
    with Email.read_config() as email:
        email.send("Subject", "Email content")

DateTime Extensions
*******************

Enhanced datetime classes with convenient methods:

.. code-block:: python

    from fx_lib.datetime_ext import Date, Datetime

    # Date utilities
    today = Date.today()
    tomorrow = today.tomorrow()
    yesterday = today.yesterday()
    next_week = today.next_days(7)
    
    # Formatting
    print(today.to_yyyy_mm_dd())  # 2025-08-24
    print(today.to_yyyymmdd())    # 20250824
    
    # Datetime utilities
    now = Datetime()
    formatted = now.to_iso_date_time()  # 2025-08-24T10:30:45

Functional Utilities
********************

Practical helper functions for common operations:

.. code-block:: python

    from fx_lib.func import range1, enumerate1, p, convert_size, chunks

    # 1-indexed iterations
    for i in range1(5):
        print(i)  # Prints 1, 2, 3, 4, 5

    for i, val in enumerate1(['a', 'b', 'c']):
        print(i, val)  # Prints (1, 'a'), (2, 'b'), (3, 'c')

    # Function composition
    result = p(5, lambda x: x * 2, lambda x: x + 3)  # ((5 * 2) + 3) = 13

    # Human-readable file sizes
    print(convert_size(1536))  # "1.5KB"
    print(convert_size(1048576))  # "1.0MB"

    # Split lists into chunks
    data = [1, 2, 3, 4, 5, 6, 7]
    for chunk in chunks(data, 3):
        print(chunk)  # [1, 2, 3], [4, 5, 6], [7]

String & List Extensions
************************

Enhanced string and list classes:

.. code-block:: python

    from fx_lib.str_ext import StrExt, S
    from fx_lib.list_ext import ListExt

    # String extensions
    s = S("hello world")
    # Add your string manipulation here

    # List extensions
    lst = ListExt([1, 2, 3])
    joined = lst.join(", ")  # "1, 2, 3"

Mathematical Utilities
*********************

Common mathematical operations:

.. code-block:: python

    from fx_lib.math import modable

    # Check if number is divisible
    if modable(10, 2):
        print("10 is divisible by 2")

Configuration
-------------

Email Configuration
*******************

Create `.email_config.yaml` in your project or home directory:

.. code-block:: yaml

    zoho_email:
      username: your_email@zoho.com
      password: your_password
      sender_title: Your Name
      recipient: recipient@example.com

Logging Configuration
*********************

Create `logging.yaml` for custom logging setup:

.. code-block:: yaml

    version: 1
    formatters:
      default:
        format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    handlers:
      console:
        class: logging.StreamHandler
        level: DEBUG
        formatter: default
        stream: ext://sys.stdout
    root:
      level: INFO
      handlers: [console]

See `docs/log_config_example.yaml <https://github.com/frankyxhl/fx_lib/blob/main/docs/log_config_example.yaml>`_ for a complete example.

Development
-----------

.. code-block:: bash

    # Clone the repository
    git clone git@github.com:frankyxhl/fx_lib.git
    cd fx_lib

    # Install in development mode
    pip install -e .

    # Run tests
    python -m unittest discover tests/

    # Run tests with coverage
    coverage run --source fx_lib -m unittest discover
    coverage report

    # Run linting
    flake8 fx_lib tests

Requirements
------------

- Python 3.7-3.12
- PyYAML >= 5.4

License
-------

MIT License - see `LICENSE <https://github.com/frankyxhl/fx_lib/blob/main/LICENSE>`_ file for details.

Author
------

**Frank Xu**

- Email: frank@frankxu.me
- GitHub: https://github.com/frankyxhl

Contributing
------------

Contributions are welcome! Please feel free to submit a Pull Request.

Links
-----

- **PyPI Package**: https://pypi.org/project/fx-lib/
- **Source Code**: https://github.com/frankyxhl/fx_lib
- **Issue Tracker**: https://github.com/frankyxhl/fx_lib/issues

Changelog
---------

See `HISTORY.rst <https://github.com/frankyxhl/fx_lib/blob/main/HISTORY.rst>`_ for a detailed changelog.