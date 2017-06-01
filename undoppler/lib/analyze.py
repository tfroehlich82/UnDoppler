from .media_types import MEDIA_TYPES


def analyze_file(filepath):
    for t in MEDIA_TYPES:
        if t().analyze(filepath):
            return t().identifier
    raise Exception()
