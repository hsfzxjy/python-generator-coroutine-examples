events_list = []


class Event(object):

    def __init__(self, *args, **kwargs):
        self.callback = lambda: None
        events_list.append(self)

    def set_callback(self, callback):
        self.callback = callback

    def is_ready(self):
        result = self._is_ready()

        if result:
            self.callback()

        return result
