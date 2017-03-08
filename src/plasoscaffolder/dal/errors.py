# -*- coding: utf-8 -*-
"""This file contains the error classes."""

class Error(Exception):
  """Base error class."""

class BadConfigObject(Error):
  """Raised when the configuration object is of the wrong type."""
