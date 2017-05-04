# -*- coding: utf-8 -*-
"""the plugin database formatter."""

from plaso.formatters import interface
from plaso.formatters import manager
from plaso.lib import errors


class ThePluginBlobtypesFormatter(interface.ConditionalEventFormatter):
  """the plugin blobtypes event formatter."""

  DATA_TYPE = u'the:plugin:blobtypes'
  """Correct Format String Pieces where needed"""
  FORMAT_STRING_PIECES = [u'Blobval:{blobval}']

  #TODO: add Format String Pieces for the short Format
  FORMAT_STRING_SHORT_PIECES = []

  SOURCE_LONG = u'The Plugin Blobtypes'
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
      raise errors.WrongFormatter(
        u'Unsupported data type: {0:s}.'.format(event.data_type))

    event_values = event.CopyToDict()

    # TODO: replace variable replace_with_attribute_name with the attribute to customize
    replace_with_attribute_name = event_values.get(
      u'replace_with_attribute_name', None)
    if replace_with_attribute_name is not None:
      event_values[u'replace_with_attribute_name'] = (
        self._REPLACEWITHATTRIBUTENAME.get(replace_with_attribute_name,
                                           u'UNKNOWN'))

    return self._ConditionalFormatMessages(event_values)


class ThePluginIntegertypesFormatter(interface.ConditionalEventFormatter):
  """the plugin integertypes event formatter."""

  DATA_TYPE = u'the:plugin:integertypes'
  """Correct Format String Pieces where needed"""
  FORMAT_STRING_PIECES = [
    u'Bigintval:{bigintval}', u'Int2Val:{int2val}', u'Int8Val:{int8val}',
    u'Integerval:{integerval}', u'Intval:{intval}',
    u'Mediumintval:{mediumintval}', u'Smallintval:{smallintval}',
    u'Tinyintval:{tinyintval}', u'Unsignedbigintval:{unsignedbigintval}'
  ]

  #TODO: add Format String Pieces for the short Format
  FORMAT_STRING_SHORT_PIECES = []

  SOURCE_LONG = u'The Plugin Integertypes'
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
      raise errors.WrongFormatter(
        u'Unsupported data type: {0:s}.'.format(event.data_type))

    event_values = event.CopyToDict()

    # TODO: replace variable replace_with_attribute_name with the attribute to customize
    replace_with_attribute_name = event_values.get(
      u'replace_with_attribute_name', None)
    if replace_with_attribute_name is not None:
      event_values[u'replace_with_attribute_name'] = (
        self._REPLACEWITHATTRIBUTENAME.get(replace_with_attribute_name,
                                           u'UNKNOWN'))

    return self._ConditionalFormatMessages(event_values)


class ThePluginNumerictypesFormatter(interface.ConditionalEventFormatter):
  """the plugin numerictypes event formatter."""

  DATA_TYPE = u'the:plugin:numerictypes'
  """Correct Format String Pieces where needed"""
  FORMAT_STRING_PIECES = [
    u'Booleanval:{booleanval}', u'Datetimeval:{datetimeval}',
    u'Dateval:{dateval}', u'Decimalval:{decimalval}', u'Numericval:{numericval}'
  ]

  #TODO: add Format String Pieces for the short Format
  FORMAT_STRING_SHORT_PIECES = []

  SOURCE_LONG = u'The Plugin Numerictypes'
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
      raise errors.WrongFormatter(
        u'Unsupported data type: {0:s}.'.format(event.data_type))

    event_values = event.CopyToDict()

    # TODO: replace variable replace_with_attribute_name with the attribute to customize
    replace_with_attribute_name = event_values.get(
      u'replace_with_attribute_name', None)
    if replace_with_attribute_name is not None:
      event_values[u'replace_with_attribute_name'] = (
        self._REPLACEWITHATTRIBUTENAME.get(replace_with_attribute_name,
                                           u'UNKNOWN'))

    return self._ConditionalFormatMessages(event_values)


class ThePluginRealtypesFormatter(interface.ConditionalEventFormatter):
  """the plugin realtypes event formatter."""

  DATA_TYPE = u'the:plugin:realtypes'
  """Correct Format String Pieces where needed"""
  FORMAT_STRING_PIECES = [
    u'Doubleprecesionval:{doubleprecesionval}', u'Doubleval:{doubleval}',
    u'Floatval:{floatval}', u'Realval:{realval}'
  ]

  #TODO: add Format String Pieces for the short Format
  FORMAT_STRING_SHORT_PIECES = []

  SOURCE_LONG = u'The Plugin Realtypes'
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
      raise errors.WrongFormatter(
        u'Unsupported data type: {0:s}.'.format(event.data_type))

    event_values = event.CopyToDict()

    # TODO: replace variable replace_with_attribute_name with the attribute to customize
    replace_with_attribute_name = event_values.get(
      u'replace_with_attribute_name', None)
    if replace_with_attribute_name is not None:
      event_values[u'replace_with_attribute_name'] = (
        self._REPLACEWITHATTRIBUTENAME.get(replace_with_attribute_name,
                                           u'UNKNOWN'))

    return self._ConditionalFormatMessages(event_values)


class ThePluginTexttypesFormatter(interface.ConditionalEventFormatter):
  """the plugin texttypes event formatter."""

  DATA_TYPE = u'the:plugin:texttypes'
  """Correct Format String Pieces where needed"""
  FORMAT_STRING_PIECES = [
    u'Characterval:{characterval}', u'Clobval:{clobval}',
    u'Nativecharacterval:{nativecharacterval}', u'Ncharval:{ncharval}',
    u'Nvarchar Val:{nvarchar_val}', u'Textval:{textval}',
    u'Varcharval:{varcharval}', u'Varyingcharacterval:{varyingcharacterval}'
  ]

  #TODO: add Format String Pieces for the short Format
  FORMAT_STRING_SHORT_PIECES = []

  SOURCE_LONG = u'The Plugin Texttypes'
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
      raise errors.WrongFormatter(
        u'Unsupported data type: {0:s}.'.format(event.data_type))

    event_values = event.CopyToDict()

    # TODO: replace variable replace_with_attribute_name with the attribute to customize
    replace_with_attribute_name = event_values.get(
      u'replace_with_attribute_name', None)
    if replace_with_attribute_name is not None:
      event_values[u'replace_with_attribute_name'] = (
        self._REPLACEWITHATTRIBUTENAME.get(replace_with_attribute_name,
                                           u'UNKNOWN'))

    return self._ConditionalFormatMessages(event_values)


class ThePluginNodataFormatter(interface.ConditionalEventFormatter):
  """the plugin nodata event formatter."""

  DATA_TYPE = u'the:plugin:nodata'
  """Correct Format String Pieces where needed"""
  FORMAT_STRING_PIECES = [
    u'Bigintval:{bigintval}', u'Blobval:{blobval}', u'Booleanval:{booleanval}',
    u'Characterval:{characterval}', u'Clobval:{clobval}',
    u'Datetimeval:{datetimeval}', u'Dateval:{dateval}',
    u'Decimalval:{decimalval}', u'Doubleprecisionval:{doubleprecisionval}',
    u'Doubleval:{doubleval}', u'Floatval:{floatval}', u'Int2Val:{int2val}',
    u'Int8Val:{int8val}', u'Integerval:{integerval}', u'Intval:{intval}',
    u'Mediuintval:{mediuintval}', u'Nativecharacterval:{nativecharacterval}',
    u'Ncharval:{ncharval}', u'Numericval:{numericval}',
    u'Nvarcharval:{nvarcharval}', u'Realval:{realval}',
    u'Smallintval:{smallintval}', u'Textval:{textval}',
    u'Tinyintval:{tinyintval}', u'Unsignedbigintval:{unsignedbigintval}',
    u'Varcharval:{varcharval}', u'Varyingcharacterval:{varyingcharacterval}'
  ]

  #TODO: add Format String Pieces for the short Format
  FORMAT_STRING_SHORT_PIECES = []

  SOURCE_LONG = u'The Plugin Nodata'
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
      raise errors.WrongFormatter(
        u'Unsupported data type: {0:s}.'.format(event.data_type))

    event_values = event.CopyToDict()

    # TODO: replace variable replace_with_attribute_name with the attribute to customize
    replace_with_attribute_name = event_values.get(
      u'replace_with_attribute_name', None)
    if replace_with_attribute_name is not None:
      event_values[u'replace_with_attribute_name'] = (
        self._REPLACEWITHATTRIBUTENAME.get(replace_with_attribute_name,
                                           u'UNKNOWN'))

    return self._ConditionalFormatMessages(event_values)


manager.FormattersManager.RegisterFormatter([
  ThePluginBlobtypesFormatter, ThePluginIntegertypesFormatter,
  ThePluginNumerictypesFormatter, ThePluginRealtypesFormatter,
  ThePluginTexttypesFormatter, ThePluginNodataFormatter
])
