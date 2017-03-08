"""Module representing the sqlite plugin generator"""
from plasoscaffolder.bll.services.file_handler import *
from plasoscaffolder.bll.services.sqlite_plugin_helper import *

def generate_sqlite_plugin(path, name, database):
  creator = FileHandler()

  file = creator.create_file_from_path
  copy = creator.copy_file

  print("generate " + file(formatter_file_path(path, name)))
  print("generate " + file(parser_file_path(path, name)))
  print("generate " + file(parser_test_file_path(path, name)))
  print("generate " + file(formatter_test_file_path(path, name)))
  print("copy " + copy(database, database_path(path, name)))
