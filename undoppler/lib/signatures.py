import binascii


class Signature(object):

    def __init__(self, signature, offset=0, length=None):
        self.signature = binascii.unhexlify(str(signature, 'UTF-8').replace(" ", ""))
        self.offset = offset
        self.length = length or len(self.signature)

    def __repr__(self):
        return str(self.signature)


JPG_SIGNATURES = (
    Signature(b'FF D8 FF DB'),
    Signature(b'FF D8 FF E0'),
    Signature(b'FF D8 FF E1'),
)

GIF_SIGNATURES = (
    Signature(b'47 49 46 38 37 61'),
    Signature(b'47 49 46 38 39 61'),
)

ICO_SIGNATURES = (
    Signature(b'00 00 01 00'),
)

TIF_SIGNATURES = (
    Signature(b'49 49 2A 00'),
    Signature(b'4D 4D 00 2A'),
)

PNG_SIGNATURES = (
    Signature(b'89 50 4E 47 0D 0A 1A 0A'),
)

MKV_SIGNATURES = (
    Signature(b'1A 45 DF A3'),
)

BMP_SIGNATURES = (
    Signature(b'42 4D'),
)

AVI_SIGNATURES = (
    b'',  # ToDo
)

MP3_SIGNATURES = (
    Signature(b'FF FB'),
    Signature(b'49 44 33'),
)


MP4_SIGNATURES = (
    Signature(b'00 00 00 1C 66 74 79 70 4D 53 4E 56 01 29 00 46 4D 53 4E 56 6D 70 34 32'),
    Signature(b'00 00 00 18 66 74 79 70 33 67 70 35'),
    Signature(b'00 00 00 18 66 74 79 70 6D 70 34 32'),
)


SIGNATURES = {
    'JPG': JPG_SIGNATURES,
    'GIF': GIF_SIGNATURES,
    'ICO': ICO_SIGNATURES,
    'TIF': TIF_SIGNATURES,
    'PNG': PNG_SIGNATURES,
    'MKV': MKV_SIGNATURES,
    'BMP': BMP_SIGNATURES,
    'AVI': AVI_SIGNATURES,
    'MP3': MP3_SIGNATURES,
    'MP4': MP4_SIGNATURES,
}
