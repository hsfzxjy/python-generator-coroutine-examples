from event import Event
from time import time


class SleepEvent(Event):

    def __init__(self, timeout):
        super(SleepEvent, self).__init__(timeout)
        self.timeout = timeout
        self.start_time = time()

    def _is_ready(self):
        return time() - self.start_time >= self.timeout


def sleep(timeout):
    return SleepEvent(timeout)
