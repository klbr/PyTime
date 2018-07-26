from threading import Timer
import time
from random import randint

def hello(index):
    print('Timer started', index, time.ctime(time.time()))
    print('Hello :)', index)

print('Start', time.ctime(time.time()))
for i in range(5):
    t = Timer(5, hello, args=(i, ))
    t.start()

print('Done and waiting...')