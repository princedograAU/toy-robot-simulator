import os

# enabling conditional import to facilitate testing of each test file without any import errors
import sys

if os.environ.get("TEST_ENABLED"):
    from .commands import CommandPlace, CommandMove, CommandLeft, CommandRight, CommandReport, InvalidCommand
    from .table import Table
    from .robot import Robot
    from .direction import InvalidDirection, Direction
    from .position import InvalidPosition
else:
    from commands import CommandPlace, CommandMove, CommandLeft, CommandRight, CommandReport, InvalidCommand
    from table import Table
    from robot import Robot
    from direction import InvalidDirection, Direction
    from position import InvalidPosition


MAP_COMMANDS_TO_CLASSES = {
    "PLACE": CommandPlace,
    "MOVE": CommandMove,
    "LEFT": CommandLeft,
    "RIGHT": CommandRight,
    "REPORT": CommandReport
}


def command_parser(command_line):
    commands = command_line.split()

    action = commands[0]
    initial_args = commands[1].split(",") if len(commands) > 1 else ""

    for command, command_class in MAP_COMMANDS_TO_CLASSES.items():
        if action == command:
            return command_class(initial_args)
    raise InvalidCommand(f"invalid command: {action}")


class Simulator:
    def __init__(self):
        self.robot = None
        self.table = None
        self.reset()

    def clear_console(self):
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')

    def reset(self):
        self.table = Table(5, 5)
        self.robot = Robot(table=self.table)
        self.clear_console()
        self.instructions()

    def instructions(self):
        print(22 * ":")
        print(" TOY ROBOT SIMULATOR ")
        print(22 * ":")

        print(f"TABLE SIZE : {self.table.table_x}x{self.table.table_y}")
        print(f"DIRECTIONS : {Direction.directions_list}")
        print(f"COMMANDS   : {[commands for commands in MAP_COMMANDS_TO_CLASSES.keys()]}")
        print("::::: TYPE EXIT TO QUIT SIMULATOR :::::")

    def simulate(self, command_line: str):
        command = command_parser(command_line)
        try:
            command.action(dispatcher=self.robot)
        except InvalidCommand:
            print(f"invalid command:\nonly available commands are : "
                  f"{[commands for commands in MAP_COMMANDS_TO_CLASSES.keys()]}\n")
        except InvalidPosition:
            print(f"invalid position:\ntable is of size {self.table.table_x}x{self.table.table_y}")
        except InvalidDirection:
            print(f"invalid direction:\nonly available directions are : {Direction.directions_list}")
