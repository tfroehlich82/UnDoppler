# -*- coding: utf-8 -*-

"""
Module Documentation
"""


import os
from datetime import datetime


__author__ = "Thorsten Froehlich <tfroehlich82@gmx.ch>"
__version__ = 1.00


def compare_binary(file_1, file_2):
    with open(file_1, 'rb') as file1, open(file_2, 'rb') as file2:
        data1 = file1.read()
        data2 = file2.read()

    if data1 != data2:
        return False
    return True


# def is_in(pattern, file_1):
#     with open(file_1, 'rb') as file1:
#         data1 = file1.read()
#
#     return pattern in data1


def get_filesize(f):
    return os.stat(f).st_size


def get_datetime(f):
    return datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M:%S')


def get_extension(f):
    return os.path.splitext(f)[-1]


def get_filename(f):
    return os.path.basename(f).replace(get_extension(f), "")


def same_filesize(file_1, file_2):
    return get_filesize(file_1) == get_filesize(file_2)


def same_datetime(file_1, file_2):
    return get_datetime(file_1) == get_datetime(file_2)


def same_filename(file_1, file_2):
    return get_filename(file_1) == get_filename(file_2)


def same_extension(file_1, file_2):
    return get_extension(file_1) == get_extension(file_2)
