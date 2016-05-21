# IMPORT LIBRARIES
import os
from boto.s3.connection import S3Connection


class S3:
    access = None
    secret = None
    bucket = None
    proxy = None
    proxy_port = None
    proxy_user = None
    proxy_pass = None

    Conn = None
    Bucket = None

    # store url and token as variables in this class
    def __init__(self, access=None, secret=None, proxy=None, proxy_port=None, proxy_user=None, proxy_pass = None):
        self.access = access
        self.secret = secret
        self.proxy = proxy
        self.proxy_port = proxy_port
        self.proxy_user = proxy_user
        self.proxy_pass = proxy_pass


    def connect(self, _bucket=None):
        if _bucket == None:
            return False

        self.bucket = _bucket
        self.Conn = S3Connection(self.access, self.secret,
                                 proxy=self.proxy,
                                 proxy_port=self.proxy_port,
                                 proxy_user=self.proxy_user,
                                 proxy_pass=self.proxy_pass)
        self.Bucket = self.Conn.get_bucket(self.bucket)
        return True


    def upload(self, filein=None, fileout=None):
        if filein == None or filein == False:
            return False

        if fileout == None:
            fileout = os.path.basename(filein)

        if self.Conn == None or self.Bucket == False:
            return False
        
        # delete existing file of same name
        try:
            self.Bucket.delete_key(fileout)
        except:
            return filein + ' | Could not delete key in bucket: ' + fileout

        # upload file
        try:
            key = self.Bucket.new_key(fileout)
            #key.set_metadata('Content-Disposition', 'attachment')
            key.set_contents_from_filename(filein)
        except:
            return filein + ' | Could not upload file to bucket: ' + fileout

        return None


    def delete(self, file):
        key = self.Bucket.lookup(file)
        size = key.size
        try:
            self.Bucket.delete_key(file)
        except:
            return file + ' | Could not delete key in bucket: ' + file, None

        return None, key.size


    def size_and_date(self, key=None):
        if self.Bucket == None or key == None:
            return False

        key = self.Bucket.lookup(key)
        
        try:
            if key.size and key.last_modified:
                return key.size, key.last_modified
            elif key.size:
                return key.size, None
        except:
            return None, None

        return None, None


    def get_bucket_objects(self):
        if self.Bucket == None:
            return False

        keys = []
        for key in self.Bucket.list():
            keys.append(key.name.encode('utf-8'))

        return keys
