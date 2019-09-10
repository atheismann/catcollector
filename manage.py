#!/usr/bin/env python
<<<<<<< HEAD
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
=======
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catcollector.settings')
>>>>>>> 8ef656553446a01c279f0b34583b1507b163af7b
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
<<<<<<< HEAD


if __name__ == '__main__':
    main()
=======
>>>>>>> 8ef656553446a01c279f0b34583b1507b163af7b
