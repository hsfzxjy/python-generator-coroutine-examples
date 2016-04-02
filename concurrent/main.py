from co import coroutine
from sleep import sleep
import runner
from time import time


@coroutine
def long_add(x, y, duration=1):
    yield sleep(duration)
    return x + y


@coroutine
def task(duration):
    print('start:', time())
    print((yield long_add(1, 2, duration)), time())
    print((yield long_add(3, 4, duration)), time())

task(2)
task(1)
runner.run()
