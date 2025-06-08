from storages.backends.s3boto3 import S3Boto3Storage
import os

class SupabaseMediaStorage(S3Boto3Storage):
    bucket_name = os.environ.get("SUPABASE_BUCKET_NAME")
    custom_domain = f"{os.environ.get('SUPABASE_ENDPOINT')}/storage/v1/object/public/{bucket_name}"
    access_key = "unused"
    secret_key = os.environ.get("SUPABASE_SECRET_KEY")
    endpoint_url = os.environ.get("SUPABASE_ENDPOINT")
    querystring_auth = False
    addressing_style = "path"
