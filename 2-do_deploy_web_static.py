#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy:
"""

import os
from fabric.api import *

env.user = "ubuntu"
env.hosts = ['54.90.34.141', '34.229.49.23', '127.0.0.1']


def do_pack():
    """
    a function that generates a .tgz archive from
    the contents of the web_static folder of your AirBnB Clone
    repo, using the function do_pack.
    """
    today = dt.now()
    day = today.day
    month = today.month
    year = today.year
    hour = today.hour
    mins = today.minute
    sec = today.second

    f_date = f"{year}{month}{day}{hour}{mins}{sec}"
    tar_name = f"web_static_{f_date}.tgz"
    print(f'Packing web_static to versions/{tar_name}')

    local("mkdir -p versions")
    archive = local(f"tar -czvf versions/{tar_name} ./web_static")
    size = os.path.getsize(f"versions/{tar_name}")
    print(f'web_static packed: verions/{tar_name} -> {size}Bytes')

    if archive.succeeded:
        return f"versions/{tar_name}"
    return None


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
        # upload archive
        put(archive_path, '/tmp')
        # get filename and directory path
        archive_name = archive_path.split('/')[-1]
        unpacked = archive_name.split('.')[0]
        new_dir = f'/data/web_static/releases/{unpacked}'
        # make new dir to store unzipped archive
        run(f'mkdir -p {new_dir}')
        # unzip archive to new dir
        run(f'tar -xvzf /tmp/{archive_name} -C {new_dir}')
        sudo(f'rsync -la {new_dir}/web_static/* {new_dir}')
        # remove archive, web_static, previous sym link
        run(f'rm /tmp/{archive_name}')
        run(f'rm -rf {new_dir}/web_static/')
        run('rm -rf /data/web_static/current')
        # create new symlink
        run(f'ln -sf {new_dir} /data/web_static/current')
        print("New version deployed!")
        return True
    except Exception:
        return False
