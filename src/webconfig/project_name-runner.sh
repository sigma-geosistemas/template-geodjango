#!/bin/bash

NAME="{{ project_name }}"

VIRTUALENV_BASE_DIR=/opt/apps/.virtualenvs
VIRTUALENV_DIR=$VIRTUALENV_BASE_DIR/{{ project_name }}/bin

APP_BASE_DIR=/opt/apps/{{ project_name }}
DJANGO_DIR=$APP_BASE_DIR/src

# configure the sock file. create the directory if necessary
SOCK_FILE=$APP_BASE_DIR/run/gunicorn.sock
RUN_DIR=$(dirname $SOCK_FILE)
test -d $RUN_DIR || mkdir -p $RUN_DIR

# configure the log file. create the directory if necessary
LOG_FILE=$APP_BASE_DIR/logs/supervisor-{{ project_name }}.log
LOG_DIR=$(dirname $LOG_FILE)
test -d $LOG_DIR || mkdir -p $LOG_DIR

# user settings
USER={{ user }}
GROUP={{ group }}

NUM_WORKERS=3

cd $VIRTUALENV_DIR
source activate
cd $DJANGO_DIR

export PYTHONPATH=$DJANGO_DIR:$PYTHONPATH

gunicorn {{ project_name }}.wsgi:application \
   --settings=$DJANGO_SETTINGS_MODULE \
   --name $NAME \
   --workers $NUM_WORKERS \
   --user=$USER --group=$GROUP \
   --log-level=debug \
   --bind=127.0.0.1:8000 \
   --timeout 500
