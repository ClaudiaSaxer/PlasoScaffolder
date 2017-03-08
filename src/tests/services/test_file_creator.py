import unittest

from plasoscaffolder.bll.services.file_creator import *
import shutil
import filecmp


class FileCreatorTest(unittest.TestCase):
  """ Class representing the test case testing the file creator class"""
  path = "temp"
  name = "testfile"
  suffix = "py"

  def test_create_folder(self):
    """Tests if the creation of a folder works."""
    self.assertFalse(os.path.exists(self.path))
    creator = FileCreator()
    creator._create_folder(self.path)
    self.assertTrue(os.path.exists(self.path))
    shutil.rmtree(self.path)

  def test_get_folder_path(self):
    """Tests if the construction of the folder path works."""
    path = FileCreator.create_file_path(self.path, self.name, self.suffix)
    self.assertEqual(path, self.path + os.sep + self.name + "." + self.suffix)

  def test_create_file(self):
    """Tests if the creation of a file none existing beforehand works."""
    creator = FileCreator()
    self.assertFalse(
      os.path.exists(self.path + os.sep + self.name + "." + self.suffix))
    creator.create_file(self.path, self.name, self.suffix)
    self.assertTrue(
      os.path.exists(self.path + os.sep + self.name + "." + self.suffix))
    shutil.rmtree(self.path)

  def test_create_file_from_path(self):
    """Tests if the creation of a file none existing beforhand works."""
    creator = FileCreator()
    self.assertFalse(
      os.path.exists(self.path + os.sep + self.name + "." + self.suffix))
    creator.create_file_from_path(
      self.path + os.sep + self.name + "." + self.suffix)
    self.assertTrue(
      os.path.exists(self.path + os.sep + self.name + "." + self.suffix))
    shutil.rmtree(self.path)

  def test_copy_file(self):
    """Tests if the copying of a file none existing beforhand works."""
    expected_content = "this is test content."
    source = self.name
    destination = self.path + os.sep + self.name + "." + self.suffix

    with open(source, "a+") as f:
      f.write(expected_content)

    creator = FileCreator()
    self.assertFalse(os.path.exists(destination))
    creator.copy_file(source, destination)
    self.assertTrue(os.path.exists(destination))
    self.assertTrue(filecmp.cmp(destination, source))

    shutil.rmtree(self.path)
    os.remove(source)


if __name__ == '__main__':
  unittest.main()
