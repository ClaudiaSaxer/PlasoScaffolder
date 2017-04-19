# -*- coding: utf-8 -*-
"""Parser for the plugin database.

SQLite database path:
#TODO: add database path
SQLite database Name: the_plugin.db
"""

from dfdatetime import posix_time as dfdatetime_posix_time

from plaso.containers import time_events
from plaso.lib import eventdata
from plaso.parsers import sqlite
from plaso.parsers.sqlite_plugins import interface

class ThePluginUsersEventData(events.EventData):
  """the plugin users event data.

  TODO: add type and description of attributes
  Attributes:  
      id (int): TODO
      screen_name (str): TODO
      profile_image_url (str): TODO
      profile_banner_url (str): TODO
      profile_link_color_hex_triplet (int): TODO
      name (str): TODO
      location (str): TODO
      structured_location (NoneType): TODO
      description (str): TODO
      url (str): TODO
      url_entities (NoneType): TODO
      bio_entities (NoneType): TODO
      protected (int): TODO
      verified (int): TODO
      following (int): TODO
      device_following (int): TODO
      advertiser_account_type (int): TODO
      statuses_count (int): TODO
      media_count (NoneType): TODO
      favorites_count (int): TODO
      following_count (int): TODO
      followers_count (int): TODO
      followers_count_fast (int): TODO
      followers_count_normal (int): TODO
      could_be_stale (int): TODO
      is_lifeline_institution (int): TODO
      has_collections (int): TODO
      updated_at (float): TODO
      created_date (float): TODO
      is_translator (int): TODO
      has_extended_profile_fields (int): TODO
      extended_profile_fields (NoneType): TODO
      pinned_tweet_id (NoneType): TODO
      business_profile_state (int): TODO
      analytics_type (int): TODO
  """

  DATA_TYPE = u'the:plugin:users'

  def __init__(self):
    """Initializes event data."""
    super(ThePluginUsersEventData, self).__init__(data_type=self.DATA_TYPE)
    self.id = None
    self.screen_name = None
    self.profile_image_url = None
    self.profile_banner_url = None
    self.profile_link_color_hex_triplet = None
    self.name = None
    self.location = None
    self.structured_location = None
    self.description = None
    self.url = None
    self.url_entities = None
    self.bio_entities = None
    self.protected = None
    self.verified = None
    self.following = None
    self.device_following = None
    self.advertiser_account_type = None
    self.statuses_count = None
    self.media_count = None
    self.favorites_count = None
    self.following_count = None
    self.followers_count = None
    self.followers_count_fast = None
    self.followers_count_normal = None
    self.could_be_stale = None
    self.is_lifeline_institution = None
    self.has_collections = None
    self.updated_at = None
    self.created_date = None
    self.is_translator = None
    self.has_extended_profile_fields = None
    self.extended_profile_fields = None
    self.pinned_tweet_id = None
    self.business_profile_state = None
    self.analytics_type = None
    

class ThePluginStatusesEventData(events.EventData):
  """the plugin statuses event data.

  TODO: add type and description of attributes
  Attributes:  
      id (int): TODO
      text (str): TODO
      date (float): TODO
      user_id (int): TODO
      in_reply_to_status_id (NoneType): TODO
      retweeted_status_id (NoneType): TODO
      geotag (NoneType): TODO
      entities (bytes): TODO
      card (NoneType): TODO
      card_users (NoneType): TODO
      primary_card_type (int): TODO
      card_version (int): TODO
      retweet_count (int): TODO
      favorite_count (int): TODO
      favorited (int): TODO
      updated_at (float): TODO
      extra_scribe_item (NoneType): TODO
      withheld_scope (NoneType): TODO
      withheld_in_countries (NoneType): TODO
      in_reply_to_username (NoneType): TODO
      possibly_sensitive (int): TODO
      is_possibly_sensitive_appealable (int): TODO
      is_lifeline_alert (int): TODO
      is_truncated (int): TODO
      preview_length (int): TODO
      full_text_length (int): TODO
      lang (str): TODO
      supplmental_language (NoneType): TODO
      include_in_profile_timeline (int): TODO
      quoted_status_id (NoneType): TODO
      source (str): TODO
  """

  DATA_TYPE = u'the:plugin:statuses'

  def __init__(self):
    """Initializes event data."""
    super(ThePluginStatusesEventData, self).__init__(data_type=self.DATA_TYPE)
    self.id = None
    self.text = None
    self.date = None
    self.user_id = None
    self.in_reply_to_status_id = None
    self.retweeted_status_id = None
    self.geotag = None
    self.entities = None
    self.card = None
    self.card_users = None
    self.primary_card_type = None
    self.card_version = None
    self.retweet_count = None
    self.favorite_count = None
    self.favorited = None
    self.updated_at = None
    self.extra_scribe_item = None
    self.withheld_scope = None
    self.withheld_in_countries = None
    self.in_reply_to_username = None
    self.possibly_sensitive = None
    self.is_possibly_sensitive_appealable = None
    self.is_lifeline_alert = None
    self.is_truncated = None
    self.preview_length = None
    self.full_text_length = None
    self.lang = None
    self.supplmental_language = None
    self.include_in_profile_timeline = None
    self.quoted_status_id = None
    self.source = None
    


class ThePluginPlugin(interface.SQLitePlugin):
  """Parser for ThePlugin"""

  NAME = u'the_plugin'
  DESCRIPTION = u'Parser for ThePlugin'

  QUERIES = [ 
    ((u'select id from users)'),
     u'ParseUsersRow'),
    ((u'select id from users)'),
     u'ParseStatusesRow')]

  REQUIRED_TABLES = frozenset([
      u'Lists',
      u'ListsShadow',
      u'MyRetweets',
      u'Statuses',
      u'StatusesShadow',
      u'Users',
      u'UsersShadow'])


  def ParseUsersRow(self,  parser_mediator, row, query=None, **unused_kwargs):
    """Parses a contact row from the database.

    Args:
      parser_mediator (ParserMediator): mediates interactions between parsers
          and other components, such as storage and dfvfs.
      row (sqlite3.Row): row resulting from Query.
      Query (Optional[str]): Query.
    """
    # Note that pysqlite does not accept a Unicode string in row['string'] and
    # will raise "IndexError: Index must be int or string".

    event_data = ThePluginUsersEventData()
    event_data.id = row['id']
    event_data.screen_name = row['screenName']
    event_data.profile_image_url = row['profileImageUrl']
    event_data.profile_banner_url = row['profileBannerUrl']
    event_data.profile_link_color_hex_triplet = row['profileLinkColorHexTriplet']
    event_data.name = row['name']
    event_data.location = row['location']
    event_data.structured_location = row['structuredLocation']
    event_data.description = row['description']
    event_data.url = row['url']
    event_data.url_entities = row['urlEntities']
    event_data.bio_entities = row['bioEntities']
    event_data.protected = row['protected']
    event_data.verified = row['verified']
    event_data.following = row['following']
    event_data.device_following = row['deviceFollowing']
    event_data.advertiser_account_type = row['advertiserAccountType']
    event_data.statuses_count = row['statusesCount']
    event_data.media_count = row['mediaCount']
    event_data.favorites_count = row['favoritesCount']
    event_data.following_count = row['followingCount']
    event_data.followers_count = row['followersCount']
    event_data.followers_count_fast = row['followersCountFast']
    event_data.followers_count_normal = row['followersCountNormal']
    event_data.could_be_stale = row['couldBeStale']
    event_data.is_lifeline_institution = row['isLifelineInstitution']
    event_data.has_collections = row['hasCollections']
    event_data.updated_at = row['updatedAt']
    event_data.created_date = row['createdDate']
    event_data.is_translator = row['isTranslator']
    event_data.has_extended_profile_fields = row['hasExtendedProfileFields']
    event_data.extended_profile_fields = row['extendedProfileFields']
    event_data.pinned_tweet_id = row['pinnedTweetId']
    event_data.business_profile_state = row['businessProfileState']
    event_data.analytics_type = row['analyticsType']
    
    # TODO: add timestamp row to convert
    timestamp = row['TODO']
    if timestamp:
    # Convert the floating point value to an integer.
      timestamp = int(timestamp)
      date_time = dfdatetime_posix_time.PosixTime(timestamp=timestamp)
      # TODO: Add correct time field for None value.  Example: eventdata.EventTimestamp.UPDATE_TIME
      event = time_events.DateTimeValuesEvent(date_time, None)
      parser_mediator.ProduceEventWithEventData(event, event_data)

  def ParseStatusesRow(self,  parser_mediator, row, query=None, **unused_kwargs):
    """Parses a contact row from the database.

    Args:
      parser_mediator (ParserMediator): mediates interactions between parsers
          and other components, such as storage and dfvfs.
      row (sqlite3.Row): row resulting from Query.
      Query (Optional[str]): Query.
    """
    # Note that pysqlite does not accept a Unicode string in row['string'] and
    # will raise "IndexError: Index must be int or string".

    event_data = ThePluginStatusesEventData()
    event_data.id = row['id']
    event_data.text = row['text']
    event_data.date = row['date']
    event_data.user_id = row['userId']
    event_data.in_reply_to_status_id = row['inReplyToStatusId']
    event_data.retweeted_status_id = row['retweetedStatusId']
    event_data.geotag = row['geotag']
    event_data.entities = row['entities']
    event_data.card = row['card']
    event_data.card_users = row['cardUsers']
    event_data.primary_card_type = row['primaryCardType']
    event_data.card_version = row['cardVersion']
    event_data.retweet_count = row['retweetCount']
    event_data.favorite_count = row['favoriteCount']
    event_data.favorited = row['favorited']
    event_data.updated_at = row['updatedAt']
    event_data.extra_scribe_item = row['extraScribeItem']
    event_data.withheld_scope = row['withheldScope']
    event_data.withheld_in_countries = row['withheldInCountries']
    event_data.in_reply_to_username = row['inReplyToUsername']
    event_data.possibly_sensitive = row['possiblySensitive']
    event_data.is_possibly_sensitive_appealable = row['isPossiblySensitiveAppealable']
    event_data.is_lifeline_alert = row['isLifelineAlert']
    event_data.is_truncated = row['isTruncated']
    event_data.preview_length = row['previewLength']
    event_data.full_text_length = row['fullTextLength']
    event_data.lang = row['lang']
    event_data.supplmental_language = row['supplmentalLanguage']
    event_data.include_in_profile_timeline = row['includeInProfileTimeline']
    event_data.quoted_status_id = row['quotedStatusId']
    event_data.source = row['source']
    
    # TODO: add timestamp row to convert
    timestamp = row['TODO']
    if timestamp:
    # Convert the floating point value to an integer.
      timestamp = int(timestamp)
      date_time = dfdatetime_posix_time.PosixTime(timestamp=timestamp)
      # TODO: Add correct time field for None value.  Example: eventdata.EventTimestamp.UPDATE_TIME
      event = time_events.DateTimeValuesEvent(date_time, None)
      parser_mediator.ProduceEventWithEventData(event, event_data)


sqlite.SQLiteParser.RegisterPlugin(ThePluginPlugin)