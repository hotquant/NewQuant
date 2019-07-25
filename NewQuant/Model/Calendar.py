from abc import ABCMeta,abstractmethod

class Calendar(object):
    
    @abstractmethod
    def check(self):
        pass
    
#A股日历
class AStockCalendar(Calendar):
    
    def check(self):
        pass

#期货日历
class FutureCalendar(Calendar):
    
    def check(self):
        pass

#数字货币日历
class DigitalCalendar(Calendar):
    
    def check(self):
        pass
        
#美股日历
class USStockCalendar(Calendar):
    
    def check(self):
        pass
        
#港股日历
class HKStockCalendar(Calendar):

    def check(self):
        pass
        
if __name__=="__main__":
    print('Calendar UnitTest finished!')