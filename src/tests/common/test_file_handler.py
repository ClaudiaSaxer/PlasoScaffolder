# -*- coding: utf-8 -*-
"""test class"""
import filecmp
import os
import shutil
import tempfile
import unittest

from plasoscaffolder.common.file_handler import FileHandler


class FileHandlerTest(unittest.TestCase):
  """ Class representing the test case testing the file creator class"""
  path = "temp"
  name = "testfile"
  suffix = "py"
  file = name + "." + suffix
  file_with_dir = path + os.sep + name + "." + suffix

  def tearDown(self):
    if os.path.isfile(self.file):
      os.remove(self.file)
    if os.path.isfile(self.file_with_dir):
      os.remove(self.file_with_dir)
    if os.path.exists(self.path):
      shutil.rmtree(self.path)

  def test_create_folder(self):
    """Tests if the creation of a folder works."""
    self.assertFalse(os.path.exists(self.path))
    creator = FileHandler()
    with tempfile.TemporaryDirectory() as tmpdir:
      creator._create_folder(os.path.join(tmpdir, "t"))  # pylint: disable=W0212
      actual = os.path.exists(os.path.join(tmpdir, "t"))
    self.assertTrue(actual)

  def test_get_folder_path(self):
    """Tests if the construction of the folder path works."""
    path = FileHandler.create_file_path(self.path, self.name, self.suffix)
    self.assertEqual(path, self.file_with_dir)

  def test_create_file(self):
    """Tests if the creation of a file none existing beforehand works."""
    creator = FileHandler()
    self.assertFalse(os.path.exists(self.file_with_dir))
    creator.create_file(self.path, self.name, self.suffix)
    self.assertTrue(os.path.exists(self.file_with_dir))

  def test_create_file_from_path(self):
    """Tests if the creation of a file none existing beforhand works."""
    creator = FileHandler()
    self.assertFalse(os.path.exists(self.file_with_dir))
    creator.create_file_from_path(self.file_with_dir)
    self.assertTrue(os.path.exists(self.file_with_dir))

  def test_copy_file(self):
    """Tests if the copying of a file none existing beforhand works."""
    expected_content = "this is test content."
    source = self.file
    destination = self.file_with_dir

    with open(source, "a") as f:
      f.write(expected_content)

    creator = FileHandler()
    self.assertFalse(os.path.exists(destination))
    creator.copy_file(source, destination)
    self.assertTrue(os.path.exists(destination))
    self.assertTrue(filecmp.cmp(destination, source))

  def test_edit_and_create_file_1(self):
    """Tests if the editing of a file existing works."""
    content = "this is test content. "
    expected = content + content
    source = self.file

    with open(source, "a") as f:
      f.write(content)

    creator = FileHandler()
    self.assertTrue(os.path.exists(source))
    creator.add_content(source, content)
    self.assertTrue(os.path.exists(source))

    with open(source, "r") as f:
      actual = f.read()

    self.assertEqual(expected, actual)

  def test_edit_and_create_file_2(self):
    """Tests if the editing of a file not existing works."""
    content = "this is test content. "
    expected = content
    source = self.file

    creator = FileHandler()
    self.assertFalse(os.path.exists(source))
    creator.add_content(source, content)
    self.assertTrue(os.path.exists(source))

    with open(source, "r") as f:
      actual = f.read()

    self.assertEqual(expected, actual)


if __name__ == '__main__':
  unittest.main()
