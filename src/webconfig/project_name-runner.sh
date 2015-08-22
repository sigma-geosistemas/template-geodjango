#!/bin/bash

NAME="{{ project_name }}"
DJANGODIR=/opt/apps/{{ project_name }}/src
VIRTUALENVDIR=/opt/apps/.virtualenvs/{{ project_name }}/bin
SOCKFILE=/opt/apps/{{ project_name }}/run/gunicorn.sock
USER={{ user }}
GROUP={{ group }}
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE="{{ project_name }}.settings.production"
export SECRET_KEY="<changethisinproduction>"

# Activate the virtual environment
cd $VIRTUALENVDIR
source activate
cd $DJANGODIR

export PYTHONPATH=$DJANGODIR:$PYTHONPATH

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

gunicorn {{ project_name }}.wsgi:application \
   --settings=$DJANGO_SETTINGS_MODULE \
   --name $NAME \
   --workers $NUM_WORKERS \
   --user=$USER --group=$GROUP \
   --log-level=debug \
   --bind=127.0.0.1:8004 \
   --timeout 500
