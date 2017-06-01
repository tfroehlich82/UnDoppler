import binascii
from .file_extensions import EXTENSIONS


class Signature(object):
    name = None
    offset = 0
    length = 0
    signatures = []
    extensions = None

    def __init__(self, name, offset=0, length=0, signatures=None):
        if signatures is None:
            signatures = []
        self.name = name
        self.offset = offset
        self.length = length
        self.extensions = EXTENSIONS.get(self.name, [])
        for sig in signatures:
            self.signatures.append(binascii.unhexlify(sig))

    def get_signatures(self):
        return self.signatures

    def __repr__(self):
        return "%s: %s" % (self.name, self.get_signatures())


JPG_SIGNATURES = [
    b'FFD8FFDB',
    b'FFD8FFE0',
    b'FFD8FFE1',
]

GIF_SIGNATURES = [
    b'474946383761',
    b'474946383961',
]

ICO_SIGNATURES = [
    b'00000100',
]

TIF_SIGNATURES = [
    b'49492A00',
    b'4D4D002A',
]

PNG_SIGNATURES = [
    b'89504E470D0A1A0A',
]

SIGNATURES = {
    'jpg': Signature('jpg', 0, 4, JPG_SIGNATURES),
    'gif': Signature('gif', 0, 6, GIF_SIGNATURES),
    'ico': Signature('ico', 0, 4, ICO_SIGNATURES),
    'tif': Signature('tif', 0, 4, TIF_SIGNATURES),
    'png': Signature('png', 0, 8, PNG_SIGNATURES),
}
