import urllib
import urllib2

try:
    from aor.local import CLOUDFLARE_TOKEN, CLOUDFLARE_EMAIL
except ImportError:
    pass

from fabric.api import *

PROJECT_NAME = 'archlinux'

PROJECT_BASEDIR = '/home/amigo/archlinux'
PROJECT_ROOT = '/home/amigo/archlinux/aor'
PROJECT_SOURCE = 'https://github.com/hovel/aor.git'

env.hosts = ['amigo@ec2-54-226-65-210.compute-1.amazonaws.com']
env.always_use_pty = False


def purge_clouflare_static():
    response = urllib2.urlopen('https://www.cloudflare.com/api_json.html',
                               data=urllib.urlencode({
                                   'a': 'fpurge_ts',
                                   'tkn': CLOUDFLARE_TOKEN,
                                   'email': CLOUDFLARE_EMAIL,
                                   'z': 'archlinux.org.ru',
                                   'v': '1'
                               }))
    print response.read()


def clone_project():
    with cd(PROJECT_BASEDIR):
        run('git clone %s' % PROJECT_SOURCE)
    put_settings()


def update_project():
    with cd(PROJECT_ROOT):
        run('git pull origin master')
        run('git checkout master')


def setup_env():
    with cd(PROJECT_BASEDIR):
        run('virtualenv --clear --no-site-packages env')


def update_env():
    with cd(PROJECT_ROOT):
        run('%s/env/bin/pip install -U -r %s/build/pipreq.txt' % (PROJECT_BASEDIR, PROJECT_ROOT))


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
        run('./gunicorn.sh start')


def restart():
    with cd(PROJECT_ROOT):
        run('./gunicorn.sh reload')


def stop():
    with cd(PROJECT_ROOT):
        run('./gunicorn.sh stop')


def put_settings():
    put('aor/settings_local.py', '/home/amigo/archlinux/aor/aor/local.py')


def get_settings():
    get('/home/amigo/archlinux/aor/aor/local.py', 'aor/settings_local.py')


def install():
    clone_project()
    setup_env()
    update_env()
    syncdb_all()
    collect_static()


def update():
    update_project()
    update_env()
    syncdb()
    collect_static()
    restart()


def soft_update():
    update_project()
    syncdb()
    collect_static()
    restart()
