# -*- coding: utf-8 -*-
from enum import Enum

class EventType(Enum):
    Bar='Bar'
    Market='Market'
    DataClean='DataClean'
    Signal='Signal'
    Order='Order'
    Fill='Fill'

class Event(object):
    def __init__(self):
        pass