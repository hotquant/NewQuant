
from Handler import FillEvent
from Model import Environment

class Execution(object):
    pass
    
class SimulatedExecution(Execution):
    def __init__(self,environment):
        self._environment=environment
        
    def submit_order(self,event):
        self._environment.get_events().put(FillEvent.FillEvent())
