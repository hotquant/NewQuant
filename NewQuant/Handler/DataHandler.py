
from abc import ABCMeta,abstractmethod
from Handler.Event import *
from Handler.MarketEvent import MarketEvent
import tushare as ts

import Model.BarData

class DataHandler(object):
    @abstractmethod
    def update_bars(self):
        raise NotImplementedError('Should implement update_bars()')
        
class CVSDataHandler(DataHandler):
    def __init__(self,environment,csv_dir,symbol_list):
        self.type=EventType.Bar
        self.b_continue_backtest=True
        self._environment=environment
        self.csv_dir = csv_dir
        self.symbol_list = symbol_list
        self.symbol_data = {}
        self.latest_symbol_data = {}   
        self._read_data_from_tushare()
        
    def _read_data_from_tushare(self):
        comb_index=None
        
        for s in self.symbol_list:
            self.symbol_data[s] = (ts.get_hist_data(s)).sort_index()
            print(self.symbol_data[s])
            if comb_index is None:
                comb_index=self.symbol_data[s].index
            else:
                comb_index=comb_index.union(self.symbol_data[s].index)
        self.latest_symbol_data[s]=[]
        for s in self.symbol_list:
            self.symbol_data[s]=self.symbol_data[s].reindex(index=comb_index,method='pad').iterrows()    
    
    def _get_new_bar(self, symbol):
        #if self.symbol_data.getattr('symbol') is None:return {'','','','',''}
        for b in self.symbol_data[symbol]:
            yield b
            
    def update_bars(self):        
        for s in self.symbol_list:
            try:
                print(s)
                bar = next(self._get_new_bar(s))
                if bar is not None:
                    self.latest_symbol_data[s].append(bar)
            except StopIteration:
                self.continue_backtest = False
                    
        self._environment.get_events().put(MarketEvent())