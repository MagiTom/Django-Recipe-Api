

import os
from storages.backends.s3boto3 import S3Boto3Storage

class SupabaseMediaStorage(S3Boto3Storage):
    bucket_name = os.environ.get("SUPABASE_BUCKET_NAME")
    endpoint_url = os.environ.get("SUPABASE_ENDPOINT")
    default_acl = "public-read"
    file_overwrite = False
