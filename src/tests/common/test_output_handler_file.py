# -*- coding: utf-8 -*-
"""test class"""
import unittest

from plasoscaffolder.common import output_handler_file
from tests.fake import fake_file_handler


class FileOutputHandler(unittest.TestCase):
  """testing the file output handler"""

  def setUp(self):
    self.file_path = "testpath"
    self.output = output_handler_file.OutputHandlerFile(
        self.file_path,
        fake_file_handler.FakeFileHandler)

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
