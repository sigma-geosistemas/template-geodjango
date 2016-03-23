#!/bin/bash

source /opt/apps/.virtualenvs/{{ project_name }}/bin/activate
cd /opt/apps/{{ project_name }}/src
./manage.py dbbackup
./manage.py mediabackup