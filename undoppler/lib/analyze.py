# -*- coding: utf-8 -*-

"""
Module Documentation
"""


import os
from .media_types import MEDIA_TYPES
from .strategies import Default_Strategy


__author__ = "Thorsten Froehlich <tfroehlich82@gmx.ch>"
__version__ = 1.00


def analyze_file(filepath):
    for t in MEDIA_TYPES:
        if t().analyze(filepath):
            return t().identifier
    raise Exception()


def check_extensions():
    pass


def compare_paths(fp1, fp2, recursive=True):
    files_1 = []
    files_2 = []
    equal_files = []
    for dirpath1, dnames1, fnames1 in os.walk(fp1):
        for x in fnames1:
            files_1.append(os.path.join(dirpath1, x))
    for dirpath2, dnames2, fnames2 in os.walk(fp2):
        for x in fnames2:
            files_2.append(os.path.join(dirpath2, x))
    for f1 in files_1:
        for f2 in files_2:
            for s in Default_Strategy:
                for t in s:
                    fu = t[0]
                    res = t[1]
                    if fu(f1, f2) != res:
                        # print("%s != %s" % (f1, f2))
                        break
                    elif fu.__name__ == "compare_binary":
                        # print("%s == %s (%s)" % (f1, f2, fu.__name__))
                        ef = (f1, f2)
                        if ef not in equal_files:
                            equal_files.append(ef)
    print(equal_files)
