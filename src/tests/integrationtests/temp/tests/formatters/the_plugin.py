# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for The Plugin event formatter."""

import unittest

from plaso.formatters import the_plugin
from tests.formatters import test_lib

class ThePluginUsersFormatterTest(test_lib.EventFormatterTestCase):
  """Tests the TThe Plugin users event formatter."""

  def testInitialization(self):
    """Tests the initialization."""
    event_formatter = the_plugin.ThePluginUsersFormatter()
    self.assertIsNotNone(event_formatter)

  def testGetFormatStringAttributeNames(self):
    """Tests the GetFormatStringAttributeNames function."""
    event_formatter = the_plugin.ThePluginusersFormatter()

    expected_attribute_names = [
        u'advertiser_account_type',
        u'analytics_type',
        u'bio_entities',
        u'business_profile_state',
        u'could_be_stale',
        u'created_date',
        u'description',
        u'device_following',
        u'extended_profile_fields',
        u'favorites_count',
        u'followers_count',
        u'followers_count_fast',
        u'followers_count_normal',
        u'following',
        u'following_count',
        u'has_collections',
        u'has_extended_profile_fields',
        u'id',
        u'is_lifeline_institution',
        u'is_translator',
        u'location',
        u'media_count',
        u'name',
        u'pinned_tweet_id',
        u'profile_banner_url',
        u'profile_image_url',
        u'profile_link_color_hex_triplet',
        u'protected',
        u'screen_name',
        u'statuses_count',
        u'structured_location',
        u'updated_at',
        u'url',
        u'url_entities',
        u'verified'
        ]

    self._TestGetFormatStringAttributeNames(
        event_formatter, expected_attribute_names)

class ThePluginStatusesFormatterTest(test_lib.EventFormatterTestCase):
  """Tests the TThe Plugin statuses event formatter."""

  def testInitialization(self):
    """Tests the initialization."""
    event_formatter = the_plugin.ThePluginStatusesFormatter()
    self.assertIsNotNone(event_formatter)

  def testGetFormatStringAttributeNames(self):
    """Tests the GetFormatStringAttributeNames function."""
    event_formatter = the_plugin.ThePluginstatusesFormatter()

    expected_attribute_names = [
        u'card',
        u'card_users',
        u'card_version',
        u'date',
        u'entities',
        u'extra_scribe_item',
        u'favorite_count',
        u'favorited',
        u'full_text_length',
        u'geotag',
        u'id',
        u'in_reply_to_status_id',
        u'in_reply_to_username',
        u'include_in_profile_timeline',
        u'is_lifeline_alert',
        u'is_possibly_sensitive_appealable',
        u'is_truncated',
        u'lang',
        u'possibly_sensitive',
        u'preview_length',
        u'primary_card_type',
        u'quoted_status_id',
        u'retweet_count',
        u'retweeted_status_id',
        u'source',
        u'supplmental_language',
        u'text',
        u'updated_at',
        u'user_id',
        u'withheld_in_countries',
        u'withheld_scope'
        ]

    self._TestGetFormatStringAttributeNames(
        event_formatter, expected_attribute_names)


if __name__ == '__main__':
  unittest.main()