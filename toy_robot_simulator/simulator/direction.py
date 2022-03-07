class InvalidDirection(Exception):
    pass


class Direction:
    """
        Holds direction NORTH, SOUTH, EAST, WEST and calculates positional directions based on the direction.
    """
    directions_list = ['NORTH', 'WEST', 'SOUTH', 'EAST']
    NORTH, WEST, SOUTH, EAST = directions_list
    POSITIONAL_DIRECTIONS = {
        NORTH: (0, 1),
        SOUTH: (0, -1),
        EAST: (1, 0),
        WEST: (-1, 0)
    }

    def __init__(self, direction: str):
        if direction not in self.directions_list:
            raise InvalidDirection(f"invalid direction: {direction}")
        self._name = direction

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value not in self.directions_list:
            raise InvalidDirection(f"invalid direction: {value}")
        self._name = value

    def positional_direction(self, seed_value: int, position):
        """
            calculates positional direction based on current position and step-size(seed_value)
            :param seed_value:
            :param position:
            :return: next possible position
        """
        x, y = self.POSITIONAL_DIRECTIONS.get(self.name)
        return position.current_x + x * seed_value, position.current_y + y * seed_value

    def rotational_direction(self, seed_value: int):
        """
            calculates the next positional direction based on current direction and seed value
            :param seed_value:
            :return: next possible direction
        """
        index = (self.directions_list.index(self._name) + seed_value) % len(self.directions_list)
        self.name = self.directions_list[index]
