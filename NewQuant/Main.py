# -*- coding: utf-8 -*-

from Handler import *
from Handler import DataHandler
from Handler import Portfolio
from Handler import Execution
from Handler import MyStrategy
from Handler.Event import *
from Model import Environment
import queue
'''
import sys,os
d = os.path.dirname(__file__)
sys.path.append(d)
'''

class Backtest(object):
    def __init__(self):
        self._strategy=None
        self._market=None
        self._dataHandler=None
        self._portfolio=None
        self._order=None
        self._signal=None
        self._events=None
        self._contruct()
        self._init_event_handlers()
        
    def _init_event_handlers(self):
        self._event_handler={}
        self._event_handler[EventType.Market]=self._handle_event_bar
        self._event_handler[EventType.Signal]=self._handle_event_signal
        self._event_handler[EventType.Order]=self._handle_event_order
        self._event_handler[EventType.Fill]=self._handle_event_fill
        
    def _contruct(self):
        self._events=queue.Queue()
        self._environment=Environment.Environment(self._events)
        self._dataHandler=DataHandler.CVSDataHandler(self._environment,'',['300008'])
        self._strategy=MyStrategy.MyStrategy(self._environment)
        self._portfolio=Portfolio.Portfolio(self._environment)
        self._execution=Execution.SimulatedExecution(self._environment)
       
        
    def run(self):
        while True:
            if self._dataHandler.b_continue_backtest:
                self._dataHandler.update_bars()
            else:
                break
                
            while True:
                try:
                    event=self._events.get(False)
                except queue.Empty:
                    break
                else:
                    self._handle_event(event)
                    
    def _handle_event(self,event):
        print("_handle_event")
        handler=self._event_handler.get(event.type,None)
        if handler is None:
            print('type:%s,handler is None'%event.type)
        else:
            handler(event)
            
    def _handle_event_bar(self,event):
        print('OnBar Event',event.type)
        self._strategy.on_bar()
        self._portfolio.update_timeindex()
    
    def _handle_event_signal(self,event):
        print('OnSignal Event',event.type)
        self._portfolio.on_signal(event)
        
    def _handle_event_order(self,event):
        print('OnOrder Event',event.type)
        self._execution.submit_order(event)
        
    def _handle_event_fill(self,event):
        print('OnFill Event',event.type)
        self._portfolio.on_fill(event)
        
    def _output(self):
        pass

def _adjust_start_date():
    config_start_date
    pass
    
def _rqalpha_main(self):
    pass
        
if __name__=="__main__":
    backtest=Backtest()
    backtest.run()