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
        with open(filepath, 'rb') as file:
            file.seek(self.signature.offset)
            identifier_bytes = file.read(self.signature.length)
            if identifier_bytes in self.signature.get_signatures():
                return True
            return False


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
