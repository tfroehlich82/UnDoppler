# -*- coding: utf-8 -*-

"""
Module Documentation
"""


from .comparisons import same_datetime, same_filesize, same_extension, same_filename, compare_binary


__author__ = "Thorsten Froehlich <tfroehlich82@gmx.ch>"
__version__ = 1.00


Default_Strategy = [
    [
        (same_extension, True),
        (same_filename, True),
        (same_datetime, True),
        (same_filesize, True),
        (compare_binary, True),
    ],
    [
        (same_filesize, True),
        (compare_binary, True),
    ],
]
