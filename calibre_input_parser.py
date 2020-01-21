from isbn import ISBN
from calibre_config import USER_MARKER, COMMAND_MARKER

class InputParser:
    def detect_name(self, value):
        return value.split()[0] == USER_MARKER

    def detect_command(self, value):
        return value.split()[0] == COMMAND_MARKER

    def detect_isbn(self, value):
        is_numeric = all(map(lambda x: x.isnumeric(), value))
        length = len(value)
        has_valid_length = length == 10 or length == 13
        correct_checksum = ISBN.validate_isbn(value)
        return is_numeric and has_valid_length and correct_checksum

