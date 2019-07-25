
from Handler.Event import *

class OrderEvent(Event):
    def __init__(self):
        self.type=EventType.Order