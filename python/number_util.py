
class NumberUtils:
    @staticmethod
    def is_in_closed_range(v: int, lower_bound: int, upper_bound: int) -> bool:
        return lower_bound <= v <= upper_bound

    @staticmethod
    def is_in_open_range(v: int, lower_bound: int, upper_bound: int) -> bool:
        return lower_bound < v < upper_bound

    @staticmethod
    def is_in_open_closed_range(v: int, lower_bound: int, upper_bound: int) -> bool:
        return lower_bound < v <= upper_bound

    @staticmethod
    def is_in_closed_open_range(v: int, lower_bound: int, upper_bound: int) -> bool:
        return lower_bound <= v < upper_bound
