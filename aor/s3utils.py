from storages.backends.s3boto3 import S3Boto3Storage


class StaticRootS3Boto3Storage(S3Boto3Storage):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'static'
        super(StaticRootS3Boto3Storage, self).__init__(*args, **kwargs)


class MediaRootS3Boto3Storage(S3Boto3Storage):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'media'
        super(MediaRootS3Boto3Storage, self).__init__(*args, **kwargs)
