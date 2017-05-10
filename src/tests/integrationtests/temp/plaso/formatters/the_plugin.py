# -*- coding: utf-8 -*-
"""the plugin database formatter."""

from plaso.formatters import interface
from plaso.formatters import manager
from plaso.lib import errors


class ThePluginBlobtypesFormatter(interface.ConditionalEventFormatter):
  """the plugin blobtypes event formatter."""

  DATA_TYPE = u'the:plugin:'
  """Correct Format String Pieces where needed"""

  FORMAT_STRING_PIECES = [
    u'Blobval:{blobval}']

  #TODO: add Format String Pieces for the short Format
  FORMAT_STRING_SHORT_PIECES = [
    u'Blobval:{blobval}']

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
          self._REPLACEWITHATTRIBUTENAME.get(
              replace_with_attribute_name, u'UNKNOWN'))

    return self._ConditionalFormatMessages(event_values)


class ThePluginIntegertypesFormatter(interface.ConditionalEventFormatter):
  """the plugin integertypes event formatter."""

  DATA_TYPE = u'the:plugin:'
  """Correct Format String Pieces where needed"""

  FORMAT_STRING_PIECES = [
    u'Intval:{intval}',
    u'Integerval:{integerval}',
    u'Tinyintval:{tinyintval}',
    u'Smallintval:{smallintval}',
    u'Mediumintval:{mediumintval}',
    u'Bigintval:{bigintval}',
    u'Unsignedbigintval:{unsignedbigintval}',
    u'Int2Val:{int2val}',
    u'Int8Val:{int8val}']

  #TODO: add Format String Pieces for the short Format
  FORMAT_STRING_SHORT_PIECES = [
    u'Intval:{intval}',
    u'Integerval:{integerval}',
    u'Tinyintval:{tinyintval}',
    u'Smallintval:{smallintval}',
    u'Mediumintval:{mediumintval}',
    u'Bigintval:{bigintval}',
    u'Unsignedbigintval:{unsignedbigintval}',
    u'Int2Val:{int2val}',
    u'Int8Val:{int8val}']

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
          self._REPLACEWITHATTRIBUTENAME.get(
              replace_with_attribute_name, u'UNKNOWN'))

    return self._ConditionalFormatMessages(event_values)


class ThePluginNumerictypesFormatter(interface.ConditionalEventFormatter):
  """the plugin numerictypes event formatter."""

  DATA_TYPE = u'the:plugin:'
  """Correct Format String Pieces where needed"""

  FORMAT_STRING_PIECES = [
    u'Numericval:{numericval}',
    u'Decimalval:{decimalval}',
    u'Booleanval:{booleanval}',
    u'Dateval:{dateval}',
    u'Datetimeval:{datetimeval}']

  #TODO: add Format String Pieces for the short Format
  FORMAT_STRING_SHORT_PIECES = [
    u'Numericval:{numericval}',
    u'Decimalval:{decimalval}',
    u'Booleanval:{booleanval}',
    u'Dateval:{dateval}',
    u'Datetimeval:{datetimeval}']

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
          self._REPLACEWITHATTRIBUTENAME.get(
              replace_with_attribute_name, u'UNKNOWN'))

    return self._ConditionalFormatMessages(event_values)


class ThePluginRealtypesFormatter(interface.ConditionalEventFormatter):
  """the plugin realtypes event formatter."""

  DATA_TYPE = u'the:plugin:'
  """Correct Format String Pieces where needed"""

  FORMAT_STRING_PIECES = [
    u'Realval:{realval}',
    u'Doubleval:{doubleval}',
    u'Doubleprecesionval:{doubleprecesionval}',
    u'Floatval:{floatval}']

  #TODO: add Format String Pieces for the short Format
  FORMAT_STRING_SHORT_PIECES = [
    u'Realval:{realval}',
    u'Doubleval:{doubleval}',
    u'Doubleprecesionval:{doubleprecesionval}',
    u'Floatval:{floatval}']

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
          self._REPLACEWITHATTRIBUTENAME.get(
              replace_with_attribute_name, u'UNKNOWN'))

    return self._ConditionalFormatMessages(event_values)


class ThePluginTexttypesFormatter(interface.ConditionalEventFormatter):
  """the plugin texttypes event formatter."""

  DATA_TYPE = u'the:plugin:'
  """Correct Format String Pieces where needed"""

  FORMAT_STRING_PIECES = [
    u'Characterval:{characterval}',
    u'Varcharval:{varcharval}',
    u'Varyingcharacterval:{varyingcharacterval}',
    u'Ncharval:{ncharval}',
    u'Nativecharacterval:{nativecharacterval}',
    u'Nvarchar Val:{nvarchar_val}',
    u'Textval:{textval}',
    u'Clobval:{clobval}']

  #TODO: add Format String Pieces for the short Format
  FORMAT_STRING_SHORT_PIECES = [
    u'Characterval:{characterval}',
    u'Varcharval:{varcharval}',
    u'Varyingcharacterval:{varyingcharacterval}',
    u'Ncharval:{ncharval}',
    u'Nativecharacterval:{nativecharacterval}',
    u'Nvarchar Val:{nvarchar_val}',
    u'Textval:{textval}',
    u'Clobval:{clobval}']

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
          self._REPLACEWITHATTRIBUTENAME.get(
              replace_with_attribute_name, u'UNKNOWN'))

    return self._ConditionalFormatMessages(event_values)


class ThePluginNodataFormatter(interface.ConditionalEventFormatter):
  """the plugin nodata event formatter."""

  DATA_TYPE = u'the:plugin:'
  """Correct Format String Pieces where needed"""

  FORMAT_STRING_PIECES = [
    u'Intval:{intval}',
    u'Integerval:{integerval}',
    u'Tinyintval:{tinyintval}',
    u'Smallintval:{smallintval}',
    u'Mediuintval:{mediuintval}',
    u'Bigintval:{bigintval}',
    u'Unsignedbigintval:{unsignedbigintval}',
    u'Int2Val:{int2val}',
    u'Int8Val:{int8val}',
    u'Characterval:{characterval}',
    u'Varcharval:{varcharval}',
    u'Varyingcharacterval:{varyingcharacterval}',
    u'Ncharval:{ncharval}',
    u'Nativecharacterval:{nativecharacterval}',
    u'Nvarcharval:{nvarcharval}',
    u'Textval:{textval}',
    u'Clobval:{clobval}',
    u'Blobval:{blobval}',
    u'Realval:{realval}',
    u'Doubleval:{doubleval}',
    u'Doubleprecisionval:{doubleprecisionval}',
    u'Floatval:{floatval}',
    u'Numericval:{numericval}',
    u'Decimalval:{decimalval}',
    u'Booleanval:{booleanval}',
    u'Dateval:{dateval}',
    u'Datetimeval:{datetimeval}']

  #TODO: add Format String Pieces for the short Format
  FORMAT_STRING_SHORT_PIECES = [
    u'Intval:{intval}',
    u'Integerval:{integerval}',
    u'Tinyintval:{tinyintval}',
    u'Smallintval:{smallintval}',
    u'Mediuintval:{mediuintval}',
    u'Bigintval:{bigintval}',
    u'Unsignedbigintval:{unsignedbigintval}',
    u'Int2Val:{int2val}',
    u'Int8Val:{int8val}',
    u'Characterval:{characterval}',
    u'Varcharval:{varcharval}',
    u'Varyingcharacterval:{varyingcharacterval}',
    u'Ncharval:{ncharval}',
    u'Nativecharacterval:{nativecharacterval}',
    u'Nvarcharval:{nvarcharval}',
    u'Textval:{textval}',
    u'Clobval:{clobval}',
    u'Blobval:{blobval}',
    u'Realval:{realval}',
    u'Doubleval:{doubleval}',
    u'Doubleprecisionval:{doubleprecisionval}',
    u'Floatval:{floatval}',
    u'Numericval:{numericval}',
    u'Decimalval:{decimalval}',
    u'Booleanval:{booleanval}',
    u'Dateval:{dateval}',
    u'Datetimeval:{datetimeval}']

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
          self._REPLACEWITHATTRIBUTENAME.get(
              replace_with_attribute_name, u'UNKNOWN'))

    return self._ConditionalFormatMessages(event_values)


manager.FormattersManager.RegisterFormatter([
    ThePluginBlobtypesFormatter, ThePluginIntegertypesFormatter,
    ThePluginNumerictypesFormatter, ThePluginRealtypesFormatter,
    ThePluginTexttypesFormatter, ThePluginNodataFormatter
])
