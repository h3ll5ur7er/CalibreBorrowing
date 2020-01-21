
from threading import Timer

class ResettableTimer:
    def __init__(self, interval_in_s, handler):
        """
        Resettable timer class compatible with threading.Timer
        """
        self.interval = interval_in_s
        self.handler = handler
        self.started = False
        self._timer = Timer(self.interval, self.handler)

    def start(self):
        """
        Start method for compatibility with threading.Timer class.
        Starts the timer.
        """
        self._timer.start()
        self.started = True

    def cancel(self):
        """
        Cancel method for compatibility with threading.Timer class.
        Abort the timer.
        """
        try:
            self._timer.cancel()
        except:
            pass

    def reset(self):
        """
        Stops the running Timer and starts a new one.
        If timer is not running, it is started
        """
        if not self.started:
            self.start()
        else:
            self._timer.cancel()
            self._timer = Timer(self.interval, self.handler)
            self._timer.start()
