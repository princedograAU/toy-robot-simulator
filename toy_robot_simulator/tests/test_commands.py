import os
import unittest
import test_setup

# Relative path
from simulator.table import Table
from simulator.robot import Robot
from simulator.commands import CommandPlace, CommandMove, CommandLeft, CommandRight, CommandReport
from simulator.position import Position, InvalidPosition
from simulator.direction import InvalidDirection


class TestCommands(unittest.TestCase):
    def setUp(self) -> None:
        self.table = Table(5, 5)
        self.robot = Robot(self.table)

    def test_invalid_place_params(self):
        cases = (
            (
                None,
                InvalidPosition
            ),
            (
                ["A", "0", "NORTH"],
                InvalidPosition
            ),
            (
                ["1", "0", "NO-DIRECTION"],
                InvalidDirection
            ),
        )
        for index, (params, raise_exception) in enumerate(cases):
            with self.subTest(index), self.assertRaises(raise_exception):
                CommandPlace(params)

    def test_command_place(self):
        command_place = CommandPlace(["1", "0", "NORTH"])
        command_place.action(dispatcher=self.robot)
        self.assertEqual(self.robot.position.current_x, 1)
        self.assertEqual(self.robot.position.current_y, 0)
        self.assertEqual(self.robot.direction.name, "NORTH")

    def test_command_move(self):
        cases = (
            (
                ["1", "0", "NORTH"],
                {'current_x': 1, 'current_y': 1},
                "NORTH"
            ),
            (
                ["4", "4", "SOUTH"],
                {'current_x': 4, 'current_y': 3},
                "SOUTH"
            ),
            (
                ["4", "0", "WEST"],
                {'current_x': 3, 'current_y': 0},
                "WEST"
            ),
            (
                ["0", "4", "EAST"],
                {'current_x': 1, 'current_y': 4},
                "EAST"
            ),
            (
                ["0", "4", "SOUTH"],
                {'current_x': 0, 'current_y': 3},
                "SOUTH"
            ),
        )
        for index, (params, final_coordinates, direction) in enumerate(cases):
            with self.subTest(index):
                cmd_place = CommandPlace(params)
                cmd_place.action(dispatcher=self.robot)
                cmd_move = CommandMove()
                cmd_move.action(dispatcher=self.robot)
                self.assertEqual(self.robot.position.__dict__, final_coordinates)
                self.assertEqual(self.robot.direction.name, direction)

    def test_command_move_not_available(self):
        cases = (
            (
                ["4", "4", "NORTH"],
                {'current_x': 4, 'current_y': 4},
                "NORTH"
            ),
            (
                ["4", "4", "EAST"],
                {'current_x': 4, 'current_y': 4},
                "EAST"
            ),
            (
                ["0", "0", "WEST"],
                {'current_x': 0, 'current_y': 0},
                "WEST"
            ),
            (
                ["0", "0", "SOUTH"],
                {'current_x': 0, 'current_y': 0},
                "SOUTH"
            ),
        )
        for index, (params, final_coordinates, direction) in enumerate(cases):
            with self.subTest(index):
                cmd_place = CommandPlace(params)
                cmd_place.action(dispatcher=self.robot)
                cmd_move = CommandMove()
                cmd_move.action(dispatcher=self.robot)
                self.assertEqual(self.robot.position.__dict__, final_coordinates)
                self.assertEqual(self.robot.direction.name, direction)

    def test_command_left(self):
        cases = (
            (
                ["1", "0", "NORTH"],
                {'current_x': 1, 'current_y': 0},
                "WEST"
            ),
            (
                ["1", "0", "SOUTH"],
                {'current_x': 1, 'current_y': 0},
                "EAST"
            ),
            (
                ["4", "4", "SOUTH"],
                {'current_x': 4, 'current_y': 4},
                "EAST"
            ),
        )
        for index, (params, final_coordinates, direction) in enumerate(cases):
            with self.subTest(index):
                cmd_place = CommandPlace(params)
                cmd_place.action(dispatcher=self.robot)
                cmd_left = CommandLeft()
                cmd_left.action(dispatcher=self.robot)
                self.assertEqual(self.robot.position.__dict__, final_coordinates)
                self.assertEqual(self.robot.direction.name, direction)

    def test_command_right(self):
        cases = (
            (
                ["1", "0", "NORTH"],
                {'current_x': 1, 'current_y': 0},
                "EAST"
            ),
            (
                ["1", "0", "SOUTH"],
                {'current_x': 1, 'current_y': 0},
                "WEST"
            ),
            (
                ["4", "4", "SOUTH"],
                {'current_x': 4, 'current_y': 4},
                "WEST"
            ),
            (
                ["4", "0", "EAST"],
                {'current_x': 4, 'current_y': 0},
                "SOUTH"
            ),
        )
        for index, (params, final_coordinates, direction) in enumerate(cases):
            with self.subTest(index):
                cmd_place = CommandPlace(params)
                cmd_place.action(dispatcher=self.robot)
                cmd_left = CommandRight()
                cmd_left.action(dispatcher=self.robot)
                self.assertEqual(self.robot.position.__dict__, final_coordinates)
                self.assertEqual(self.robot.direction.name, direction)

    def test_command_report(self):
        command_place = CommandPlace(["1", "0", "NORTH"])
        command_place.action(dispatcher=self.robot)
        cmd_report = CommandReport()
        cmd_report.action(dispatcher=self.robot)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    del os.environ["TEST_ENABLED"]
