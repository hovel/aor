class PHPBB3(object):
    """
    PHPBB3 database router
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'django_phpBB3':
            return 'phpbb3'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'django_phpBB3':
            return 'phpbb3'
        return None

    def allow_syncdb(self, db, model):
        if db == 'default' and model._meta.app_label == 'django_phpBB3':
            return False
        return None

