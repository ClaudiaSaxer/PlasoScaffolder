# -*- coding: utf-8 -*-
"""The event model class."""


class EventModel(object):
  "A event model."

  def __init__(self, name: str, needs_customizing=False):
    """ initializes the event model.

    Args:
      name (str): The Name of the event.
      needs_customizing (bool): If the event needs customizing.
    """
    self._name = name
    self._needs_customizing = needs_customizing

  @property
  def Name(self) -> str:
    """ the event Name.

    Returns:
      (str): The Name of the event.
    """
    return self._name

  @property
  def NeedsCustomizing(self) -> bool:
    """ If the event needs customizing.

    Returns:
      (bool): True if the event needs customizing. False if not.

    """
    return self._needs_customizing
