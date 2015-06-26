#!/bin/bash

NAME="{{ project_name }}"
DJANGODIR=/opt/apps/{{ project_name }}/src
VIRTUALENVDIR=/opt/apps/.virtualenvs/{{ project_name }}/bin
SOCKFILE=/opt/apps/{{ project_name }}/run/gunicorn.sock
USER=app-runner
GROUP=app-runner
NUM_WORKERS=4
# DJANGO_SETTINGS_MODULE= determinado por variavel de ambiente e pelo supervisor

echo "Starting $NAME"

# Activate the virtual environment
cd $VIRTUALENVDIR
source activate
cd $DJANGODIR

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

echo $PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

gunicorn {{ project_name }}.wsgi:application \
   --name $NAME \
   --workers $NUM_WORKERS \
   --user=$USER --group=$GROUP \
   --log-level=debug \
   --bind=127.0.0.1:8004 \
   --timeout 500
