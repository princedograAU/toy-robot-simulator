import os

if os.environ.get("TEST_ENABLED"):
    from .position import InvalidPosition
else:
    from position import InvalidPosition


class MissingPosition(Exception):
    pass


class MissingDirection(Exception):
    pass


class Robot:
    """
        Initializes a robot with 4 params:
        table: <class 'Table'>
        position: <class 'Position'>
        direction: <class 'Direction'>
        step_size: int (default to 1)
    """
    def __init__(self, table):
        self._table = table
        self._position = None
        self._direction = None
        self._step_size = 1

    @property
    def step_size(self):
        return self._step_size

    @property
    def table(self):
        return self._table

    @property
    def position(self):
        return self._position

    @property
    def direction(self):
        return self._direction

    @step_size.setter
    def step_size(self, value):
        self._step_size = value

    @position.setter
    def position(self, position):
        """sets valid position"""
        if self._table.is_valid_move(position.current_x, position.current_y):
            self._position = position

    @direction.setter
    def direction(self, direction):
        self._direction = direction

    def place(self, direction, position):
        """validates position and direction before assigning then to robot"""
        if not self._table.is_valid_move(position.current_x, position.current_y):
            raise InvalidPosition(f"invalid position")
        self.position = position
        self.direction = direction

    def action_report(self):
        """
        :raises: MissingPosition, MissingDirection if position and direction is not set for robot
        :return: string with robot coordinates and direction
        example: 0,0,NORTH
        """
        if not self._position:
            raise MissingPosition("initial position not set")

        if not self._direction:
            raise MissingDirection("initial direction not set")

        return f"{self._position.current_x},{self._position.current_y},{self._direction.name}"

    def action_move(self):
        """
            Moves robot by 1-step if move is a valid move
        """
        if not self._position:
            raise MissingPosition("initial position not set")

        new_x, new_y = self._direction.positional_direction(seed_value=self._step_size, position=self.position)
        if self._table.is_valid_move(new_x, new_y):
            self._position.current_y = new_y
            self._position.current_x = new_x

    def action_rotate(self, seed_value):
        """
        rotates robot 90 degree based on seed_valye
        :param seed_value:
        """
        if not self._direction:
            raise MissingPosition("direction not set")

        self._direction.rotational_direction(seed_value=seed_value)


