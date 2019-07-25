from Handler import SignalEvent
from Handler import Strategy


class MyStrategy(Strategy.Strategy):
    def __init__(self,environment):
        self._environment=environment
        
    def on_bar(self):
        self._environment.get_events().put(SignalEvent.SignalEvent())
        
    def calculate_signals(self):
        pass