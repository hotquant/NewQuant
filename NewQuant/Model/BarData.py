

class BarData(object):
    def __init__(self,data,dt=None):
        self._data=data
        self._dt=dt
     
    @property
    def date(self):
        return self._data['date']
    
    @property
    def open(self):
        return self._data['open']
    
    @property
    def close(self):
        return self._data['close']
    
    @property
    def high(self):
        return self._data['high']
        
    @property
    def low(self):
        return self._data['low']
    
    @property
    def volume(self):
        return self._data['volume']
    
    @property
    def prev_close(self):
        pass
        
    @property
    def limit_down(self):
        try:
            v=self._data['limit_down']
            return v if v != 0 else np.nan
        except (KeyError,ValueError):
            return np.nan
        
    @property
    def limit_up(self):
        try:
            v=self._data['limit_up']
            return v if v!=0 else np.nan
        except (KeyError,ValueError):
            return np.nan
    
    def output(self):
        print('date=%s,open=%d,close=%d,high=%d,low=%d,volume=%d'%
            (self.date,self.open,self.close,self.high,self.low,self.volume)
            )

class BarDatas(object):
    def __init__(self,symbol,datas):
        self.symbol=symbol
        self.datas=datas
    
    def get_latest_bar(self):
        pass
    
    def get_latest_bar_date(self):
        pass
        
    def get_latest_bars(self):
        pass
    

if __name__=="__main__":
    test_date='2019-02-02'
    test_open=3.25
    test_close=3.37
    test_high=3.42
    test_low=3.33
    test_volume=300
    barData=BarData(test_date,test_open,test_close,test_high,test_low,test_volume)
    barData.output()
    print('BarData UnitTest Finished!')