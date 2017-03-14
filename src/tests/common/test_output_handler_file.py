import unittest

from plasoscaffolder.common.output_handler_file import OutputHandlerFile
from tests.fake.fake_file_handler import FakeFileHandler


class FileOutputHandler(unittest.TestCase):
  def setUp(self):
    self.file_path = "testpath"
    self.output = OutputHandlerFile(self.file_path, FakeFileHandler)

  def test_prompt_info(self):
    """test prompt info, should raise not implemented error"""
    with self.assertRaises(NotImplementedError):
      self.output.prompt_info("")

  def test_prompt_error(self):
    """test prompt error, should raise not implemented error"""
    with self.assertRaises(NotImplementedError):
      self.output.prompt_error("")

  def test_print_info(self):
    """test print info. should return the edited file"""
    actual_file = self.output.print_info("the mighty")
    self.assertEqual(self.file_path, actual_file)

  def test_print_error(self):
    """test print error. should return the edited file"""
    actual_file = self.output.print_error("the mighty")
    self.assertEqual(self.file_path, actual_file)

  def test_confirm(self):
    """test confirm, should raise not implemented error"""
    with self.assertRaises(NotImplementedError):
      self.output.confirm("")
