# -*- coding: utf-8 -*-
__version__ = '1.0.0'

VERSION_DEV = True
VERSION_DATE = '20170413'


def GetVersion():
  """Retrieves the version.

  Returns:
    A string containing the version.
  """
  if VERSION_DEV:
    return u'{0:s}_{1:s}'.format(__version__, VERSION_DATE)

  return __version__
