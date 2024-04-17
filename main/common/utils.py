from datetime import datetime
import time


def time_of_function(function):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = function()
        print(datetime.now() - start)
        return res
    return wrapper
