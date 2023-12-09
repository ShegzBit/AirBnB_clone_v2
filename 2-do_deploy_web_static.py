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
    Deploy the archived directory to the servers

    Args:
        archive_path (str): The full path of the archived directory
                            to be deployed
    Return:
        True if succeeded, otherwise False
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Copy the compressed file to the remote server
        put(archive_path, "/tmp/")

        # Get `archive_path` without the extension
        compressed_file = os.path.basename(archive_path)
        archive_name = compressed_file.split(".")[0]

        # Make the destination directory
        destination_path = '/data/web_static/releases/'
        run("mkdir -p {}{}/".format(destination_path, archive_name))

        # Uncompress the file on the remote server
        command = "tar -xzf {} -C {}"
        compressed_file = "/tmp/{}".format(compressed_file)
        full_archive_name_dir = "{}{}/".format(destination_path, archive_name)
        run(command.format(compressed_file, full_archive_name_dir))

        # Remove the compressed file from where it was initially copied to
        run("rm {}".format(compressed_file))

        # Move the uncompressed files to the appropriate location for serving
        run("mv {0}web_static/* {0}".format(full_archive_name_dir))

        # Remove `web_static` directory in the `destination_path`
        run("rm -rf {}web_static".format(full_archive_name_dir))

        # Remove precious created symbolic link for testing
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link, linked to the new version of the code
        target = full_archive_name_dir
        link = '/data/web_static/current'
        run("ln -s {} {}".format(target, link))
    except Exception:
        return False

    print("New version deployed!")
    return True
