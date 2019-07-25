
from Handler.Event import *

class MarketEvent(Event):
    def __init__(self):
        self.type=EventType.Market
    
    def update_market(self):
        pass