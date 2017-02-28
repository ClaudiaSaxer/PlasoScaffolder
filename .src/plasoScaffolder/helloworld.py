# -*- coding: utf-8 -*-
"""The helloworld test file"""
from plasoScaffolder.lib import errors

class ThisAndThat():
  """class that does nothing"""

  def __init__(self, input_reader=None):
    """Initializes the test class

    Args:
      input_reader: the input reader is to test docstring and sphinx
    """
  def _IamAmAPrivateMethod(self):
    """A private Method

    Raises:
      BadConfigOption: if the options are invalid.
    """
    self.IAmAPublicMethod1()
    raise errors.BadConfigObject("Just some error to test")

  def IAmAPublicMethod1(self):
    """I am useless but i print hello world"""
    print("Hello World")

  def IAmAPublicMethod2(self):
    """I am useless but i print hello world"""
    print("Hello World")
