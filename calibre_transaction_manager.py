
from calibre_input_parser import InputParser
from calibre_transaction import Transaction

class TransactionManager:
    def __init__(self, borrow_handler, return_handler, command_visualizer, name_visualizer, isbn_visualizer, reset_all_visualizer):
        self._borrow_handler = borrow_handler
        self._return_handler = return_handler
        self._command_visualizer = command_visualizer
        self._name_visualizer = name_visualizer
        self._isbn_visualizer = isbn_visualizer
        self._reset_all_visualizer = reset_all_visualizer
        self.input_parser = InputParser()
        self.reset_transaction()

    def reset_transaction(self):
        self.transaction = Transaction(self._borrow_handler, self._return_handler, self._command_visualizer, self._name_visualizer, self._isbn_visualizer, self._reset_all_visualizer)

    def on_name_changed(self, value):
        if self.transaction.expired:
            self.reset_transaction()
        value = " ".join(value.split()[1:])
        print("found name: ", value)
        self.transaction.name = value

    def on_command_changed(self, value):
        if self.transaction.expired:
            self.reset_transaction()
        value = " ".join(value.split()[1:])
        print("found command: ", value)
        self.transaction.command = value

    def on_isbn_changed(self, value):
        if self.transaction.expired:
            self.reset_transaction()
        print("found isbn: ", value)
        self.transaction.isbn = value

    def on_enter_pressed(self, cmd):
        print("Enter was pressed: ", cmd)
        if self.input_parser.detect_command(cmd):
            self.on_command_changed(cmd)
        elif self.input_parser.detect_name(cmd):
            self.on_name_changed(cmd)
        elif self.input_parser.detect_isbn(cmd):
            self.on_isbn_changed(cmd)
        else:
            print("unknown input: ", cmd)
