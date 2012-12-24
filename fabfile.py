from fabric.api import *

PROJECT_NAME = 'archlinux'

PROJECT_BASEDIR = '/home/amigo/archlinux'
PROJECT_ROOT = '/home/amigo/archlinux/app'
PROJECT_SOURCE = 'https://amigo@bitbucket.org/amigo/aor'

env.hosts = ['amigo@ec2-50-17-136-53.compute-1.amazonaws.com']


def clone_project():
    with cd(PROJECT_BASEDIR):
        run('hg clone %s' % PROJECT_SOURCE)
    put_settings()

def update_project():
    with cd(PROJECT_ROOT):
        run('hg pull')
        run('hg update -C default')
    put_settings()

def setup_env():
    with cd(PROJECT_BASEDIR):
        run('virtualenv --clear --no-site-packages env')

def update_env():
    with cd(PROJECT_BASEDIR):
        run('./env/bin/pip install -U -r %s/build/pipreq.txt' % PROJECT_NAME)

def syncdb():
    with cd(PROJECT_ROOT):
        run('../env/bin/python manage.py syncdb --migrate')

def syncdb_all():
    with cd(PROJECT_ROOT):
        run('../env/bin/python manage.py syncdb --all')

def collect_static():
    with cd(PROJECT_ROOT):
        run('../env/bin/python manage.py collectstatic --noinput')

def start():
    with cd(PROJECT_ROOT):
        run('../env/bin/python manage.py run_gunicorn -c gunicorn.conf.py')

def restart():
    with cd(PROJECT_BASEDIR):
        run('kill -HUP `cat /home/amigo/archlinux/log/pidfile`')

def stop():
    with cd(PROJECT_BASEDIR):
        run('kill `cat /home/amigo/archlinux/log/pidfile`')

def put_settings():
    put('aor/settings_local.py', '/home/amigo/archlinux/app/aor/local.py')

def get_settings():
    get('/home/amigo/archlinux/app/aor/local.py', 'aor/settings_local.py')

def install():
    clone_project()
    setup_env()
    update_env()
    syncdb_all()
    collect_static()

def update():
    stop()
    update_project()
    syncdb()
    collect_static()
    start()
