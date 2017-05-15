import os
import tempfile
import unittest
import pexpect
import sys
import platform
from subprocess import call


class MyTestCase(unittest.TestCase):
  def setUp(self):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    setup_path = os.path.join(os.path.dirname(os.path.dirname(dir_path)), 'setup.py')

    call(["python", setup_path, 'build'])
    call(["python", setup_path, 'install'])

    self.path_question = 'What\'s the path to the plaso project\?\:'
    self.name_question = 'What\'s the name of the plugin\?\:'
    self.name_answer = 'test'
    self.testfile_question = 'What\'s the path to your test file\?\:'
    self.testfile_answer = os.path.join(dir_path, 'twitter_ios.db')
    self.output_question = 'Do you want to have a output example for your SQL Query\? \[Y\/n\]\:'
    self.output_answer = 'n'
    self.sql_question = 'Please write your SQL script for the plugin\:'
    self.sql_answer = 'select * from users'
    self.sql_answer_escaped = 'select \* from users'
    self.sql_answer_2 = 'The SQL query was ok.'
    self.name_row_question = 'Do you want to name the query parse row\: Users \? \[Y\/n\]\:'
    self.name_row_answer = 'Y'
    self.column_question_1 = 'Is the column a time event\? updatedAt \[Y\/n\]\:'
    self.column_answer_1 = 'Y'
    self.column_question_2 = 'Is the column a time event\? createdDate \[Y\/n\]\:'
    self.column_answer_2 = 'Y'
    self.additional_question = 'Enter \(additional\) timestamp events from the query \[columnName,aliasName...\] or \[abort\]\:'
    self.additional_answer = 'abort'
    self.custom_question = 'Does the event Users need customizing\? \[y\/N\]\:'
    self.custom_answer = 'N'
    self.add_question = 'Do you want to add another Query\? \[Y\/n\]\:'
    self.add_answer = 'n'
    self.generate_question = 'Do you want to Generate the files\? \[Y\/n\]\:'
    self.generate_answer = 'Y'

  def test_help(self):
    if platform.system() in ['Linux']:
      message_help = (
        'Usage: plasoscaffolder sqlite [OPTIONS]\r\n\r\n'
        'Options:\r\n  '
        '--path TEXT       The path to plaso\r\n  '
        '--name TEXT       The plugin name\r\n  '
        '--testfile TEXT   The testfile path\r\n  '
        '--sql / --no-sql  The output example flag for the SQL Query for the plugin.\r\n  '
        '--help            Show this message and exit.')

      child = pexpect.spawn('plasoscaffolder sqlite --help')
      child.expect_exact(message_help)

  def test_something(self):
    if platform.system() in ['Linux']:
      with tempfile.TemporaryDirectory() as tmpdir:
        path_answer = tmpdir
        dir_path = os.path.dirname(os.path.realpath(__file__))
        formatter_path = os.path.join(tmpdir,'plaso/formatters/test.py')
        parser_path=os.path.join(tmpdir,"plaso/parsers/sqlite_plugins/test.py")
        formatter_test_path=os.path.join(tmpdir,"tests/formatters/test.py")
        parser_test_path=os.path.join(tmpdir,"tests/parsers/sqlite_plugins/test.py")
        test_data_path=os.path.join(tmpdir,"test_data/test.db")
        parsers_init_path=os.path.join(tmpdir,"plaso/parsers/sqlite_plugins/__init__.py")
        formatter_init_path=os.path.join(tmpdir,"plaso/formatters/__init__.py")


        child = pexpect.spawn('plasoscaffolder sqlite')

        child.expect(self.path_question)
        child.sendline(path_answer)
        child.expect(path_answer)

        child.expect(self.name_question)
        child.sendline(self.name_answer)
        child.expect(self.name_answer)

        child.expect(self.testfile_question)
        child.sendline(self.testfile_answer)
        child.expect(self.testfile_answer)

        child.expect(self.output_question)
        child.sendline(self.output_answer)
        child.expect(self.output_answer)

        child.expect(self.sql_question)
        child.sendline(self.sql_answer)
        child.expect(self.sql_answer_escaped)

        child.expect(self.sql_answer_2)
        child.expect(self.name_row_question)
        child.sendline(self.name_row_answer)
        child.expect(self.name_row_answer)

        child.expect(self.column_question_1)
        child.sendline(self.column_answer_1)
        child.expect(self.column_answer_1)

        child.expect(self.column_question_2)
        child.sendline(self.column_answer_2)
        child.expect(self.column_answer_2)

        child.expect(self.additional_question)
        child.sendline(self.additional_answer)
        child.expect(self.additional_answer)

        child.expect(self.custom_question)
        child.sendline(self.custom_answer)
        child.expect(self.custom_answer)

        child.expect(self.add_question)
        child.sendline(self.add_answer)
        child.expect(self.add_answer)

        child.expect(self.generate_question)
        child.sendline(self.generate_answer)

        child.expect(formatter_path)
        child.expect(parser_path)
        child.expect(formatter_test_path)
        child.expect(parser_test_path)
        child.expect(test_data_path)
        child.expect(parsers_init_path)
        child.expect(formatter_init_path)

        formatter_init = self._ReadFromFile(formatter_init_path)
        formatter = self._ReadFromFile(formatter_path)
        formatter_test = self._ReadFromFile(formatter_test_path)
        parser_init = self._ReadFromFile(parsers_init_path)
        parser = self._ReadFromFile(parser_path)
        parser_test = self._ReadFromFile(parser_test_path)

        #TODO
        """expected_path = tmpdir

        expected_formatter_init = self._ReadFromFile(os.path.join(
          expected_path, 'formatters_init.py'))
        expected_formatter = self._ReadFromFile(
          os.path.join(expected_path, 'formatters.py'))
        expected_formatter_test = self._ReadFromFile(os.path.join(
          expected_path, 'formatters_test.py'))
        expected_parser_init = self._ReadFromFile(
          os.path.join(expected_path, 'parsers_init.py'))
        expected_parser = self._ReadFromFile(
          os.path.join(expected_path, 'parsers.py'))
        expected_parser_test = self._ReadFromFile(
          os.path.join(expected_path, 'parsers_test.py'))"""


  def _ReadFromFile(self, path: str):
    """read from file helper"""
    with open(path, 'r') as f:
      return f.read()


if __name__ == '__main__':
  unittest.main()
