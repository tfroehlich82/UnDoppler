# -*- coding: utf-8 -*-

"""
Module Documentation
"""


from .file_extensions import EXTENSIONS
from .signatures import SIGNATURES


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


MEDIA_TYPES = [
    Jpg,
    Gif,
    Ico,
    Tif,
    Png,
    Mkv,
    Bmp,
]
