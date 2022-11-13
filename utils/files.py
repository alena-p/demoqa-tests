import os

from definitions import ROOT_DIR


def generate_absolute_path(source):
    path = os.path.join(ROOT_DIR, source)
    return path
