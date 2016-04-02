class Future(object):
    def __init__(self):
        super(Future, self).__init__()
        self.callback = lambda *args: None
        self._done = False

    def set_callback(self, callback):
        self.callback = callback

    def done(self, value=None):
        self._done = True
        self.callback(value)
