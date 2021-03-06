#Python S3 Sync Helper

```python
# Written Hastily by:	Philip Joyner
# Version:				0.1
# Last Updated:			2014-04-09
# Python Version:		2.7
# Requirements:			Python 2.7, Scandir & Boto
# Forked by:            Josh Kehoe
# Fork Last Updated:    2016-05-12
# Forked Modifications:
#   1) Linux support
#   2) Check last update date in addition to file size when synching
#   3) Proxy configuration
```

###Installation


Python - Download and install Python 2.7

https://www.python.org/download/releases/2.7.6/


pip - Install pip to install boto. Makes package installation a breeze

http://www.pip-installer.org/en/latest/installing.html

boto

pip install boto

Scandir

Windows:

Unpack from App/Installs/scandir-master.zip and run the following from within the scandir directory: python setup.py install

\*nix:

sudo pip install Scandir




###How to Use



Rename config.example.py to config.py

Windows:
```python
Config = {
	's3_access' : 'YOUR ACCESS HERE',
	's3_secret' : 'YOUR SECRET HERE',
	's3_bucket' : 'YOUR BUCKET HERE',
	's3_folder' : None, 								# default is: None
	'local_dir' : 'C:/full/path/of/directory/to/upload', # use '/' in place of '\',
	'upload_threads'  : 15,
	'proxy'           : None,     # if behind a proxy, add it here (without http(s)://)
	'proxy_port'      : None,     # proxy port
	'proxy_user'      : None,     # if your proxy requires authentication, add it here
	'proxy_pass'      : None
}
```

\*nix:
```python
Config = {
	's3_access' : 'YOUR ACCESS HERE',
	's3_secret' : 'YOUR SECRET HERE',
	's3_bucket' : 'YOUR BUCKET HERE',
	's3_folder' : None, 								# default is: None
	'local_dir' : 'home/{username}/directory/to/upload', # use '/' in place of '\',
	'upload_threads'  : 15,
	'proxy'           : None,     # if behind a proxy, add it here (without http(s)://)
	'proxy_port'      : None,     # proxy port
	'proxy_user'      : None,     # if your proxy requires authentication, add it here
	'proxy_pass'      : None
}

```

The config file requires the following info

s3_access: api access key

s3_secret: api secret

s3_bucket: The bucket in s3 where your files will be uploaded

s3_folder: Optional. The folder to upload the files to. If not set this will become the local_dir folder

local_dir: The local directory you would like to upload files from

upload_threads: The number of threads to use for simultaneous uploads. Don't use too many or your computer will crash. :(

If you are behind a proxy, use proxy and proxy_port. If your proxy requires authentication, also use proxy_user and proxy_pass.

###Warnings & Notes


Use at your own risk. If a key exists and a file is uploaded that key will be overwritten. Make sure the bucket "folder" you are uploading to is the one you would like to overwrite.

Files that are in S3 that have been deleted locally will not be deleted. In this version S3 does not sync down first. This would be a good feature though.

Might be nice to add a GUI too. One thing at a time.

Comparing MD5 hashes would be a great addition, but it would require downloading each file from S3 first in order to get
the MD5 hash. As a poor man's work around, we are comparing the last modified timestamp on the local file with to last
modified timestamp of the file in S3 - which is when it was last uploaded - and replacing if it is newer.