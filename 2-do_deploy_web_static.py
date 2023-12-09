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
        new_dir = f'/data/web_static/releases/{unpacked}'
        with cd('/tmp'):
            run(f'mkdir -p {new_dir}')
            run(f'tar -xvzf {archive_name} -C {new_dir}')
            sudo(f'mv {new_dir}/web_static/* {new_dir}')
            run(f'rm {archive_name}')
            run(f'rm -rf {new_dir}/web_static/')
            run('rm -rf /data/web_static/current')
            run(f'ln -sf {new_dir} /data/web_static/current')
            print("New version deployed!")
        return True
    except Exception:
        return False
