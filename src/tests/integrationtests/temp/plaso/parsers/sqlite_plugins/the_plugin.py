# -*- coding: utf-8 -*-
"""Parser for the plugin database.

SQLite database path:
# TODO: add database path
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
    advertiser_account_type (int): TODO
    analytics_type (int): TODO
    bio_entities (bytes): TODO
    business_profile_state (int): TODO
    could_be_stale (int): TODO
    description (str): TODO
    device_following (int): TODO
    extended_profile_fields (bytes): TODO
    favorites_count (int): TODO
    followers_count (int): TODO
    followers_count_fast (int): TODO
    followers_count_normal (int): TODO
    following (int): TODO
    following_count (int): TODO
    has_collections (int): TODO
    has_extended_profile_fields (int): TODO
    id (int): TODO
    is_lifeline_institution (int): TODO
    is_translator (int): TODO
    location (str): TODO
    media_count (int): TODO
    name (str): TODO
    pinned_tweet_id (int): TODO
    profile_banner_url (str): TODO
    profile_image_url (str): TODO
    profile_link_color_hex_triplet (int): TODO
    protected (int): TODO
    screen_name (str): TODO
    statuses_count (int): TODO
    structured_location (bytes): TODO
    url (str): TODO
    url_entities (bytes): TODO
    verified (int): TODO
  """

  DATA_TYPE = u'the:plugin:'

  def __init__(self):
    """Initializes event data."""
    super(ThePluginUsersEventData, self).__init__(data_type=self.DATA_TYPE)
    self.advertiser_account_type = None
    self.analytics_type = None
    self.bio_entities = None
    self.business_profile_state = None
    self.could_be_stale = None
    self.description = None
    self.device_following = None
    self.extended_profile_fields = None
    self.favorites_count = None
    self.followers_count = None
    self.followers_count_fast = None
    self.followers_count_normal = None
    self.following = None
    self.following_count = None
    self.has_collections = None
    self.has_extended_profile_fields = None
    self.id = None
    self.is_lifeline_institution = None
    self.is_translator = None
    self.location = None
    self.media_count = None
    self.name = None
    self.pinned_tweet_id = None
    self.profile_banner_url = None
    self.profile_image_url = None
    self.profile_link_color_hex_triplet = None
    self.protected = None
    self.screen_name = None
    self.statuses_count = None
    self.structured_location = None
    self.url = None
    self.url_entities = None
    self.verified = None


class ThePluginStatusesEventData(events.EventData):
  """the plugin statuses event data.

  TODO: add type and description of attributes
  Attributes:
    card (bytes): TODO
    card_users (bytes): TODO
    card_version (int): TODO
    entities (bytes): TODO
    extra_scribe_item (bytes): TODO
    favorite_count (int): TODO
    favorited (int): TODO
    full_text_length (int): TODO
    geotag (bytes): TODO
    id (int): TODO
    include_in_profile_timeline (int): TODO
    in_reply_to_status_id (int): TODO
    in_reply_to_username (str): TODO
    is_lifeline_alert (int): TODO
    is_possibly_sensitive_appealable (int): TODO
    is_truncated (int): TODO
    lang (str): TODO
    possibly_sensitive (int): TODO
    preview_length (int): TODO
    primary_card_type (int): TODO
    quoted_status_id (int): TODO
    retweet_count (int): TODO
    retweeted_status_id (int): TODO
    source (str): TODO
    supplmental_language (str): TODO
    text (str): TODO
    user_id (int): TODO
    withheld_in_countries (str): TODO
    withheld_scope (str): TODO
  """

  DATA_TYPE = u'the:plugin:'

  def __init__(self):
    """Initializes event data."""
    super(ThePluginStatusesEventData, self).__init__(data_type=self.DATA_TYPE)
    self.card = None
    self.card_users = None
    self.card_version = None
    self.entities = None
    self.extra_scribe_item = None
    self.favorite_count = None
    self.favorited = None
    self.full_text_length = None
    self.geotag = None
    self.id = None
    self.include_in_profile_timeline = None
    self.in_reply_to_status_id = None
    self.in_reply_to_username = None
    self.is_lifeline_alert = None
    self.is_possibly_sensitive_appealable = None
    self.is_truncated = None
    self.lang = None
    self.possibly_sensitive = None
    self.preview_length = None
    self.primary_card_type = None
    self.quoted_status_id = None
    self.retweet_count = None
    self.retweeted_status_id = None
    self.source = None
    self.supplmental_language = None
    self.text = None
    self.user_id = None
    self.withheld_in_countries = None
    self.withheld_scope = None


class ThePluginPlugin(interface.SQLitePlugin):
  """Parser for ThePlugin"""

  NAME = u'the_plugin'
  DESCRIPTION = u'Parser for ThePlugin'

  QUERIES = [((u'select * from users)'), u'ParseUsersRow'),
             ((u'select * from users)'), u'ParseStatusesRow')]

  REQUIRED_TABLES = frozenset([
      u'Lists', u'ListsShadow', u'MyRetweets', u'Statuses', u'StatusesShadow',
      u'Users', u'UsersShadow'
  ])

  def ParseUsersRow(self, parser_mediator, row, query=None, **unused_kwargs):
    """Parses a contact row from the database.

    Args:
      parser_mediator (ParserMediator): mediates interactions between parsers
          and other components, such as storage and dfvfs.
      row (sqlite3.Row): row resulting from Query.
      Query (Optional[str]): Query.
    """
    # Note that pysqlite does not accept a Unicode string in row['string'] and
    # will raise "IndexError: Index must be int or string".

    event_data = ThePluginEventData()
    event_data.advertiser_account_type = row['']
    event_data.analytics_type = row['']
    event_data.bio_entities = row['']
    event_data.business_profile_state = row['']
    event_data.could_be_stale = row['']
    event_data.description = row['']
    event_data.device_following = row['']
    event_data.extended_profile_fields = row['']
    event_data.favorites_count = row['']
    event_data.followers_count = row['']
    event_data.followers_count_fast = row['']
    event_data.followers_count_normal = row['']
    event_data.following = row['']
    event_data.following_count = row['']
    event_data.has_collections = row['']
    event_data.has_extended_profile_fields = row['']
    event_data.id = row['']
    event_data.is_lifeline_institution = row['']
    event_data.is_translator = row['']
    event_data.location = row['']
    event_data.media_count = row['']
    event_data.name = row['']
    event_data.pinned_tweet_id = row['']
    event_data.profile_banner_url = row['']
    event_data.profile_image_url = row['']
    event_data.profile_link_color_hex_triplet = row['']
    event_data.protected = row['']
    event_data.screen_name = row['']
    event_data.statuses_count = row['']
    event_data.structured_location = row['']
    event_data.url = row['']
    event_data.url_entities = row['']
    event_data.verified = row['']

    timestamp = row['createdDate']
    if timestamp:
      # Convert the floating point value to an integer.
      timestamp = int(timestamp)
      date_time = dfdatetime_posix_time.PosixTime(timestamp=timestamp)
      # TODO: Add correct time field for None value.  Example: eventdata.EventTimestamp.UPDATE_TIME
      event = time_events.DateTimeValuesEvent(date_time, None)
      parser_mediator.ProduceEventWithEventData(event, event_data)

    timestamp = row['updatedAt']
    if timestamp:
      # Convert the floating point value to an integer.
      timestamp = int(timestamp)
      date_time = dfdatetime_posix_time.PosixTime(timestamp=timestamp)
      # TODO: Add correct time field for None value.  Example: eventdata.EventTimestamp.UPDATE_TIME
      event = time_events.DateTimeValuesEvent(date_time, None)
      parser_mediator.ProduceEventWithEventData(event, event_data)

  def ParseStatusesRow(self, parser_mediator, row, query=None, **unused_kwargs):
    """Parses a contact row from the database.

    Args:
      parser_mediator (ParserMediator): mediates interactions between parsers
          and other components, such as storage and dfvfs.
      row (sqlite3.Row): row resulting from Query.
      Query (Optional[str]): Query.
    """
    # Note that pysqlite does not accept a Unicode string in row['string'] and
    # will raise "IndexError: Index must be int or string".

    event_data = ThePluginEventData()
    event_data.card = row['']
    event_data.card_users = row['']
    event_data.card_version = row['']
    event_data.entities = row['']
    event_data.extra_scribe_item = row['']
    event_data.favorite_count = row['']
    event_data.favorited = row['']
    event_data.full_text_length = row['']
    event_data.geotag = row['']
    event_data.id = row['']
    event_data.include_in_profile_timeline = row['']
    event_data.in_reply_to_status_id = row['']
    event_data.in_reply_to_username = row['']
    event_data.is_lifeline_alert = row['']
    event_data.is_possibly_sensitive_appealable = row['']
    event_data.is_truncated = row['']
    event_data.lang = row['']
    event_data.possibly_sensitive = row['']
    event_data.preview_length = row['']
    event_data.primary_card_type = row['']
    event_data.quoted_status_id = row['']
    event_data.retweet_count = row['']
    event_data.retweeted_status_id = row['']
    event_data.source = row['']
    event_data.supplmental_language = row['']
    event_data.text = row['']
    event_data.user_id = row['']
    event_data.withheld_in_countries = row['']
    event_data.withheld_scope = row['']

    timestamp = row['date']
    if timestamp:
      # Convert the floating point value to an integer.
      timestamp = int(timestamp)
      date_time = dfdatetime_posix_time.PosixTime(timestamp=timestamp)
      # TODO: Add correct time field for None value.  Example: eventdata.EventTimestamp.UPDATE_TIME
      event = time_events.DateTimeValuesEvent(date_time, None)
      parser_mediator.ProduceEventWithEventData(event, event_data)

    timestamp = row['updatedAt']
    if timestamp:
      # Convert the floating point value to an integer.
      timestamp = int(timestamp)
      date_time = dfdatetime_posix_time.PosixTime(timestamp=timestamp)
      # TODO: Add correct time field for None value.  Example: eventdata.EventTimestamp.UPDATE_TIME
      event = time_events.DateTimeValuesEvent(date_time, None)
      parser_mediator.ProduceEventWithEventData(event, event_data)


sqlite.SQLiteParser.RegisterPlugin(ThePluginPlugin)
