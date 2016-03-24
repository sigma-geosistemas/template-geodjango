#!/bin/bash

source /opt/apps/.virtualenvs/{{cookiecutter.repo_name}}/bin/activate
cd /opt/apps/{{cookiecutter.repo_name}}/src
./manage.py dbbackup
./manage.py mediabackup