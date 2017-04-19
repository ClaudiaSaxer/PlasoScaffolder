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
    # - x Users events.
    # - x Statuses events.
    
    self.assertEqual(, len(storage_writer.events))


    # Test the first users todo event.
    test_event = storage_writer.events[0]
    expected_timestamp = timelib.Timestamp.CopyFromString(
        u'todo')
    self.assertEqual(test_event.timestamp, expected_timestamp)

    self.assertEqual(
      test_event.timestamp_desc, eventdata.EventTimestamp.CREATION_TIME)

    self.assertEqual(test_event.advertiser_account_type, u'todo')
    self.assertEqual(test_event.analytics_type, u'todo')
    self.assertEqual(test_event.bio_entities, u'todo')
    self.assertEqual(test_event.business_profile_state, u'todo')
    self.assertEqual(test_event.could_be_stale, u'todo')
    self.assertEqual(test_event.created_date, u'todo')
    self.assertEqual(test_event.description, u'todo')
    self.assertEqual(test_event.device_following, u'todo')
    self.assertEqual(test_event.extended_profile_fields, u'todo')
    self.assertEqual(test_event.favorites_count, u'todo')
    self.assertEqual(test_event.followers_count, u'todo')
    self.assertEqual(test_event.followers_count_fast, u'todo')
    self.assertEqual(test_event.followers_count_normal, u'todo')
    self.assertEqual(test_event.following, u'todo')
    self.assertEqual(test_event.following_count, u'todo')
    self.assertEqual(test_event.has_collections, u'todo')
    self.assertEqual(test_event.has_extended_profile_fields, u'todo')
    self.assertEqual(test_event.id, u'todo')
    self.assertEqual(test_event.is_lifeline_institution, u'todo')
    self.assertEqual(test_event.is_translator, u'todo')
    self.assertEqual(test_event.location, u'todo')
    self.assertEqual(test_event.media_count, u'todo')
    self.assertEqual(test_event.name, u'todo')
    self.assertEqual(test_event.pinned_tweet_id, u'todo')
    self.assertEqual(test_event.profile_banner_url, u'todo')
    self.assertEqual(test_event.profile_image_url, u'todo')
    self.assertEqual(test_event.profile_link_color_hex_triplet, u'todo')
    self.assertEqual(test_event.protected, u'todo')
    self.assertEqual(test_event.screen_name, u'todo')
    self.assertEqual(test_event.statuses_count, u'todo')
    self.assertEqual(test_event.structured_location, u'todo')
    self.assertEqual(test_event.updated_at, u'todo')
    self.assertEqual(test_event.url, u'todo')
    self.assertEqual(test_event.url_entities, u'todo')
    self.assertEqual(test_event.verified, u'todo')
    
    expected_description = (u'todo')
    self.assertEqual(test_event.description, expected_description)

    expected_profile_url = ('todo')
    self.assertEqual(test_event.profile_url, expected_profile_url)

    expected_message = ('todo')
    expected_message_short = ('todo')

    self._TestGetMessageStrings(
        test_event, expected_message, expected_message_short)

    # Test the first statuses todo event.
    test_event = storage_writer.events[0]
    expected_timestamp = timelib.Timestamp.CopyFromString(
        u'todo')
    self.assertEqual(test_event.timestamp, expected_timestamp)

    self.assertEqual(
      test_event.timestamp_desc, eventdata.EventTimestamp.CREATION_TIME)

    self.assertEqual(test_event.card, u'todo')
    self.assertEqual(test_event.card_users, u'todo')
    self.assertEqual(test_event.card_version, u'todo')
    self.assertEqual(test_event.date, u'todo')
    self.assertEqual(test_event.entities, u'todo')
    self.assertEqual(test_event.extra_scribe_item, u'todo')
    self.assertEqual(test_event.favorite_count, u'todo')
    self.assertEqual(test_event.favorited, u'todo')
    self.assertEqual(test_event.full_text_length, u'todo')
    self.assertEqual(test_event.geotag, u'todo')
    self.assertEqual(test_event.id, u'todo')
    self.assertEqual(test_event.in_reply_to_status_id, u'todo')
    self.assertEqual(test_event.in_reply_to_username, u'todo')
    self.assertEqual(test_event.include_in_profile_timeline, u'todo')
    self.assertEqual(test_event.is_lifeline_alert, u'todo')
    self.assertEqual(test_event.is_possibly_sensitive_appealable, u'todo')
    self.assertEqual(test_event.is_truncated, u'todo')
    self.assertEqual(test_event.lang, u'todo')
    self.assertEqual(test_event.possibly_sensitive, u'todo')
    self.assertEqual(test_event.preview_length, u'todo')
    self.assertEqual(test_event.primary_card_type, u'todo')
    self.assertEqual(test_event.quoted_status_id, u'todo')
    self.assertEqual(test_event.retweet_count, u'todo')
    self.assertEqual(test_event.retweeted_status_id, u'todo')
    self.assertEqual(test_event.source, u'todo')
    self.assertEqual(test_event.supplmental_language, u'todo')
    self.assertEqual(test_event.text, u'todo')
    self.assertEqual(test_event.updated_at, u'todo')
    self.assertEqual(test_event.user_id, u'todo')
    self.assertEqual(test_event.withheld_in_countries, u'todo')
    self.assertEqual(test_event.withheld_scope, u'todo')
    
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