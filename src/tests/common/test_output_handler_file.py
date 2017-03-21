# -*- coding: utf-8 -*-
"""test class"""
import unittest

from plasoscaffolder.common.output_handler_file import OutputHandlerFile
from tests.fake.fake_file_handler import FakeFileHandler


class FileOutputHandler(unittest.TestCase):
  """testing the file output handler"""
  def setUp(self):
    self.file_path = "testpath"
    self.output = OutputHandlerFile(self.file_path, FakeFileHandler)

  def testPromptInfo(self):
    """test prompt info, should raise not implemented error"""
    with self.assertRaises(NotImplementedError):
      self.output.PromptInfo("")

  def test_prompt_error(self):
    """test prompt error, should raise not implemented error"""
    with self.assertRaises(NotImplementedError):
      self.output.PromptError("")

  def testPrintInfo(self):
    """test print info. should return the edited file"""
    actual_file = self.output.PrintInfo("the mighty")
    self.assertEqual(self.file_path, actual_file)

  def testPrintError(self):
    """test print error. should return the edited file"""
    actual_file = self.output.PrintError("the mighty")
    self.assertEqual(self.file_path, actual_file)

  def testConfirm(self):
    """test Confirm, should raise not implemented error"""
    with self.assertRaises(NotImplementedError):
      self.output.Confirm("")
