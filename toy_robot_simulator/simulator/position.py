class InvalidPosition(Exception):
    pass


class Position:
    def __init__(self, current_x: int, current_y: int):
        self.current_x = current_x
        self.current_y = current_y
