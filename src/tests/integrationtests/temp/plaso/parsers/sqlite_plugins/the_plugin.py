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


class ThePluginBlobtypesEventData(events.EventData):
  """the plugin blobtypes event data.

  TODO: add type and description of attributes
  Attributes:
    blobval (bytes): TODO
  """

  DATA_TYPE = u'the:plugin:'

  def __init__(self):
    """Initializes event data."""
    super(ThePluginBlobtypesEventData, self).__init__(data_type=self.DATA_TYPE)
    self.blobval = None


class ThePluginIntegertypesEventData(events.EventData):
  """the plugin integertypes event data.

  TODO: add type and description of attributes
  Attributes:
    bigintval (int): TODO
    int2val (int): TODO
    int8val (int): TODO
    integerval (int): TODO
    intval (int): TODO
    mediumintval (int): TODO
    smallintval (int): TODO
    tinyintval (int): TODO
    unsignedbigintval (int): TODO
  """

  DATA_TYPE = u'the:plugin:'

  def __init__(self):
    """Initializes event data."""
    super(ThePluginIntegertypesEventData, self).__init__(
        data_type=self.DATA_TYPE)
    self.bigintval = None
    self.int2val = None
    self.int8val = None
    self.integerval = None
    self.intval = None
    self.mediumintval = None
    self.smallintval = None
    self.tinyintval = None
    self.unsignedbigintval = None


class ThePluginNumerictypesEventData(events.EventData):
  """the plugin numerictypes event data.

  TODO: add type and description of attributes
  Attributes:
    booleanval (bool): TODO
    datetimeval (int): TODO
    dateval (int): TODO
    decimalval (int): TODO
    numericval (int): TODO
  """

  DATA_TYPE = u'the:plugin:'

  def __init__(self):
    """Initializes event data."""
    super(ThePluginNumerictypesEventData, self).__init__(
        data_type=self.DATA_TYPE)
    self.booleanval = None
    self.datetimeval = None
    self.dateval = None
    self.decimalval = None
    self.numericval = None


class ThePluginRealtypesEventData(events.EventData):
  """the plugin realtypes event data.

  TODO: add type and description of attributes
  Attributes:
    doubleprecesionval (float): TODO
    doubleval (float): TODO
    floatval (float): TODO
    realval (float): TODO
  """

  DATA_TYPE = u'the:plugin:'

  def __init__(self):
    """Initializes event data."""
    super(ThePluginRealtypesEventData, self).__init__(data_type=self.DATA_TYPE)
    self.doubleprecesionval = None
    self.doubleval = None
    self.floatval = None
    self.realval = None


class ThePluginTexttypesEventData(events.EventData):
  """the plugin texttypes event data.

  TODO: add type and description of attributes
  Attributes:
    characterval (str): TODO
    clobval (str): TODO
    nativecharacterval (str): TODO
    ncharval (str): TODO
    nvarchar_val (str): TODO
    textval (str): TODO
    varcharval (str): TODO
    varyingcharacterval (str): TODO
  """

  DATA_TYPE = u'the:plugin:'

  def __init__(self):
    """Initializes event data."""
    super(ThePluginTexttypesEventData, self).__init__(data_type=self.DATA_TYPE)
    self.characterval = None
    self.clobval = None
    self.nativecharacterval = None
    self.ncharval = None
    self.nvarchar_val = None
    self.textval = None
    self.varcharval = None
    self.varyingcharacterval = None


class ThePluginNodataEventData(events.EventData):
  """the plugin nodata event data.

  TODO: add type and description of attributes
  Attributes:
    bigintval (int): TODO
    blobval (bytes): TODO
    booleanval (bool): TODO
    characterval (str): TODO
    clobval (str): TODO
    datetimeval (int): TODO
    dateval (int): TODO
    decimalval (int): TODO
    doubleprecisionval (float): TODO
    doubleval (float): TODO
    floatval (float): TODO
    int2val (int): TODO
    int8val (int): TODO
    integerval (int): TODO
    intval (int): TODO
    mediuintval (int): TODO
    nativecharacterval (str): TODO
    ncharval (str): TODO
    numericval (int): TODO
    nvarcharval (str): TODO
    realval (float): TODO
    smallintval (int): TODO
    textval (str): TODO
    tinyintval (int): TODO
    unsignedbigintval (int): TODO
    varcharval (str): TODO
    varyingcharacterval (str): TODO
  """

  DATA_TYPE = u'the:plugin:'

  def __init__(self):
    """Initializes event data."""
    super(ThePluginNodataEventData, self).__init__(data_type=self.DATA_TYPE)
    self.bigintval = None
    self.blobval = None
    self.booleanval = None
    self.characterval = None
    self.clobval = None
    self.datetimeval = None
    self.dateval = None
    self.decimalval = None
    self.doubleprecisionval = None
    self.doubleval = None
    self.floatval = None
    self.int2val = None
    self.int8val = None
    self.integerval = None
    self.intval = None
    self.mediuintval = None
    self.nativecharacterval = None
    self.ncharval = None
    self.numericval = None
    self.nvarcharval = None
    self.realval = None
    self.smallintval = None
    self.textval = None
    self.tinyintval = None
    self.unsignedbigintval = None
    self.varcharval = None
    self.varyingcharacterval = None


class ThePluginPlugin(interface.SQLitePlugin):
  """Parser for ThePlugin"""

  NAME = u'the_plugin'
  DESCRIPTION = u'Parser for ThePlugin'

  QUERIES = [((u'select * from blobtypes)'), u'ParseBlobtypesRow'), ((
      u'select * from integertypes)'), u'ParseIntegertypesRow'), ((
          u'select * from numerictypes)'), u'ParseNumerictypesRow'), ((
              u'select * from realtypes)'), u'ParseRealtypesRow'), ((
                  u'select * from texttypes)'), u'ParseTexttypesRow'), ((
                      u'select * from nodata)'), u'ParseNodataRow')]

  REQUIRED_TABLES = frozenset([
      u'blobtypes', u'integertypes', u'nodata', u'numerictypes', u'realtypes',
      u'texttypes'
  ])

  def ParseBlobtypesRow(
      self, parser_mediator, row, query=None, **unused_kwargs):
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
    event_data.blobval = row['']

  def ParseIntegertypesRow(
      self, parser_mediator, row, query=None, **unused_kwargs):
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
    event_data.bigintval = row['']
    event_data.int2val = row['']
    event_data.int8val = row['']
    event_data.integerval = row['']
    event_data.intval = row['']
    event_data.mediumintval = row['']
    event_data.smallintval = row['']
    event_data.tinyintval = row['']
    event_data.unsignedbigintval = row['']

  def ParseNumerictypesRow(
      self, parser_mediator, row, query=None, **unused_kwargs):
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
    event_data.booleanval = row['']
    event_data.datetimeval = row['']
    event_data.dateval = row['']
    event_data.decimalval = row['']
    event_data.numericval = row['']

  def ParseRealtypesRow(
      self, parser_mediator, row, query=None, **unused_kwargs):
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
    event_data.doubleprecesionval = row['']
    event_data.doubleval = row['']
    event_data.floatval = row['']
    event_data.realval = row['']

  def ParseTexttypesRow(
      self, parser_mediator, row, query=None, **unused_kwargs):
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
    event_data.characterval = row['']
    event_data.clobval = row['']
    event_data.nativecharacterval = row['']
    event_data.ncharval = row['']
    event_data.nvarchar_val = row['']
    event_data.textval = row['']
    event_data.varcharval = row['']
    event_data.varyingcharacterval = row['']

  def ParseNodataRow(self, parser_mediator, row, query=None, **unused_kwargs):
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
    event_data.bigintval = row['']
    event_data.blobval = row['']
    event_data.booleanval = row['']
    event_data.characterval = row['']
    event_data.clobval = row['']
    event_data.datetimeval = row['']
    event_data.dateval = row['']
    event_data.decimalval = row['']
    event_data.doubleprecisionval = row['']
    event_data.doubleval = row['']
    event_data.floatval = row['']
    event_data.int2val = row['']
    event_data.int8val = row['']
    event_data.integerval = row['']
    event_data.intval = row['']
    event_data.mediuintval = row['']
    event_data.nativecharacterval = row['']
    event_data.ncharval = row['']
    event_data.numericval = row['']
    event_data.nvarcharval = row['']
    event_data.realval = row['']
    event_data.smallintval = row['']
    event_data.textval = row['']
    event_data.tinyintval = row['']
    event_data.unsignedbigintval = row['']
    event_data.varcharval = row['']
    event_data.varyingcharacterval = row['']


sqlite.SQLiteParser.RegisterPlugin(ThePluginPlugin)
