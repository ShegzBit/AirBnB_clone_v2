#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy:
"""

import os
from fabric.api import *


env.user = "ubuntu"
env.hosts = ['54.90.34.141', '34.229.49.23']


@task
def do_deploy(archive_path):
    """
    a Fabric task (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers,
    using the function do_deploy:
    """

    if not os.path.exists(archive_path):
        return False

    # versions/
    # archive name = web_static_20170315003959
    # .tgz
    try:
        put(archive_path, '/tmp')
        archive_name = archive_path.split('/')[-1]
        unpacked = archive_name.split('.')[0]
        new_dir = unpacked
        with cd('/tmp'):
            run(f'mkdir -p /data/web_static/releases/{new_dir}')
            run(f'tar -xvzf {archive_name} -C\
                /data/web_static/releases/{new_dir}')
            sudo(f'rsyinc -a /data/web_static/releases/{new_dir}/web_static/* \
                /data/web_static/releases/{new_dir}')
            run(f'rm {archive_name}')
            run(f'rm -r /data/web_static/releases/{new_dir}/web_static/')
            run(f'ln -sf /data/web_static/releases/{unpacked} \
                /data/web_static/current')
        return True
    except Exception:
        return False
