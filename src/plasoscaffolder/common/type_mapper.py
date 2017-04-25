# -*- coding: utf-8 -*-
"""The mapper between SQL and python data types"""


class TypeMapperSQLitePython(object):
  """The mapper between SQLite and python data types"""
  # https://sqlite.org/datatype3.html
  MAPPINGS = {'BLOB': bytes,
              'INTEGER': int,
              'INT': int,
              'TINYINT': int,
              'SMALLINT': int,
              'MEDIUMINT': int,
              'BIGINT': int,
              'UNSIGNED BIG INT': int,
              'INT2': int,
              'INT8': int,
              'TEXT': str,
              'CHARACTER': str,
              'VARCHAR': str,
              'VARYING CHARACTER': str,
              'NCHAR': str,
              'NATIVE CHARACTER': str,
              'NVARCHAR': str,
              'TEXT': str,
              'CLOB': str,
              'REAL': float,
              'DOUBLE': float,
              'DOUBLE PRECISION': float,
              'FLOAT': float,
              'NUMERIC': float,
              'DECIMAL': float,
              'BOOLEAN': float,
              'DATE': float,
              'DATETIME': float
              }