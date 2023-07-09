#!/usr/bin/python3

""" A python script that compreses the content of the web folder
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    A python fabric function that compreses to tgz
    """

    my_time = datetime.strftime('%Y%M%D%H%M%S')
    file_name = 'web_static_{}.tgz'.format(my_time)

    local('mkdir -p versions')
    result = local('tar -czvf versions/{} web_static'.format(file_name))

    if result.failed:
        return None
    else:
        return 'versions/{}'.format(file_name)
