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

  def testCreateFolder(self):
    """Tests if the creation of a folder works."""
    self.assertFalse(os.path.exists(self.path))
    creator = FileHandler()
    with tempfile.TemporaryDirectory() as tmpdir:
      creator._CreateFolder(os.path.join(tmpdir, "t"))  # pylint: disable=W0212
      actual = os.path.exists(os.path.join(tmpdir, "t"))
    self.assertTrue(actual)

  def testCreateFilePath(self):
    """Tests if the construction of the folder path works."""
    path = FileHandler.CreateFilePath(self.path, self.name, self.suffix)
    self.assertEqual(path, self.file_with_dir)

  def testCreateFile(self):
    """Tests if the creation of a file none existing beforehand works."""
    creator = FileHandler()
    self.assertFalse(os.path.exists(self.file_with_dir))
    creator.CreateFile(self.path, self.name, self.suffix)
    self.assertTrue(os.path.exists(self.file_with_dir))

  def testCreateFileFromPath(self):
    """Tests if the creation of a file none existing beforhand works."""
    creator = FileHandler()
    self.assertFalse(os.path.exists(self.file_with_dir))
    creator.CreateFileFromPath(self.file_with_dir)
    self.assertTrue(os.path.exists(self.file_with_dir))

  def testCopyFile(self):
    """Tests if the copying of a file none existing beforhand works."""
    expected_content = "this is test content."
    source = self.file
    destination = self.file_with_dir

    with open(source, "a") as f:
      f.write(expected_content)

    creator = FileHandler()
    self.assertFalse(os.path.exists(destination))
    creator.CopyFile(source, destination)
    self.assertTrue(os.path.exists(destination))
    self.assertTrue(filecmp.cmp(destination, source))

  def testAddContentIfFileExists(self):
    """Tests if the editing of a file existing works."""
    content = "this is test content. "
    expected = content + content
    source = self.file

    with open(source, "a") as f:
      f.write(content)

    creator = FileHandler()
    self.assertTrue(os.path.exists(source))
    creator.AddContent(source, content)
    self.assertTrue(os.path.exists(source))

    with open(source, "r") as f:
      actual = f.read()

    self.assertEqual(expected, actual)

  def testAddContentIfFileDoesNotExist(self):
    """Tests if the editing of a file not existing works."""
    content = "this is test content. "
    expected = content
    source = self.file

    creator = FileHandler()
    self.assertFalse(os.path.exists(source))
    creator.AddContent(source, content)
    self.assertTrue(os.path.exists(source))

    with open(source, "r") as f:
      actual = f.read()

    self.assertEqual(expected, actual)


if __name__ == '__main__':
  unittest.main()
