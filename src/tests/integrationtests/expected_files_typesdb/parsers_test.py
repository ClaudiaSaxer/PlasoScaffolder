# -*- coding: utf-8 -*-
"""Tests for the plugin plugin."""
import unittest

from plaso.lib import eventdata
from plaso.lib import timelib
from plaso.parsers.sqlite_plugins import the_plugin

from tests import test_lib as shared_test_lib
from tests.parsers.sqlite_plugins import test_lib


class ThePluginTest(test_lib.SQLitePluginTestCase):
  """Tests for the plugin database plugin."""

  @shared_test_lib.skipUnlessHasTestFile([u'the_plugin.db'])
  def testProcess(self):
    """Test the Process function on a The Plugin file."""
    plugin_object = the_plugin.ThePluginPlugin()
    storage_writer = self._ParseDatabaseFileWithPlugin(
        [u'the_plugin.db'], plugin_object)

    # We should have  events in total.
    # - x blobtypes events.
    # - x integertypes events.
    # - x numerictypes events.
    # - x realtypes events.
    # - x texttypes events.
    # - x nodata events.
    
    self.assertEqual(, len(storage_writer.events))


    # Test the first blobtypes todo event.
    test_event = storage_writer.events[0]
    expected_timestamp = timelib.Timestamp.CopyFromString(
        u'todo')
    self.assertEqual(test_event.timestamp, expected_timestamp)

    self.assertEqual(
      test_event.timestamp_desc, eventdata.EventTimestamp.CREATION_TIME)

    self.assertEqual(test_event.blobval, u'todo')
    
    expected_description = (u'todo')
    self.assertEqual(test_event.description, expected_description)

    expected_profile_url = ('todo')
    self.assertEqual(test_event.profile_url, expected_profile_url)

    expected_message = ('todo')
    expected_message_short = ('todo')

    self._TestGetMessageStrings(
        test_event, expected_message, expected_message_short)

    # Test the first integertypes todo event.
    test_event = storage_writer.events[0]
    expected_timestamp = timelib.Timestamp.CopyFromString(
        u'todo')
    self.assertEqual(test_event.timestamp, expected_timestamp)

    self.assertEqual(
      test_event.timestamp_desc, eventdata.EventTimestamp.CREATION_TIME)

    self.assertEqual(test_event.bigintval, u'todo')
    self.assertEqual(test_event.int2val, u'todo')
    self.assertEqual(test_event.int8val, u'todo')
    self.assertEqual(test_event.integerval, u'todo')
    self.assertEqual(test_event.intval, u'todo')
    self.assertEqual(test_event.mediumintval, u'todo')
    self.assertEqual(test_event.smallintval, u'todo')
    self.assertEqual(test_event.tinyintval, u'todo')
    self.assertEqual(test_event.unsignedbigintval, u'todo')
    
    expected_description = (u'todo')
    self.assertEqual(test_event.description, expected_description)

    expected_profile_url = ('todo')
    self.assertEqual(test_event.profile_url, expected_profile_url)

    expected_message = ('todo')
    expected_message_short = ('todo')

    self._TestGetMessageStrings(
        test_event, expected_message, expected_message_short)

    # Test the first numerictypes todo event.
    test_event = storage_writer.events[0]
    expected_timestamp = timelib.Timestamp.CopyFromString(
        u'todo')
    self.assertEqual(test_event.timestamp, expected_timestamp)

    self.assertEqual(
      test_event.timestamp_desc, eventdata.EventTimestamp.CREATION_TIME)

    self.assertEqual(test_event.booleanval, u'todo')
    self.assertEqual(test_event.datetimeval, u'todo')
    self.assertEqual(test_event.dateval, u'todo')
    self.assertEqual(test_event.decimalval, u'todo')
    self.assertEqual(test_event.numericval, u'todo')
    
    expected_description = (u'todo')
    self.assertEqual(test_event.description, expected_description)

    expected_profile_url = ('todo')
    self.assertEqual(test_event.profile_url, expected_profile_url)

    expected_message = ('todo')
    expected_message_short = ('todo')

    self._TestGetMessageStrings(
        test_event, expected_message, expected_message_short)

    # Test the first realtypes todo event.
    test_event = storage_writer.events[0]
    expected_timestamp = timelib.Timestamp.CopyFromString(
        u'todo')
    self.assertEqual(test_event.timestamp, expected_timestamp)

    self.assertEqual(
      test_event.timestamp_desc, eventdata.EventTimestamp.CREATION_TIME)

    self.assertEqual(test_event.doubleprecesionval, u'todo')
    self.assertEqual(test_event.doubleval, u'todo')
    self.assertEqual(test_event.floatval, u'todo')
    self.assertEqual(test_event.realval, u'todo')
    
    expected_description = (u'todo')
    self.assertEqual(test_event.description, expected_description)

    expected_profile_url = ('todo')
    self.assertEqual(test_event.profile_url, expected_profile_url)

    expected_message = ('todo')
    expected_message_short = ('todo')

    self._TestGetMessageStrings(
        test_event, expected_message, expected_message_short)

    # Test the first texttypes todo event.
    test_event = storage_writer.events[0]
    expected_timestamp = timelib.Timestamp.CopyFromString(
        u'todo')
    self.assertEqual(test_event.timestamp, expected_timestamp)

    self.assertEqual(
      test_event.timestamp_desc, eventdata.EventTimestamp.CREATION_TIME)

    self.assertEqual(test_event.characterval, u'todo')
    self.assertEqual(test_event.clobval, u'todo')
    self.assertEqual(test_event.nativecharacterval, u'todo')
    self.assertEqual(test_event.ncharval, u'todo')
    self.assertEqual(test_event.nvarchar_val, u'todo')
    self.assertEqual(test_event.textval, u'todo')
    self.assertEqual(test_event.varcharval, u'todo')
    self.assertEqual(test_event.varyingcharacterval, u'todo')
    
    expected_description = (u'todo')
    self.assertEqual(test_event.description, expected_description)

    expected_profile_url = ('todo')
    self.assertEqual(test_event.profile_url, expected_profile_url)

    expected_message = ('todo')
    expected_message_short = ('todo')

    self._TestGetMessageStrings(
        test_event, expected_message, expected_message_short)

    # Test the first nodata todo event.
    test_event = storage_writer.events[0]
    expected_timestamp = timelib.Timestamp.CopyFromString(
        u'todo')
    self.assertEqual(test_event.timestamp, expected_timestamp)

    self.assertEqual(
      test_event.timestamp_desc, eventdata.EventTimestamp.CREATION_TIME)

    self.assertEqual(test_event.bigintval, u'todo')
    self.assertEqual(test_event.blobval, u'todo')
    self.assertEqual(test_event.booleanval, u'todo')
    self.assertEqual(test_event.characterval, u'todo')
    self.assertEqual(test_event.clobval, u'todo')
    self.assertEqual(test_event.datetimeval, u'todo')
    self.assertEqual(test_event.dateval, u'todo')
    self.assertEqual(test_event.decimalval, u'todo')
    self.assertEqual(test_event.doubleprecisionval, u'todo')
    self.assertEqual(test_event.doubleval, u'todo')
    self.assertEqual(test_event.floatval, u'todo')
    self.assertEqual(test_event.int2val, u'todo')
    self.assertEqual(test_event.int8val, u'todo')
    self.assertEqual(test_event.integerval, u'todo')
    self.assertEqual(test_event.intval, u'todo')
    self.assertEqual(test_event.mediuintval, u'todo')
    self.assertEqual(test_event.nativecharacterval, u'todo')
    self.assertEqual(test_event.ncharval, u'todo')
    self.assertEqual(test_event.numericval, u'todo')
    self.assertEqual(test_event.nvarcharval, u'todo')
    self.assertEqual(test_event.realval, u'todo')
    self.assertEqual(test_event.smallintval, u'todo')
    self.assertEqual(test_event.textval, u'todo')
    self.assertEqual(test_event.tinyintval, u'todo')
    self.assertEqual(test_event.unsignedbigintval, u'todo')
    self.assertEqual(test_event.varcharval, u'todo')
    self.assertEqual(test_event.varyingcharacterval, u'todo')
    
    expected_description = (u'todo')
    self.assertEqual(test_event.description, expected_description)

    expected_profile_url = ('todo')
    self.assertEqual(test_event.profile_url, expected_profile_url)

    expected_message = ('todo')
    expected_message_short = ('todo')

    self._TestGetMessageStrings(
        test_event, expected_message, expected_message_short)


if __name__ == '__main__':
  unittest.main()