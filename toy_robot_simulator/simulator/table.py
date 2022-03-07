from dataclasses import dataclass


@dataclass
class Table:
    """Initializes table with default of 5x5"""
    table_x: int
    table_y: int

    def is_valid_move(self, x: int, y: int):
        """check if move is valid"""
        return -1 < x <= (self.table_x - 1) and -1 < y <= (self.table_y - 1) if True else False
