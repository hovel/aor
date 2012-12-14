from os.path import join, expanduser

bind = "127.0.0.1:24524"
max_requests = 1024
timeout = 15
workers = 2
daemon = True
pidfile = join(expanduser('~'), 'aor.pid')
accesslog = join(expanduser('~'), 'aor.access.log')
errorlog = join(expanduser('~'), 'aor.error.log')

