
from Handler.Event import *

class SignalEvent(Event):
    def __init__(self):
        self.type=EventType.Signal