# -*- coding: utf-8 -*-
"""the plugin database formatter."""

from plaso.formatters import interface
from plaso.formatters import manager
from plaso.lib import errors


class ThePluginUsersFormatter(interface.ConditionalEventFormatter):
  """the plugin users event formatter."""

  DATA_TYPE = u'the:plugin:users'

  """Correct Format String Pieces where needed"""
  FORMAT_STRING_PIECES = [
    u'Advertiser Account Type:{advertiser_account_type}',
    u'Analytics Type:{analytics_type}',
    u'Bio Entities:{bio_entities}',
    u'Business Profile State:{business_profile_state}',
    u'Could Be Stale:{could_be_stale}',
    u'Created Date:{created_date}',
    u'Description:{description}',
    u'Device Following:{device_following}',
    u'Extended Profile Fields:{extended_profile_fields}',
    u'Favorites Count:{favorites_count}',
    u'Followers Count:{followers_count}',
    u'Followers Count Fast:{followers_count_fast}',
    u'Followers Count Normal:{followers_count_normal}',
    u'Following:{following}',
    u'Following Count:{following_count}',
    u'Has Collections:{has_collections}',
    u'Has Extended Profile Fields:{has_extended_profile_fields}',
    u'Id:{id}',
    u'Is Lifeline Institution:{is_lifeline_institution}',
    u'Is Translator:{is_translator}',
    u'Location:{location}',
    u'Media Count:{media_count}',
    u'Name:{name}',
    u'Pinned Tweet Id:{pinned_tweet_id}',
    u'Profile Banner Url:{profile_banner_url}',
    u'Profile Image Url:{profile_image_url}',
    u'Profile Link Color Hex Triplet:{profile_link_color_hex_triplet}',
    u'Protected:{protected}',
    u'Screen Name:{screen_name}',
    u'Statuses Count:{statuses_count}',
    u'Structured Location:{structured_location}',
    u'Updated At:{updated_at}',
    u'Url:{url}',
    u'Url Entities:{url_entities}',
    u'Verified:{verified}']

  #TODO: add Format String Pieces for the short Format
  FORMAT_STRING_SHORT_PIECES = []

  SOURCE_LONG = u'The Plugin Users'
  SOURCE_SHORT = u'The Plugin'
  #TODO: Replace constant _REPLACEWITHATTRIBUTENAME with the attribute to customize and add values
  _REPLACEWITHATTRIBUTENAME = {}

  def GetMessages(self, unused_formatter_mediator, event):
    """Determines the formatted message strings for an event object.

    Args:
      formatter_mediator (FormatterMediator): mediates the interactions between
          formatters and other components, such as storage and Windows EventLog
          resources.
      event (EventObject): event.

    Returns:
      tuple(str, str): formatted message string and short message string.

    Raises:
      WrongFormatter: if the event object cannot be formatted by the formatter.
    """
    if self.DATA_TYPE != event.data_type:
      raise errors.WrongFormatter(u'Unsupported data type: {0:s}.'.format(
          event.data_type))

    event_values = event.CopyToDict()

    # TODO: replace variable replace_with_attribute_name with the attribute to customize
    replace_with_attribute_name = event_values.get(u'replace_with_attribute_name', None)
    if replace_with_attribute_name is not None:
      event_values[u'replace_with_attribute_name'] = (
          self._REPLACEWITHATTRIBUTENAME.get(replace_with_attribute_name, u'UNKNOWN'))

    return self._ConditionalFormatMessages(event_values)



class ThePluginStatusesFormatter(interface.ConditionalEventFormatter):
  """the plugin statuses event formatter."""

  DATA_TYPE = u'the:plugin:statuses'

  """Correct Format String Pieces where needed"""
  FORMAT_STRING_PIECES = [
    u'Card:{card}',
    u'Card Users:{card_users}',
    u'Card Version:{card_version}',
    u'Date:{date}',
    u'Entities:{entities}',
    u'Extra Scribe Item:{extra_scribe_item}',
    u'Favorite Count:{favorite_count}',
    u'Favorited:{favorited}',
    u'Full Text Length:{full_text_length}',
    u'Geotag:{geotag}',
    u'Id:{id}',
    u'Include In Profile Timeline:{include_in_profile_timeline}',
    u'In Reply To Status Id:{in_reply_to_status_id}',
    u'In Reply To Username:{in_reply_to_username}',
    u'Is Lifeline Alert:{is_lifeline_alert}',
    u'Is Possibly Sensitive Appealable:{is_possibly_sensitive_appealable}',
    u'Is Truncated:{is_truncated}',
    u'Lang:{lang}',
    u'Possibly Sensitive:{possibly_sensitive}',
    u'Preview Length:{preview_length}',
    u'Primary Card Type:{primary_card_type}',
    u'Quoted Status Id:{quoted_status_id}',
    u'Retweet Count:{retweet_count}',
    u'Retweeted Status Id:{retweeted_status_id}',
    u'Source:{source}',
    u'Supplmental Language:{supplmental_language}',
    u'Text:{text}',
    u'Updated At:{updated_at}',
    u'User Id:{user_id}',
    u'Withheld In Countries:{withheld_in_countries}',
    u'Withheld Scope:{withheld_scope}']

  #TODO: add Format String Pieces for the short Format
  FORMAT_STRING_SHORT_PIECES = []

  SOURCE_LONG = u'The Plugin Statuses'
  SOURCE_SHORT = u'The Plugin'
  

manager.FormattersManager.RegisterFormatter([
  ThePluginUsersFormatter,
  ThePluginStatusesFormatter
])