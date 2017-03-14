import unittest
import click
from click.testing import CliRunner
from plasoscaffolder.frontend.main import entry_point


class MyTestCase(unittest.TestCase):
  def test_something(self):
    self.assertEqual(True, False)

  def test_hello_world(self):
    runner = CliRunner()
    result = runner.invoke(entry_point, ['--help'])
    assert result.exit_code == 0
    assert 'Debug mode is on' in result.output
    assert 'Syncing' in result.output
if __name__ == '__main__':
  unittest.main()
