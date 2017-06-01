from .signatures import SIGNATURES


def is_jpeg(filepath):
    with open(filepath, 'rb') as file:
        first_four_bytes = file.read(4)

        if first_four_bytes in SIGNATURES.get('jpg')():
            return True
        return False
