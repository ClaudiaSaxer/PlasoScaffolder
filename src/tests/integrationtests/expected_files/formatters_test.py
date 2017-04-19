#!/usr/bin/python
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
        u'id',
        u'screen_name',
        u'profile_image_url',
        u'profile_banner_url',
        u'profile_link_color_hex_triplet',
        u'name',
        u'location',
        u'structured_location',
        u'description',
        u'url',
        u'url_entities',
        u'bio_entities',
        u'protected',
        u'verified',
        u'following',
        u'device_following',
        u'advertiser_account_type',
        u'statuses_count',
        u'media_count',
        u'favorites_count',
        u'following_count',
        u'followers_count',
        u'followers_count_fast',
        u'followers_count_normal',
        u'could_be_stale',
        u'is_lifeline_institution',
        u'has_collections',
        u'updated_at',
        u'created_date',
        u'is_translator',
        u'has_extended_profile_fields',
        u'extended_profile_fields',
        u'pinned_tweet_id',
        u'business_profile_state',
        u'analytics_type'
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
        u'id',
        u'text',
        u'date',
        u'user_id',
        u'in_reply_to_status_id',
        u'retweeted_status_id',
        u'geotag',
        u'entities',
        u'card',
        u'card_users',
        u'primary_card_type',
        u'card_version',
        u'retweet_count',
        u'favorite_count',
        u'favorited',
        u'updated_at',
        u'extra_scribe_item',
        u'withheld_scope',
        u'withheld_in_countries',
        u'in_reply_to_username',
        u'possibly_sensitive',
        u'is_possibly_sensitive_appealable',
        u'is_lifeline_alert',
        u'is_truncated',
        u'preview_length',
        u'full_text_length',
        u'lang',
        u'supplmental_language',
        u'include_in_profile_timeline',
        u'quoted_status_id',
        u'source'
        ]

    self._TestGetFormatStringAttributeNames(
        event_formatter, expected_attribute_names)


if __name__ == '__main__':
  unittest.main()