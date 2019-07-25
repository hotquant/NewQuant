
from Handler import SignalEvent,OrderEvent

class Portfolio(object):
    def __init__(self,_environment):
        self.__environment=_environment
        
    def on_signal(self,event):
        self.__environment.get_events().put(OrderEvent.OrderEvent())
        
    def on_fill(self,event):
        print("on fill finished")
        quit()
        
    def update_timeindex(self):
        self._environment.get_events().put(SignalEvent.SignalEvent())
        
    