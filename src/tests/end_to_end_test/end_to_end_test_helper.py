# -*- coding: utf-8 -*-
"""class for end to end test helper"""
import os

from tests.test_helper import path_helper


class EndToEndTestHelper(object):
  DIR_PATH = os.path.dirname(os.path.realpath(__file__))
  DATABASE_PATH = path_helper.TestDatabasePath()
  MAIN_PATH = os.path.join(
      os.path.dirname(os.path.dirname(DIR_PATH)), 'plasoscaffolder',
      'frontend', 'main.py')
  PATH_QUESTION = 'What\'s the path to the plaso project\?\:'
  PATH_WRONG_QUESTION = 'Folder does not exists. Enter correct one\:'
  NAME_QUESTION = 'What\'s the name of the plugin\?\:'
  NAME_QUESTION_NOT_VALID = ('Plugin is not in a valid format\. Choose new '
                             'Name \[plugin\_name\_\.\.\.\]\:')

  NAME_ANSWER = 'test'
  TESTFILE_QUESTION = 'What\'s the path to your test file\?\:'
  TESTFILE_QUESTION_NOT_FOUND = "File does not exists\. Choose another\.\:"
  TESTFILE_QUESTION_INVALID = 'Unable to open the database file\. Choose ' \
                              'another\.\:'
  TESTFILE_ANSWER = os.path.join(DATABASE_PATH, 'twitter_ios.db')
  TESTFILE_ANSWER_ERROR = os.path.join(DATABASE_PATH, 'twitter_ios_error.db')
  TESTFILE_ANSWER_NOT_FOUND = os.path.join(DATABASE_PATH, 'does_not_exist')

  OUTPUT_QUESTION = ('Do you want to have a output example for your '
                     'SQL Query\? \[Y\/n\]\:')
  OUTPUT_ANSWER_NO = 'n'
  OUTPUT_ANSWER_YES = 'y'
  OUTPUT_ADD_QUESTION = 'Do you want to add this query? \[Y\/n\]\:'
  OUTPUT_ADD_ANSWER_NO = 'n'
  OUTPUT_ADD_ANSWER_YES = 'y'
  OUTPUT_EXAMPLE_FIRST_ROW = 'Your query output could look like this\.'
  OUTPUT_USERS_ID_NAME_EXAMPLE_HEADER = '\[\'id\'\, \'name\'\]'
  OUTPUT_USERS_ID_EXAMPLE_FIRST_ROW = '(5402612\, \'BBC Breaking News\'\)'
  OUTPUT_USERS_ID_EXAMPLE_SECOND_ROW = '\(13334762\, \'GitHub\'\)'
  OUTPUT_USERS_ID_EXAMPLE_THIRD_ROW = '\(14388264\, \'Tom Pohl\'\)'

  SQL_QUESTION = 'Please write your SQL script for the plugin\:'
  SQL_QUESTION_WITH_ABORT = (
    'Please write your SQL script for the plugin \[\'abort\' to continue\]\:')
  SQL_ANSWER = 'select * from users'
  SQL_ANSWER_ESCAPED = 'select \* from users'
  SQL_ANSWER_2 = 'select * from statuses'
  SQL_ANSWER_ESCAPED_2 = 'select \* from statuses'
  SQL_ANSWER_OK = 'The SQL query was ok.'
  NAME_ROW_QUESTION = ('Do you want to name the query parse row\: '
                       'Users \? \[Y\/n\]\:')
  NAME_ROW_ANSWER_YES = 'Y'
  NAME_ROW_ANSWER_NO = 'N'
  COLUMN_ANSWER_YES = 'Y'
  COLUMN_ANSWER_NO = 'N'
  COLUMN_QUESTION_CREATED_DATE = ('Is the column a time event\? createdDate \['
                                  'Y\/n\]\:')
  COLUMN_QUESTION_UPDATED_AT = ('Is the column a time event\? updatedAt \['
                                'Y\/n\]\:')
  COLUMN_QUESTION_DATE = ('Is the column a time event\? date \['
                           'Y\/n\]\:')
  COLUMN_QUESTION_PROFILE_TIMELINE = (
    'Is the column a time event\? includeInProfileTimeline \['
    'Y\/n\]\:')
  ADDITIONAL_TIMESTAMP = ('Enter \(additional\) timestamp events from '
                          'the query \[columnName,aliasName...\] or \['
                          'abort\]\:')
  ADDITIONAL_TIMESTAMP_ABORT = 'abort'
  CUSTOM_QUESTION = ('Does the event Users need customizing\? \['
                     'y\/N\]\:')
  CUSTOM_ANSWER_NO = 'N'
  ADD_QUESTION = 'Do you want to add another Query\? \[Y\/n\]\:'
  ADD_ANSWER_NO = 'n'
  ADD_ANSWER_YES = 'Y'
  GENERATE_QUESTION = 'Do you want to Generate the files\? \[Y\/n\]\:'
  GENERATE_ANSWER_YES = 'Y'
  GENERATE_ANSWER_NO = 'N'

  def __init__(self, dir: str):
    """Initializes the test helper
    
    Args:
      dir (str): the path of the directory of plaso 
    """
    self.formatter_path = os.path.join(dir, 'plaso/formatters/test.py')
    self.parser_path = os.path.join(dir,
                                    "plaso/parsers/sqlite_plugins/test.py")
    self.formatter_test_path = os.path.join(dir, "tests/formatters/test.py")
    self.parser_test_path = os.path.join(dir,
                                         "tests/parsers/sqlite_plugins/test.py")
    self.test_data_path = os.path.join(dir, "test_data/test.db")
    self.parsers_init_path = os.path.join(dir,
                                          "plaso/parsers/sqlite_plugins/__init__.py")
    self.formatter_init_path = os.path.join(dir,
                                            "plaso/formatters/__init__.py")

  def ReadFromFile(self, path: str):
    """read from file helper"""
    with open(path, 'r') as f:
      return f.read()
