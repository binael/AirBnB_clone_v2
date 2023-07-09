#!/usr/bin/python3

""" A python script that compreses the content of the web folder
"""

from fabric.api import local, run, put, settings
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
    if not os.path.exits(archive_path):
        return False

    class FabricException(Exception):
        pass

    with settings(abort_exception=FabricException):
        try:
            file_name = os.path.basename(archive_path)
            name = file_name.split('.')
            folder = name[0]
            full_folder = '/data/web_static/releases/{}/'.format(folder)

            with cd('/tmp'):
                put(archive_path, '{}'.format(file_name))

            run('mkdir -p {}'.format(full_folder))
            run('tar -xzf /tmp/{} -C {}'.format(file_name, full_folder))

            with cd('/tmp'):
                run('rm -f {}'.file_name)

            run('rm -f /data/web_static/current/')
            run('ln -sf {} /data/web_static/current/'.format(full_folder))
        except FabricException:
            return False
        else:
            return True
