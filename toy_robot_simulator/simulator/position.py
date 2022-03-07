from dataclasses import dataclass


class InvalidPosition(Exception):
    pass


@dataclass
class Position:
    """Holds current co-ordinates"""
    current_x: int
    current_y: int
