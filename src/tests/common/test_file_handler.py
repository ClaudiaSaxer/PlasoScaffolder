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
  name = "testfile"
  suffix = "py"
  file = '{0:s}.{1:s}'.format(name, suffix)


  def testCreateFolder(self):
    """Tests if the creation of a folder works."""
    with tempfile.TemporaryDirectory() as tmpdir:
      new_path = os.path.join(tmpdir,"newfolder")
      self.assertFalse(os.path.exists(new_path))
      creator = FileHandler()
      creator._CreateFolder(new_path)  # pylint: disable=W0212
      actual = os.path.exists(new_path)
    self.assertTrue(actual)

  def testCreateFilePath(self):
    """Tests if the construction of the folder path works."""
    with tempfile.TemporaryDirectory() as tmpdir:
      new_path = os.path.join(tmpdir, "temp")
      path = FileHandler.CreateFilePath(new_path, self.name, self.suffix)
      self.assertEqual(path, os.path.join(new_path, self.file))

  def testCreateFile(self):
    """Tests if the creation of a file none existing beforehand works."""
    with tempfile.TemporaryDirectory() as tmpdir:
      creator = FileHandler()
      file_path = os.path.join(tmpdir,self.file)
      self.assertFalse(os.path.exists(file_path))
      creator.CreateFile(tmpdir, self.name, self.suffix)
      self.assertTrue(os.path.exists(file_path))

  def testCreateFileFromPath(self):
    """Tests if the creation of a file none existing beforhand works."""
    creator = FileHandler()
    with tempfile.TemporaryDirectory() as tmpdir:
      source = os.path.join(tmpdir,self.file)
      self.assertFalse(os.path.exists(source))
      creator.CreateFileFromPath(source)
      self.assertTrue(os.path.exists(source))

  def testCopyFile(self):
    """Tests if the copying of a file none existing beforhand works."""
    expected_content = "this is test content."

    with tempfile.TemporaryDirectory() as tmpdir:
      source = os.path.join(tmpdir, self.file)
      destination = os.path.join(tmpdir,"copy",self.file)

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

    with tempfile.TemporaryDirectory() as tmpdir:
      source = os.path.join(tmpdir,self.file)
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

    with tempfile.TemporaryDirectory() as tmpdir:
      source = os.path.join(tmpdir, self.file)
      creator = FileHandler()
      self.assertFalse(os.path.exists(source))
      creator.AddContent(source, content)
      self.assertTrue(os.path.exists(source))

      with open(source, "r") as f:
        actual = f.read()

    self.assertEqual(expected, actual)


if __name__ == '__main__':
  unittest.main()
