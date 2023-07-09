#!/usr/bin/python3

""" A python script that compreses the content of the web folder
"""

from fabric.api import local
from datetime import datetime


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
