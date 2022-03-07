import unittest
import test_setup

from simulator.simulator import command_parser
from simulator.commands import CommandPlace, CommandMove, CommandLeft, CommandRight, CommandReport


class TestCommandParser(unittest.TestCase):

    def line_parser(self, line):
        return command_parser(line)

    def test_command_parser(self):
        cmd = self.line_parser("PLACE 0,0,NORTH")
        self.assertEqual(type(cmd), CommandPlace)
        self.assertEqual(cmd.initial_args, ["0", "0", "NORTH"])

    def test_command_move(self):
        cmd = self.line_parser("MOVE")
        self.assertEqual(type(cmd), CommandMove)

    def test_command_left(self):
        cmd = self.line_parser("LEFT")
        self.assertEqual(type(cmd), CommandLeft)

    def test_command_right(self):
        cmd = self.line_parser("RIGHT")
        self.assertEqual(type(cmd), CommandRight)

    def test_command_report(self):
        cmd = self.line_parser("REPORT")
        self.assertEqual(type(cmd), CommandReport)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)