#!/usr/bin/python3

""" A python script that compreses the content of the web folder
"""

from fabric.api import run, put, env
from datetime import datetime
import os

env.hosts = ['52.86.109.82', '54.175.133.2']


def do_pack():
    """
    A python fabric function that compreses to tgz
    """

    my_time = datetime.now()
    my_time = my_time.strftime("%Y%m%d%H%M%S")
    my_file = 'web_static_{}.tgz'.format(my_time)

    local('mkdir -p versions')
    result = local('tar -cvzf versions/{} web_static'.format(my_file))

    if result.failed:
        return None
    else:
        local('chmod 664 versions/{}'.format(my_file))
        return 'versions/{}'.format(my_file)


def do_deploy(archive_path):
    """
    A python fabric function that deploys and distributes archive
    to your web servers
    Arguments:
        archive_path - the path to archive
    """

    if not os.path.exists(archive_path):
        return False

    for host in env.hosts:
        f_name = os.path.basename(archive_path)
        name = f_name.split('.')
        folder = name[0]
        full_folder = '/data/web_static/releases/{}/'.format(folder)

        r = put(archive_path, '/tmp/{}'.format(f_name))
        if r.failed:
            return False

        r = run('mkdir -p {}'.format(full_folder))
        if r.failed:
            return False

        r = run('tar -xzf /tmp/{} -C {}'.format(f_name, full_folder))
        if r.failed:
            return False

        r = run('rm -f /tmp/{}'.format(f_name))
        if r.failed:
            return False

        r = run('rm -R -f /data/web_static/current/')
        if r.failed:
            return False

        r = run('ln -sf {} /data/web_static/current/'.format(full_folder))
        if r.failed:
            return False

    return True
