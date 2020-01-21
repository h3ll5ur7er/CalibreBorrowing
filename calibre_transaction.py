
from resettable_timer import ResettableTimer
from calibre_config import MAX_AGE_IN_S, COMMAND_BORROW, COMMAND_RETURN

class Transaction:
    def __init__(self, borrow_handler, return_handler, command_visualizer, name_visualizer, isbn_visualizer, reset_all_visualizer):
        self.expired = False
        self._timer = ResettableTimer(MAX_AGE_IN_S, self.on_timeout)
        self._command = None
        self._name = None
        self._isbn = None
        self._borrow_handler = borrow_handler
        self._return_handler = return_handler
        self._command_visualizer = command_visualizer
        self._name_visualizer = name_visualizer
        self._isbn_visualizer = isbn_visualizer
        self._reset_all_visualizer = reset_all_visualizer

    @property
    def command(self):
        return self._command
    @command.setter
    def command(self, value):
        self._command_visualizer()
        self._command = value
        self._timer.reset()
        self.try_send()

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name_visualizer()
        self._name = value
        self._timer.reset()
        self.try_send()

    @property
    def isbn(self):
        return self._isbn
    @isbn.setter
    def isbn(self, value):
        self._isbn_visualizer()
        self._isbn = value
        self._timer.reset()
        self.try_send()

    def on_timeout(self):
        self._command = None
        self._name = None
        self._isbn = None
        self._reset_all_visualizer()
        self._timer.cancel()
        self.expired = True

    def is_valid(self):
        return self._command is not None and self._name is not None and self._isbn is not None

    def try_send(self):
        if not self.is_valid():
            return False
        if self._command == COMMAND_BORROW:
            self._borrow_handler(self._name, self._isbn)
        if self._command == COMMAND_RETURN:
            self._return_handler(self._name, self._isbn)
        self.on_timeout()
        return True
