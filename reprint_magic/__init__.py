"""
A module that registers and defines a jupyter ipython magic 
to run and reprint on output the code.
"""
from __future__ import absolute_import

__version__ = "1.0.0"

from .reprint_magic import ReprintMagics

__all__ = ('ReprintMagics', )

def load_ipython_extension(ipython):
    """
    Register the ``%%reprint`` magic.

    This function allows to just run ``%load_ext reprint_magic``
    to activate the ``%%reprint`` cell magic.
    """
    ipython.register_magics(ReprintMagics)