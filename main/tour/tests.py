import time
from datetime import datetime

from django.test import TestCase


def select(input_func):
    def output_func(*args):
        start_time = datetime.now()
        input_func(*args)
        end_time = datetime.now()
        print(end_time-start_time)
    return output_func


@select
def hello(a, b):
    time.sleep(5)
    print(a + b)


hello(1, 2)