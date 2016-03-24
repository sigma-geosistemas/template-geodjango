cookiecutter-geodjango
==================

This is a helper template to get started with GeoDjango and a few other libraries that
we end up using a lot here at sigma-geosistemas.

This consists of:

* django;
* django.contrib.gis;
* psycopg2;
* djangorestframework;
* djangorestframework-gis;
* celery;
* redis;
* django-dbbackup
* django-mailgun

## What does this template do?

This template set's up a few things for you, such as:

* requirements separated by environment type;
* settings separated by environment type;
* settings configured using environment variables, for a more secure deploy;
* sample nginx configuration;
* sample shell script for running the django application;
* sample supervisor script for watching over the application, with the user of environment variables for deploy;
* creates a generic index.html, located in ```<project_name>/templates``` folder and it's URL;

## What this template does not do for you?

* Fully configure nginx, supervisor and the shell runner - you should fill in details yourself!;

## To Do

* Samples for celery worker and celery beat;
* Lot's of other stuff;

# Usage

First install cookiecutter

```bash
pip install cookiecutter
```

Use it to create a new templated geodjango project

```bash
cookiecutter http://github.com/sigma-geosistemas/cookiecutter-geodjango
```

