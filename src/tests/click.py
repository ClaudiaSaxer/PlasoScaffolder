# -*- coding: utf-8 -*-
"""Tests for click"""
import unittest
from click.testing import CliRunner
from plasoscaffolder.frontend.main import entry_point

class TestClick(unittest.TestCase):
  """Testing a click function"""

  def test(self):
    """blabla"""
    runner = CliRunner()
    result = runner.invoke(entry_point,[--help])
    self.assertEqual(result.exit_code, 0)
    self.assertEqual(result.output, "")

if __name__ == '__main__':
  unittest.main()
