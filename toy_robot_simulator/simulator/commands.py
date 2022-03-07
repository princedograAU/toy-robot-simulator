import os
from abc import ABCMeta, abstractmethod

# conditional import to help test single module
if os.environ.get("TEST_ENABLED"):
    from .position import Position, InvalidPosition
    from .direction import Direction
else:
    from position import Position, InvalidPosition
    from direction import Direction


class InvalidCommand(Exception):
    pass


class BaseCommand(metaclass=ABCMeta):
    """
        Abstract Base Class
    """
    _initial_args = []

    def __init__(self, initial_args=None):
        self.initial_args = initial_args

    @property
    def initial_args(self):
        return self._initial_args

    @initial_args.setter
    def initial_args(self, initial_args):
        self._initial_args = initial_args

    @abstractmethod
    def action(self, dispatcher):
        """
            hook to bind action creator like robot with already available commands
            :params: dispatcher
        """
        pass


class CommandPlace(BaseCommand):
    """
        Expects constructor params of format
        <int>,<int>,<direction>

        integer value should be in range of 0-table-size (0-5)
        direction should be one of NORTH, SOUTH, EAST, WEST
        example: 0,0,NORTH

        :raises: InvalidPosition, if invalid PLACE arguments are passed
        example: 0,0,UP or 0,A,NORTH or None
    """

    @BaseCommand.initial_args.setter
    def initial_args(self, initial_args):
        # de-structure x, y co-ordinate and direction
        # validate if co-ordinates are integer only
        BaseCommand.initial_args.fset(self, initial_args)
        try:
            x, y, direction = initial_args
            x = int(x)
            y = int(y)
        except ValueError:
            raise InvalidPosition("position arguments should be a number")
        except TypeError:
            raise InvalidPosition("position arguments required")

        self._position = Position(current_x=x, current_y=y)
        self._direction = Direction(direction)

    def action(self, dispatcher):
        dispatcher.place(self._direction, self._position)


class CommandMove(BaseCommand):

    def action(self, dispatcher):
        dispatcher.action_move()


class CommandLeft(BaseCommand):

    def action(self, dispatcher):
        dispatcher.action_rotate(seed_value=1)


class CommandRight(BaseCommand):

    def action(self, dispatcher):
        dispatcher.action_rotate(seed_value=-1)


class CommandReport(BaseCommand):

    def action(self, dispatcher):
        print(dispatcher.action_report())
