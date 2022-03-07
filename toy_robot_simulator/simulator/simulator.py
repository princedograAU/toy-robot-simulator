import os

# enabling conditional import to facilitate testing of each test file without any import errors
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


# helper dict to map available commands with classes in command module
MAP_COMMANDS_TO_CLASSES = {
    "PLACE": CommandPlace,
    "MOVE": CommandMove,
    "LEFT": CommandLeft,
    "RIGHT": CommandRight,
    "REPORT": CommandReport
}


def command_parser(command_line):
    """
    split each line and separate the command and args out of it to perform mapping and action calling
    :param command_line:
    :return: Action Class like CommandPlace, etc.
    """
    commands = command_line.split()

    # get command out of the line
    action = commands[0]
    # when PLACE command is passed initial_args will be have value as ["0","0","NORTH"]
    initial_args = commands[1].split(",") if len(commands) > 1 else ""

    # map action to class and raise exception if not found
    if command_class := MAP_COMMANDS_TO_CLASSES.get(action):
        return command_class(initial_args)
    raise InvalidCommand(f"invalid command: {action}")


class Simulator:
    """
    Simulates toy robot based on the commands and ignore them if they are not either valid or drop robot from table
    """
    def __init__(self):
        self.robot = None
        self.table = None
        self.reset()

    def clear_console(self):
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')

    def reset(self):
        """restarts simulator after clearing the console"""
        self.table = Table(5, 5)
        self.robot = Robot(table=self.table)
        self.clear_console()
        self.instructions()

    def instructions(self):
        """displays instructions to the console"""
        print(22 * ":")
        print(" TOY ROBOT SIMULATOR ")
        print(22 * ":")

        print(f"TABLE SIZE : {self.table.table_x}x{self.table.table_y}")
        print(f"DIRECTIONS : {Direction.directions_list}")
        print(f"COMMANDS   : {[commands for commands in MAP_COMMANDS_TO_CLASSES.keys()]}")
        print("::::: TYPE EXIT TO QUIT SIMULATOR :::::")

    def simulate(self, command_line: str):
        """Parse each and every command and perform action accordingly"""
        try:
            command = command_parser(command_line)
            # bind action with caller
            command.action(dispatcher=self.robot)
        except InvalidCommand:
            print(f"invalid command:\nonly available commands are : "
                  f"{[commands for commands in MAP_COMMANDS_TO_CLASSES.keys()]}\n")
        except InvalidPosition:
            print(f"invalid position:\ntable is of size {self.table.table_x}x{self.table.table_y}")
        except InvalidDirection:
            print(f"invalid direction:\nonly available directions are : {Direction.directions_list}")
