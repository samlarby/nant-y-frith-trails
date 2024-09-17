from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


def StaticStorage(S3Boto3Storage):
    location = setting.STATICFILES_LOCATION


def MediaStorage(S3Boto3Storage):
    location = setting.MEDIAFILES_LOCATION