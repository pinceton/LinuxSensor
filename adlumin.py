'''
Created on Jun 7, 2017

@author: gevans
'''

import time
from sensor import process_monitor
from random import random

def print_current():
    now = time.localtime()
    print time.strftime("%Y-%m-%d-%H:%M:%S", now)

memory_leak = []

while True:
    print_current()
    print process_monitor.stacksize()
    memory_leak.append(random())
    time.sleep(1)
