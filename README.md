template-geodjango
==================

This is a helper template to get started with GeoDjango and a few other libraries that
we end up using a lot here at sigma-geosistemas.

This consists of:

* django;
* psycopg2;
* djangorestframework;
* djangorestframework-gis;
* celery;
* redis;

## What does this template do?

This template set's up a few things for you, such as:

* requirements separated by environment type;
* settings separated by environment type;
* settings configured using environment variables, for a more secure deploy;
* sample nginx configuration;
* sample shell script for running the django application;
* sample supervisor script for watching over the application;

## To Do

* Samples for celery worker and celery beat;