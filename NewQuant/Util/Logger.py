
from datetime import datetime
#import tracebook
import logbook
from logbook import Logger
from logbook.more import ColorizedStderrHandler
import better_exceptions
logbook.set_datetime_format("local")

logbook.base._level_names[logbook.base.WARNING]='WARN'

def format_exception(exc,value,tb):
    pass
    
better_exceptions.format_exception=format_exception

__all__ = [
    "user_log",
    "system_log",
]

DATETIME_FORMAT="%Y-%m-%d %H:%M:%S.00"

def user_std_handler_log_formatter(record,handler):
    pass

def formatter_builder():
    pass

user_log=Logger("user_log")

user_system_log=Logger("user_system_log")

user_detail_log=Logger("user_detail_log")

system_log=Logger("system_log")

std_log=Logger("std_log")

def user_print(*args,**kwargs):
    pass


if __name__=="__main__":
    user_log.info("test log")
    user_system_log.info("haha")
    print("Logger Unitest Finished!")
    