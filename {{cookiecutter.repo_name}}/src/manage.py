#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
	# local por default
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.app_name}}.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
