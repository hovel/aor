from fabric.api import *

PROJECT_NAME = 'aor'

PROJECT_BASEDIR = '/home/zeus/webapps/%s' % PROJECT_NAME
PROJECT_ROOT = '/home/zeus/webapps/%s/%s' % (PROJECT_NAME, PROJECT_NAME)
PROJECT_SOURCE = 'ssh://hg@bitbucket.org/amigo/%s' % PROJECT_NAME

env.hosts = ['zeus@zeus.webfactional.com']


def install():
    with cd(PROJECT_BASEDIR):
        run('hg clone %s' % PROJECT_SOURCE)
        run('virtualenv --clear --no-site-packages env')
        run('./env/bin/pip install -r %s/build/pipreq.txt' % PROJECT_NAME)
        #run('./env/bin/python manage.py syncdb --all')
        #run('./env/bin/python manage.py collectstatic --noinput')


def fu():
    with cd(PROJECT_ROOT):
        run('hg pull')
        run('hg update -C default')
        run('../env/bin/pip install -e hg+ssh://hg@bitbucket.org/amigo/dnews#egg=dnews-dev --upgrade --no-deps')
        run('../env/bin/python manage.py syncdb')
        run('../env/bin/python manage.py migrate')
        run('../env/bin/python manage.py collectstatic --noinput')
        run('kill -HUP `head -n 1 %s/aor.pid`' % PROJECT_ROOT)
