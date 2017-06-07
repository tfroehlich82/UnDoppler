# -*- coding: utf-8 -*-

"""
Module Documentation
"""


from .media_types import MEDIA_TYPES


__author__ = "Thorsten Froehlich <tfroehlich82@gmx.ch>"
__version__ = 1.00


def analyze_file(filepath):
    for t in MEDIA_TYPES:
        if t().analyze(filepath):
            return t().identifier
    raise Exception()
