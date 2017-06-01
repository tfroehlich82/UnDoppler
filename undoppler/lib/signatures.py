import binascii


class Signature(object):

    def __init__(self, name, offset=0, length=0, signatures=None):
        self.signatures = []
        if signatures is None:
            signatures = []
        self.name = name
        self.offset = offset
        self.length = length
        # self.extensions = EXTENSIONS.get(self.name, [])
        for sig in signatures:
            self.signatures.append(binascii.unhexlify(sig))

    def get_signatures(self):
        return self.signatures

    def __repr__(self):
        return "%s: %s" % (self.name, self.get_signatures())

    def __call__(self, *args, **kwargs):
        return self.get_signatures()


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

MKV_SIGNATURES = [
    b'1A45DFA3',
]

BMP_SIGNATURES = [
    b'424D',
]

AVI_SIGNATURES = [
    b'',  # ToDo
]

MP3_SIGNATURES = [
    b'FFFB',
    b''
]

SIGNATURES = {
    'JPG': Signature('jpg', 0, 4, JPG_SIGNATURES),
    'GIF': Signature('gif', 0, 6, GIF_SIGNATURES),
    'ICO': Signature('ico', 0, 4, ICO_SIGNATURES),
    'TIF': Signature('tif', 0, 4, TIF_SIGNATURES),
    'PNG': Signature('png', 0, 8, PNG_SIGNATURES),
    'MKV': Signature('mkv', 0, 4, MKV_SIGNATURES),
    'BMP': Signature('bmp', 0, 2, BMP_SIGNATURES),
    'AVI': Signature('avi', 0, 2, AVI_SIGNATURES),  # ToDo
}
