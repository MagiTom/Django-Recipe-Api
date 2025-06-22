import mimetypes
from storages.backends.s3boto3 import S3Boto3Storage
from supabase import create_client
import os
import hashlib
import time

class SupabaseMediaStorage(S3Boto3Storage):
    bucket_name = os.environ.get("SUPABASE_BUCKET_NAME")
    access_key = "unused"
    secret_key = os.environ.get("SUPABASE_SECRET_KEY")
    endpoint_url = os.environ.get("SUPABASE_URL") + "/storage/v1/s3"
    custom_domain = f"{os.environ.get('DOMAIN')}/storage/v1/object/public/{bucket_name}"
    querystring_auth = False
    addressing_style = "path"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = create_client(
            os.environ.get("SUPABASE_URL"),
            os.environ.get("SUPABASE_SECRET_KEY")
        )

    def exists(self, name):
        return False
    
    def _generate_safe_filename(self, name):
         _, ext = os.path.splitext(name)
         ext = ext.lower() or ".jpg"
         hash_part = hashlib.sha256(f"{name}-{time.time()}".encode()).hexdigest()[:16]
         
         return f"{hash_part}{ext}"

    def _save(self, name, content):
        data = content.read()
        name = self._generate_safe_filename(name)
        content_type, _ = mimetypes.guess_type(name)
        content_type = content_type or "application/octet-stream"

        self.client.storage.from_(self.bucket_name).upload(
            name,
            data,
            {"content-type": content_type}
        )

        return name
    
    def delete(self, name):
         try:
             self.client.storage.from_(self.bucket_name).remove([name])
         except Exception as e:
              import logging
              logging.getLogger(__name__).exception(f"Błąd przy usuwaniu pliku: {name}")

