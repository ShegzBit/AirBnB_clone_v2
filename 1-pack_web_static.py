#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB Clone
repo, using the function do_pack.
"""
from fabric.api import *
from datetime import datetime as dt

# env.hosts = ['ubuntu@34.229.49.23', 'ubuntu@54.90.34.141']
# env.user = "ubuntu"

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
    hour =  today.hour
    mins = today.minute
    sec = today.second
    f_date = f"{year}{month}{day}{hour}{mins}{sec}"
    tar_name = f"web_static_{f_date}.tgz"

    local("mkdir -p versions")
    local(f"tar -czvf versions/{tar_name} ./web_static")
    return tar_name
