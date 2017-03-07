import unittest

from plasoscaffolder.bll.services.file_creator import *
import datetime
import shutil


class FileHandlerTest(unittest.TestCase):
  path = "temp"
  name = "testfile"
  suffix = "py"


  def test_create_folder(self):
    self.assertFalse(os.path.exists(self.path))
    creator = FileCreator(self.path, self.name, self.suffix)
    creator._create_folder()
    self.assertTrue(os.path.exists(self.path))
    shutil.rmtree(self.path)


  def test_get_folder_path(self):
    path = FileCreator.create_file_path(self.path, self.name, self.suffix)
    self.assertEqual(path, "temp"+os.sep+"testfile.py")

  def test_create_file(self):
    creator = FileCreator(self.path, self.name, self.suffix)
    self.assertFalse(os.path.exists(creator.file_path))
    creator.create_file()
    self.assertTrue(os.path.exists(creator.file_path))
    shutil.rmtree(self.path)


if __name__ == '__main__':
  unittest.main()
