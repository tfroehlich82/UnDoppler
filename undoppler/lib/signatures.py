import binascii


class Signature(object):

    def __init__(self, signature, offset=0, length=None):
        self.signature = binascii.unhexlify(signature)
        self.offset = offset
        self.length = length or len(self.signature)

    def __repr__(self):
        return str(self.signature)


JPG_SIGNATURES = (
    Signature(b'FFD8FFDB'),
    Signature(b'FFD8FFE0'),
    Signature(b'FFD8FFE1'),
)

GIF_SIGNATURES = (
    Signature(b'474946383761'),
    Signature(b'474946383961'),
)

ICO_SIGNATURES = (
    Signature(b'00000100'),
)

TIF_SIGNATURES = (
    Signature(b'49492A00'),
    Signature(b'4D4D002A'),
)

PNG_SIGNATURES = (
    Signature(b'89504E470D0A1A0A'),
)

MKV_SIGNATURES = (
    Signature(b'1A45DFA3'),
)

BMP_SIGNATURES = [
    Signature(b'424D'),
]

# AVI_SIGNATURES = [
#     b'',  # ToDo
# ]
#
# MP3_SIGNATURES = [
#     b'FFFB',
#     b''
# ]

SIGNATURES = {
    'JPG': JPG_SIGNATURES,
    'GIF': GIF_SIGNATURES,
    'ICO': ICO_SIGNATURES,
    'TIF': TIF_SIGNATURES,
    'PNG': PNG_SIGNATURES,
    'MKV': MKV_SIGNATURES,
    'BMP': BMP_SIGNATURES,
}
