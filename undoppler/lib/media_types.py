# -*- coding: utf-8 -*-

"""
Module Documentation
"""


from .file_extensions import EXTENSIONS
from .signatures import SIGNATURES


__author__ = "Thorsten Froehlich <tfroehlich82@gmx.ch>"
__version__ = 1.00


class MediaType(object):
    identifier = None

    @property
    def extensions(self):
        return EXTENSIONS.get(self.identifier, [])

    @property
    def default_extension(self):
        if len(self.extensions) > 0:
            return self.extensions[0]
        raise Exception()

    @property
    def signature(self):
        return SIGNATURES.get(self.identifier, [])

    def analyze(self, filepath):
        if len(self.signature) > 0:
            with open(filepath, 'rb') as file:
                for sig in self.signature:
                    file.seek(sig.offset)
                    identifier_bytes = file.read(sig.length)
                    if identifier_bytes == sig.signature:
                        return True
                return False
        raise Exception()


class Jpg(MediaType):
    identifier = 'JPG'


class Gif(MediaType):
    identifier = 'GIF'


class Ico(MediaType):
    identifier = 'ICO'


class Tif(MediaType):
    identifier = 'TIF'


class Png(MediaType):
    identifier = 'PNG'


class Mkv(MediaType):
    identifier = 'MKV'


class Bmp(MediaType):
    identifier = 'BMP'


class Avi(MediaType):
    identifier = 'AVI'


class Mp3(MediaType):
    identifier = 'MP3'


class Mp4(MediaType):
    identifier = 'MP4'


MEDIA_TYPES = [
    Jpg,
    Gif,
    Ico,
    Tif,
    Png,
    Mkv,
    Bmp,
    # Avi,
    Mp3,
    Mp4,
]
