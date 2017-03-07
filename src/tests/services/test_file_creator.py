import unittest

from plasoscaffolder.bll.services.file_creator import *
import shutil


class FileCreatorTest(unittest.TestCase):
  path = "temp"
  name = "testfile"
  suffix = "py"

  def test_create_folder(self):
    self.assertFalse(os.path.exists(self.path))
    creator = FileCreator()
    creator._create_folder(self.path)
    self.assertTrue(os.path.exists(self.path))
    shutil.rmtree(self.path)

  def test_get_folder_path(self):
    path = FileCreator.create_file_path(self.path, self.name, self.suffix)
    self.assertEqual(path, self.path + os.sep + self.name + "." + self.suffix)

  def test_create_file(self):
    creator = FileCreator()
    self.assertFalse(
      os.path.exists(self.path + os.sep + self.name + "." + self.suffix))
    creator.create_file(self.path, self.name, self.suffix)
    self.assertTrue(
      os.path.exists(self.path + os.sep + self.name + "." + self.suffix))
    shutil.rmtree(self.path)

  def test_create_file_from_path(self):
    creator = FileCreator()
    self.assertFalse(
      os.path.exists(self.path + os.sep + self.name + "." + self.suffix))
    creator.create_file_from_path(
      self.path + os.sep + self.name + "." + self.suffix)
    self.assertTrue(
      os.path.exists(self.path + os.sep + self.name + "." + self.suffix))
    shutil.rmtree(self.path)


if __name__ == '__main__':
  unittest.main()
