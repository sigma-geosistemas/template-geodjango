# coding: utf-8
import os
from fabric.api import task, run
from fabric.utils import abort
from fabric.context_managers import cd
from fabtools.python import virtualenv, install_requirements as fab_install_requirements
from fabtools.supervisor import restart_process
from fabtools.git import pull, checkout
from deploy.configuration import *
from deploy.database import *
from deploy.dependencies import *
from deploy.django import *
from deploy.system import *
from deploy.virtualenv import *
from deploy.webserver import *
from fabtools.vagrant import vagrant


@task
def backup_venv(venv):
    run('rm -rf {0}-backup'.format(venv))
    run('cp -r {0} {0}-backup'.format(venv))


@task
def restore_venv(venv):
    run('rm -rf {0}-post-restore'.format(venv))
    run('mv {0} {0}-post-restore'.format(venv))
    run('cp -r {0}-backup {0}'.format(venv))


@task
def maintenance_on(venv, path):
    '''this command requires you to set up in the server DJANGO_SETTINGS_MODULE'''
    with virtualenv(venv):
        with cd(os.path.join(path, 'src')):
            run('./manage.py maintenance_mode on')


@task
def maintenance_off(venv, path):
    '''this command requires you to set up in the server DJANGO_SETTINGS_MODULE'''
    with virtualenv(venv):
        with cd(os.path.join(path, 'src')):
            run('./manage.py maintenance_mode off')


def get_latest_version():
    gitrev = run('git rev-parse HEAD')
    return gitrev.splitlines()[-1]


@task
def update_appserver(venv, path, branch='master'):
    '''this command requires you to set up in the server DJANGO_SETTINGS_MODULE'''
    backup_venv(venv)

    with virtualenv(venv):
        with cd(path):
            version = get_latest_version()
            try:
                maintenance_on(venv, path)
                checkout(path, branch)
                pull(path)
                run('bower install')
                run('pip install -r requirements/production.txt')
                with cd(os.path.join(path, 'src')):
                    run('./manage.py migrate --noinput')
                    run('./manage.py collectstatic --noinput')
            except:
                checkout(path, version)
                print u'rolledback to version {0}'.format(version)
            finally:
                maintenance_off(venv, path)