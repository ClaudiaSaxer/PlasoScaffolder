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
    storage_writer = self._ParseDatabaseFileWithPlugin([u'the_plugin.db'],
                                                       plugin_object)

    # We should have 184 events in total.
    # - 25 Users createdDate events.
    # - 25 Users updatedAt events.
    # - 67 Statuses date events.
    # - 67 Statuses updatedAt events.

    self.assertEqual(184, len(storage_writer.events))

    # Test the first users updatedAt event.
    position = 0  #TODO
    test_event = storage_writer.events[position]
    expected_timestamp = timelib.Timestamp.CopyFromString(u'1449070544.333328')
    self.assertEqual(test_event.timestamp, expected_timestamp)

    self.assertEqual(test_event.timestamp_desc,
                     eventdata.EventTimestamp.CREATION_TIME)
    self.assertEqual(test_event.advertiser_account_type, u'0')
    self.assertEqual(test_event.analytics_type, u'0')
    self.assertEqual(test_event.bio_entities, u'None')
    self.assertEqual(test_event.business_profile_state, u'0')
    self.assertEqual(test_event.could_be_stale, u'0')
    expected_description = (
        u'Breaking news alerts and updates from the BBC. For news, features, analysis follow @BBCWorld (international) or @BBCNews (UK). Latest sport news @BBCSport.'
    )
    self.assertEqual(test_event.description, expected_description)
    self.assertEqual(test_event.device_following, u'0')
    self.assertEqual(test_event.extended_profile_fields, u'None')
    self.assertEqual(test_event.favorites_count, u'0')
    self.assertEqual(test_event.followers_count, u'19466932')
    self.assertEqual(test_event.followers_count_fast, u'0')
    self.assertEqual(test_event.followers_count_normal, u'0')
    self.assertEqual(test_event.following, u'0')
    self.assertEqual(test_event.following_count, u'3')
    self.assertEqual(test_event.has_collections, u'0')
    self.assertEqual(test_event.has_extended_profile_fields, u'0')
    self.assertEqual(test_event.id, u'5402612')
    self.assertEqual(test_event.is_lifeline_institution, u'0')
    self.assertEqual(test_event.is_translator, u'0')
    self.assertEqual(test_event.location, u'London, UK')
    self.assertEqual(test_event.media_count, u'None')
    self.assertEqual(test_event.name, u'BBC Breaking News')
    self.assertEqual(test_event.pinned_tweet_id, u'None')
    expected_profile_banner_url = (
        u'https://pbs.twimg.com/profile_banners/5402612/1398336837')
    self.assertEqual(test_event.profile_banner_url, expected_profile_banner_url)
    expected_profile_image_url = (
        u'https://pbs.twimg.com/profile_images/460740982498013184/wIPwMwru_normal.png'
    )
    self.assertEqual(test_event.profile_image_url, expected_profile_image_url)
    self.assertEqual(test_event.profile_link_color_hex_triplet, u'2052731')
    self.assertEqual(test_event.protected, u'0')
    self.assertEqual(test_event.screen_name, u'BBCBreaking')
    self.assertEqual(test_event.statuses_count, u'26697')
    self.assertEqual(test_event.structured_location, u'None')
    self.assertEqual(test_event.url, u'http://www.bbc.co.uk/news')
    self.assertEqual(test_event.url_entities, u'None')
    self.assertEqual(test_event.verified, u'1')

    expected_message = (
        u'Id: 5402612 Screen Name: BBCBreaking Profile Image Url: https://pbs.twimg.com/profile_images/460740982498013184/wIPwMwru_normal.png Profile Banner Url: https://pbs.twimg.com/profile_banners/5402612/1398336837 Profile Link Color Hex Triplet: 2052731 Name: BBC Breaking News Location: London, UK Structured Location: None Description: Breaking news alerts and updates from the BBC. For news, features, analysis follow @BBCWorld (international) or @BBCNews (UK). Latest sport news @BBCSport. Url: http://www.bbc.co.uk/news Url Entities: None Bio Entities: None Protected: 0 Verified: 1 Following: 0 Device Following: 0 Advertiser Account Type: 0 Statuses Count: 26697 Media Count: None Favorites Count: 0 Following Count: 3 Followers Count: 19466932 Followers Count Fast: 0 Followers Count Normal: 0 Could Be Stale: 0 Is Lifeline Institution: 0 Has Collections: 0 Is Translator: 0 Has Extended Profile Fields: 0 Extended Profile Fields: None Pinned Tweet Id: None Business Profile State: 0 Analytics Type: 0'
    )
    expected_message_short = (
        u'Id: 5402612 Screen Name: BBCBreaking Profile Image Url: https://pbs.twimg.com...'
    )

    self._TestGetMessageStrings(test_event, expected_message,
                                expected_message_short)

    # Test the first users createdDate event.
    position = 0  #TODO
    test_event = storage_writer.events[position]
    expected_timestamp = timelib.Timestamp.CopyFromString(u'1177252957.0')
    self.assertEqual(test_event.timestamp, expected_timestamp)

    self.assertEqual(test_event.timestamp_desc,
                     eventdata.EventTimestamp.CREATION_TIME)
    self.assertEqual(test_event.advertiser_account_type, u'0')
    self.assertEqual(test_event.analytics_type, u'0')
    self.assertEqual(test_event.bio_entities, u'b&#39;{}&#39;')
    self.assertEqual(test_event.business_profile_state, u'0')
    self.assertEqual(test_event.could_be_stale, u'0')
    self.assertEqual(test_event.description, u'How people build software')
    self.assertEqual(test_event.device_following, u'0')
    self.assertEqual(test_event.extended_profile_fields, u'None')
    self.assertEqual(test_event.favorites_count, u'155')
    self.assertEqual(test_event.followers_count, u'742086')
    self.assertEqual(test_event.followers_count_fast, u'0')
    self.assertEqual(test_event.followers_count_normal, u'742086')
    self.assertEqual(test_event.following, u'0')
    self.assertEqual(test_event.following_count, u'172')
    self.assertEqual(test_event.has_collections, u'0')
    self.assertEqual(test_event.has_extended_profile_fields, u'0')
    self.assertEqual(test_event.id, u'13334762')
    self.assertEqual(test_event.is_lifeline_institution, u'0')
    self.assertEqual(test_event.is_translator, u'0')
    self.assertEqual(test_event.location, u'San Francisco, CA')
    self.assertEqual(test_event.media_count, u'33')
    self.assertEqual(test_event.name, u'GitHub')
    self.assertEqual(test_event.pinned_tweet_id, u'None')
    expected_profile_banner_url = (
        u'https://pbs.twimg.com/profile_banners/13334762/1415719104')
    self.assertEqual(test_event.profile_banner_url, expected_profile_banner_url)
    expected_profile_image_url = (
        u'https://pbs.twimg.com/profile_images/616309728688238592/pBeeJQDQ_normal.png'
    )
    self.assertEqual(test_event.profile_image_url, expected_profile_image_url)
    self.assertEqual(test_event.profile_link_color_hex_triplet, u'255')
    self.assertEqual(test_event.protected, u'0')
    self.assertEqual(test_event.screen_name, u'github')
    self.assertEqual(test_event.statuses_count, u'3120')
    self.assertEqual(test_event.structured_location, u'None')
    self.assertEqual(test_event.url, u'https://t.co/FoKGHcCyJJ')
    expected_url_entities = (
        u'b&#39;{&#34;urls&#34;:[{&#34;url&#34;:&#34;https:\\/\\/t.co\\/FoKGHcCyJJ&#34;,&#34;rangeInDisplay.length&#34;:0,&#34;displayURL&#34;:&#34;github.com&#34;,&#34;rangeInDisplay.location&#34;:0,&#34;expandedURL&#34;:&#34;https:\\/\\/github.com&#34;,&#34;range.location&#34;:0,&#34;range.length&#34;:23}]}&#39;'
    )
    self.assertEqual(test_event.url_entities, expected_url_entities)
    self.assertEqual(test_event.verified, u'1')

    expected_message = (
        u'Id: 13334762 Screen Name: github Profile Image Url: https://pbs.twimg.com/profile_images/616309728688238592/pBeeJQDQ_normal.png Profile Banner Url: https://pbs.twimg.com/profile_banners/13334762/1415719104 Profile Link Color Hex Triplet: 255 Name: GitHub Location: San Francisco, CA Structured Location: None Description: How people build software Url: https://t.co/FoKGHcCyJJ Url Entities: b&#39;{&#34;urls&#34;:[{&#34;url&#34;:&#34;https:\\/\\/t.co\\/FoKGHcCyJJ&#34;,&#34;rangeInDisplay.length&#34;:0,&#34;displayURL&#34;:&#34;github.com&#34;,&#34;rangeInDisplay.location&#34;:0,&#34;expandedURL&#34;:&#34;https:\\/\\/github.com&#34;,&#34;range.location&#34;:0,&#34;range.length&#34;:23}]}&#39; Bio Entities: b&#39;{}&#39; Protected: 0 Verified: 1 Following: 0 Device Following: 0 Advertiser Account Type: 0 Statuses Count: 3120 Media Count: 33 Favorites Count: 155 Following Count: 172 Followers Count: 742086 Followers Count Fast: 0 Followers Count Normal: 742086 Could Be Stale: 0 Is Lifeline Institution: 0 Has Collections: 0 Is Translator: 0 Has Extended Profile Fields: 0 Extended Profile Fields: None Pinned Tweet Id: None Business Profile State: 0 Analytics Type: 0'
    )
    expected_message_short = (
        u'Id: 13334762 Screen Name: github Profile Image Url: https://pbs.twimg.com/pro...'
    )

    self._TestGetMessageStrings(test_event, expected_message,
                                expected_message_short)

    # Test the first statuses date event.
    position = 0  #TODO
    test_event = storage_writer.events[position]
    expected_timestamp = timelib.Timestamp.CopyFromString(u'1410435976.0')
    self.assertEqual(test_event.timestamp, expected_timestamp)

    self.assertEqual(test_event.timestamp_desc,
                     eventdata.EventTimestamp.CREATION_TIME)
    self.assertEqual(test_event.card, u'None')
    self.assertEqual(test_event.card_users, u'None')
    self.assertEqual(test_event.card_version, u'0')
    expected_entities = (
        u'b&#39;{&#34;mediaUrls&#34;:[{&#34;thumbSizeWidth&#34;:150,&#34;mediaID&#34;:&#34;510031569718108160&#34;,&#34;largeSizeWidth&#34;:1024,&#34;largeSizeHeight&#34;:768,&#34;range.length&#34;:22,&#34;url&#34;:&#34;http:\\/\\/t.co\\/L7bjWue1A2&#34;,&#34;originalSizeHeight&#34;:0,&#34;smallSizeWidth&#34;:340,&#34;rangeInDisplay.location&#34;:14,&#34;mediumSizeFeatures&#34;:{&#34;faces&#34;:[]},&#34;range.location&#34;:14,&#34;expandedURL&#34;:&#34;http:\\/\\/twitter.com\\/HeatherMahalik\\/status\\/510031570397577216\\/photo\\/1&#34;,&#34;rangeInDisplay.length&#34;:26,&#34;originalSizeWidth&#34;:0,&#34;mediaType&#34;:1,&#34;largeSizeFeatures&#34;:{&#34;faces&#34;:[]},&#34;mediaURL&#34;:&#34;https:\\/\\/pbs.twimg.com\\/media\\/BxP_AqlIYAAyjn0.jpg&#34;,&#34;smallSizeHeight&#34;:255,&#34;smallSizeFeatures&#34;:{&#34;faces&#34;:[]},&#34;thumbSizeHeight&#34;:150,&#34;monetizable&#34;:false,&#34;mediumSizeHeight&#34;:450,&#34;displayURL&#34;:&#34;pic.twitter.com\\/L7bjWue1A2&#34;,&#34;mediumSizeWidth&#34;:600}]}&#39;'
    )
    self.assertEqual(test_event.entities, expected_entities)
    self.assertEqual(test_event.extra_scribe_item, u'None')
    self.assertEqual(test_event.favorite_count, u'3')
    self.assertEqual(test_event.favorited, u'0')
    self.assertEqual(test_event.full_text_length, u'0')
    self.assertEqual(test_event.geotag, u'None')
    self.assertEqual(test_event.id, u'510031570397577216')
    self.assertEqual(test_event.include_in_profile_timeline, u'1')
    self.assertEqual(test_event.in_reply_to_status_id, u'None')
    self.assertEqual(test_event.in_reply_to_username, u'None')
    self.assertEqual(test_event.is_lifeline_alert, u'0')
    self.assertEqual(test_event.is_possibly_sensitive_appealable, u'0')
    self.assertEqual(test_event.is_truncated, u'0')
    self.assertEqual(test_event.lang, u'en')
    self.assertEqual(test_event.possibly_sensitive, u'0')
    self.assertEqual(test_event.preview_length, u'0')
    self.assertEqual(test_event.primary_card_type, u'0')
    self.assertEqual(test_event.quoted_status_id, u'None')
    self.assertEqual(test_event.retweet_count, u'2')
    self.assertEqual(test_event.retweeted_status_id, u'None')
    expected_source = (
        u'&lt;a href=&#34;http://twitter.com/download/iphone&#34; rel=&#34;nofollow&#34;&gt;Twitter for iPhone&lt;/a&gt;'
    )
    self.assertEqual(test_event.source, expected_source)
    self.assertEqual(test_event.supplmental_language, u'None')
    expected_text = (u'Never forget. http://t.co/L7bjWue1A2')
    self.assertEqual(test_event.text, expected_text)
    self.assertEqual(test_event.user_id, u'475222380')
    self.assertEqual(test_event.withheld_in_countries, u'None')
    self.assertEqual(test_event.withheld_scope, u'None')

    expected_message = (
        u'Id: 510031570397577216 Text: Never forget. http://t.co/L7bjWue1A2 User Id: 475222380 In Reply To Status Id: None Retweeted Status Id: None Geotag: None Entities: b&#39;{&#34;mediaUrls&#34;:[{&#34;thumbSizeWidth&#34;:150,&#34;mediaID&#34;:&#34;510031569718108160&#34;,&#34;largeSizeWidth&#34;:1024,&#34;largeSizeHeight&#34;:768,&#34;range.length&#34;:22,&#34;url&#34;:&#34;http:\\/\\/t.co\\/L7bjWue1A2&#34;,&#34;originalSizeHeight&#34;:0,&#34;smallSizeWidth&#34;:340,&#34;rangeInDisplay.location&#34;:14,&#34;mediumSizeFeatures&#34;:{&#34;faces&#34;:[]},&#34;range.location&#34;:14,&#34;expandedURL&#34;:&#34;http:\\/\\/twitter.com\\/HeatherMahalik\\/status\\/510031570397577216\\/photo\\/1&#34;,&#34;rangeInDisplay.length&#34;:26,&#34;originalSizeWidth&#34;:0,&#34;mediaType&#34;:1,&#34;largeSizeFeatures&#34;:{&#34;faces&#34;:[]},&#34;mediaURL&#34;:&#34;https:\\/\\/pbs.twimg.com\\/media\\/BxP_AqlIYAAyjn0.jpg&#34;,&#34;smallSizeHeight&#34;:255,&#34;smallSizeFeatures&#34;:{&#34;faces&#34;:[]},&#34;thumbSizeHeight&#34;:150,&#34;monetizable&#34;:false,&#34;mediumSizeHeight&#34;:450,&#34;displayURL&#34;:&#34;pic.twitter.com\\/L7bjWue1A2&#34;,&#34;mediumSizeWidth&#34;:600}]}&#39; Card: None Card Users: None Primary Card Type: 0 Card Version: 0 Retweet Count: 2 Favorite Count: 3 Favorited: 0 Extra Scribe Item: None Withheld Scope: None Withheld In Countries: None In Reply To Username: None Possibly Sensitive: 0 Is Possibly Sensitive Appealable: 0 Is Lifeline Alert: 0 Is Truncated: 0 Preview Length: 0 Full Text Length: 0 Lang: en Supplmental Language: None Include In Profile Timeline: 1 Quoted Status Id: None Source: &lt;a href=&#34;http://twitter.com/download/iphone&#34; rel=&#34;nofollow&#34;&gt;Twitter for iPhone&lt;/a&gt;'
    )
    expected_message_short = (
        u'Id: 510031570397577216 Text: Never forget. http://t.co/L7bjWue1A2 User Id: 47...'
    )

    self._TestGetMessageStrings(test_event, expected_message,
                                expected_message_short)

    # Test the first statuses updatedAt event.
    position = 0  #TODO
    test_event = storage_writer.events[position]
    expected_timestamp = timelib.Timestamp.CopyFromString(u'1449070777.1575031')
    self.assertEqual(test_event.timestamp, expected_timestamp)

    self.assertEqual(test_event.timestamp_desc,
                     eventdata.EventTimestamp.CREATION_TIME)
    self.assertEqual(test_event.card, u'None')
    self.assertEqual(test_event.card_users, u'None')
    self.assertEqual(test_event.card_version, u'0')
    expected_entities = (
        u'b&#39;{&#34;mediaUrls&#34;:[{&#34;thumbSizeWidth&#34;:150,&#34;mediaID&#34;:&#34;666269245739692034&#34;,&#34;largeSizeWidth&#34;:590,&#34;largeSizeHeight&#34;:295,&#34;range.length&#34;:23,&#34;url&#34;:&#34;https:\\/\\/t.co\\/VtVaTY4Lh4&#34;,&#34;originalSizeHeight&#34;:0,&#34;smallSizeWidth&#34;:340,&#34;rangeInDisplay.location&#34;:91,&#34;mediumSizeFeatures&#34;:{&#34;faces&#34;:[{&#34;y&#34;:116,&#34;w&#34;:62,&#34;x&#34;:139,&#34;h&#34;:62}]},&#34;range.location&#34;:100,&#34;expandedURL&#34;:&#34;http:\\/\\/twitter.com\\/PacktPub\\/status\\/666269245827747840\\/photo\\/1&#34;,&#34;rangeInDisplay.length&#34;:26,&#34;originalSizeWidth&#34;:0,&#34;mediaType&#34;:1,&#34;largeSizeFeatures&#34;:{&#34;faces&#34;:[{&#34;y&#34;:116,&#34;w&#34;:62,&#34;x&#34;:139,&#34;h&#34;:62}]},&#34;mediaURL&#34;:&#34;https:\\/\\/pbs.twimg.com\\/media\\/CT8QWVUU8AIIptM.png&#34;,&#34;smallSizeHeight&#34;:170,&#34;smallSizeFeatures&#34;:{&#34;faces&#34;:[{&#34;y&#34;:66,&#34;w&#34;:35,&#34;x&#34;:80,&#34;h&#34;:35}]},&#34;thumbSizeHeight&#34;:150,&#34;monetizable&#34;:false,&#34;mediumSizeHeight&#34;:295,&#34;displayURL&#34;:&#34;pic.twitter.com\\/VtVaTY4Lh4&#34;,&#34;mediumSizeWidth&#34;:590}],&#34;urls&#34;:[{&#34;url&#34;:&#34;https:\\/\\/t.co\\/f4aNishzqk&#34;,&#34;rangeInDisplay.length&#34;:14,&#34;displayURL&#34;:&#34;bit.ly\\/20JGoj8&#34;,&#34;rangeInDisplay.location&#34;:76,&#34;expandedURL&#34;:&#34;http:\\/\\/bit.ly\\/20JGoj8&#34;,&#34;range.location&#34;:76,&#34;range.length&#34;:23}]}&#39;'
    )
    self.assertEqual(test_event.entities, expected_entities)
    self.assertEqual(test_event.extra_scribe_item, u'None')
    self.assertEqual(test_event.favorite_count, u'0')
    self.assertEqual(test_event.favorited, u'0')
    self.assertEqual(test_event.full_text_length, u'0')
    self.assertEqual(test_event.geotag, u'None')
    self.assertEqual(test_event.id, u'666269245827747840')
    self.assertEqual(test_event.include_in_profile_timeline, u'1')
    self.assertEqual(test_event.in_reply_to_status_id, u'None')
    self.assertEqual(test_event.in_reply_to_username, u'None')
    self.assertEqual(test_event.is_lifeline_alert, u'0')
    self.assertEqual(test_event.is_possibly_sensitive_appealable, u'0')
    self.assertEqual(test_event.is_truncated, u'0')
    self.assertEqual(test_event.lang, u'en')
    self.assertEqual(test_event.possibly_sensitive, u'0')
    self.assertEqual(test_event.preview_length, u'0')
    self.assertEqual(test_event.primary_card_type, u'0')
    self.assertEqual(test_event.quoted_status_id, u'None')
    self.assertEqual(test_event.retweet_count, u'0')
    self.assertEqual(test_event.retweeted_status_id, u'None')
    expected_source = (
        u'&lt;a href=&#34;http://sproutsocial.com&#34; rel=&#34;nofollow&#34;&gt;Sprout Social&lt;/a&gt;'
    )
    self.assertEqual(test_event.source, expected_source)
    self.assertEqual(test_event.supplmental_language, u'None')
    expected_text = (
        u'We don&#39;t care how you spend your $5 voucher - we just want to hear from you https://t.co/f4aNishzqk https://t.co/VtVaTY4Lh4'
    )
    self.assertEqual(test_event.text, expected_text)
    self.assertEqual(test_event.user_id, u'17778401')
    self.assertEqual(test_event.withheld_in_countries, u'None')
    self.assertEqual(test_event.withheld_scope, u'None')

    expected_message = (
        u'Id: 666269245827747840 Text: We don&#39;t care how you spend your $5 voucher - we just want to hear from you https://t.co/f4aNishzqk https://t.co/VtVaTY4Lh4 User Id: 17778401 In Reply To Status Id: None Retweeted Status Id: None Geotag: None Entities: b&#39;{&#34;mediaUrls&#34;:[{&#34;thumbSizeWidth&#34;:150,&#34;mediaID&#34;:&#34;666269245739692034&#34;,&#34;largeSizeWidth&#34;:590,&#34;largeSizeHeight&#34;:295,&#34;range.length&#34;:23,&#34;url&#34;:&#34;https:\\/\\/t.co\\/VtVaTY4Lh4&#34;,&#34;originalSizeHeight&#34;:0,&#34;smallSizeWidth&#34;:340,&#34;rangeInDisplay.location&#34;:91,&#34;mediumSizeFeatures&#34;:{&#34;faces&#34;:[{&#34;y&#34;:116,&#34;w&#34;:62,&#34;x&#34;:139,&#34;h&#34;:62}]},&#34;range.location&#34;:100,&#34;expandedURL&#34;:&#34;http:\\/\\/twitter.com\\/PacktPub\\/status\\/666269245827747840\\/photo\\/1&#34;,&#34;rangeInDisplay.length&#34;:26,&#34;originalSizeWidth&#34;:0,&#34;mediaType&#34;:1,&#34;largeSizeFeatures&#34;:{&#34;faces&#34;:[{&#34;y&#34;:116,&#34;w&#34;:62,&#34;x&#34;:139,&#34;h&#34;:62}]},&#34;mediaURL&#34;:&#34;https:\\/\\/pbs.twimg.com\\/media\\/CT8QWVUU8AIIptM.png&#34;,&#34;smallSizeHeight&#34;:170,&#34;smallSizeFeatures&#34;:{&#34;faces&#34;:[{&#34;y&#34;:66,&#34;w&#34;:35,&#34;x&#34;:80,&#34;h&#34;:35}]},&#34;thumbSizeHeight&#34;:150,&#34;monetizable&#34;:false,&#34;mediumSizeHeight&#34;:295,&#34;displayURL&#34;:&#34;pic.twitter.com\\/VtVaTY4Lh4&#34;,&#34;mediumSizeWidth&#34;:590}],&#34;urls&#34;:[{&#34;url&#34;:&#34;https:\\/\\/t.co\\/f4aNishzqk&#34;,&#34;rangeInDisplay.length&#34;:14,&#34;displayURL&#34;:&#34;bit.ly\\/20JGoj8&#34;,&#34;rangeInDisplay.location&#34;:76,&#34;expandedURL&#34;:&#34;http:\\/\\/bit.ly\\/20JGoj8&#34;,&#34;range.location&#34;:76,&#34;range.length&#34;:23}]}&#39; Card: None Card Users: None Primary Card Type: 0 Card Version: 0 Retweet Count: 0 Favorite Count: 0 Favorited: 0 Extra Scribe Item: None Withheld Scope: None Withheld In Countries: None In Reply To Username: None Possibly Sensitive: 0 Is Possibly Sensitive Appealable: 0 Is Lifeline Alert: 0 Is Truncated: 0 Preview Length: 0 Full Text Length: 0 Lang: en Supplmental Language: None Include In Profile Timeline: 1 Quoted Status Id: None Source: &lt;a href=&#34;http://sproutsocial.com&#34; rel=&#34;nofollow&#34;&gt;Sprout Social&lt;/a&gt;'
    )
    expected_message_short = (
        u'Id: 666269245827747840 Text: We don&#39;t care how you spend your $5 voucher - we...'
    )

    self._TestGetMessageStrings(test_event, expected_message,
                                expected_message_short)


if __name__ == '__main__':
  unittest.main()
