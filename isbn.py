
class ISBN:
    @staticmethod
    def calculate_isbn10_checksum(value_list):
        if len(value_list) < 9:
            raise ValueError("value_list has to be at least 9 characters long")
        parts = value_list[:9]
        result = sum([((i+1) * int(x)) for i, x in enumerate(parts)]) % 11
        if result == 10:
            calculated_checksum = "X"
        else:
            calculated_checksum = str(result)
        return str(calculated_checksum)

    @staticmethod
    def calculate_isbn13_checksum(value_list):
        if len(value_list) < 12:
            raise ValueError("value_list has to be at least 12 characters long")
        z_n = list(value_list)[:12]
        z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12 = map(int, z_n)
        return str((10-((z1 + z3 + z5 + z7 + z9 + z11 + 3*(z2 + z4 + z6 + z8 + z10 + z12))%10))%10)

    @staticmethod
    def validate_isbn10(value):
        if len(value) != 10:
            return False
        expected_checksum = value[-1]
        calculated_checksum = ISBN.calculate_isbn10_checksum(value)
        return expected_checksum == calculated_checksum

    @staticmethod
    def validate_isbn13(value):
        if len(value) != 13:
            return False
        expected_checksum = value[-1]
        calculated_checksum = ISBN.calculate_isbn13_checksum(value)
        return expected_checksum == calculated_checksum

    @staticmethod
    def validate_isbn(value):
        if len(value) == 10:
            return ISBN.validate_isbn10(value)
        if len(value) == 13:
            return ISBN.validate_isbn13(value)
        return False
