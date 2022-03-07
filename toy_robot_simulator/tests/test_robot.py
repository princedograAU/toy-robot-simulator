import unittest
import test_setup

# Relative path
from simulator.table import Table
from simulator.robot import Robot, MissingPosition
from simulator.position import Position, InvalidPosition
from simulator.direction import Direction, InvalidDirection


class TestRobot(unittest.TestCase):
    def setUp(self) -> None:
        self.table = Table(5, 5)
        self.robot = Robot(self.table)

    def test_place_robot(self):
        self.robot.place(Direction("NORTH"), Position(0, 0))
        self.assertEqual(self.robot.position.__dict__, {'current_x': 0, 'current_y': 0})
        self.assertEqual(self.robot.direction.name, "NORTH")

    def test_invalid_coordinates_robot(self):
        with self.assertRaises(InvalidPosition):
            self.robot.place(Direction("NORTH"), Position(-1, 0))

    def test_invalid_direction_robot(self):
        with self.assertRaises(InvalidDirection):
            self.robot.place(Direction("NO-DIRECTION"), Position(0, 0))

    def test_robot_command_move(self):
        self.robot.place(Direction("NORTH"), Position(0, 0))
        self.assertEqual(self.robot.position.__dict__, {'current_x': 0, 'current_y': 0})
        self.assertEqual(self.robot.direction.name, "NORTH")
        self.robot.action_move()
        self.assertEqual(self.robot.position.__dict__, {'current_x': 0, 'current_y': 1})

    def test_robot_boundary_conditions(self):
        self.robot.place(Direction("SOUTH"), Position(0, 0))
        self.assertEqual(self.robot.position.__dict__, {'current_x': 0, 'current_y': 0})
        self.assertEqual(self.robot.direction.name, "SOUTH")
        self.robot.action_move()
        self.assertEqual(self.robot.position.__dict__, {'current_x': 0, 'current_y': 0})
        self.assertEqual(self.robot.direction.name, "SOUTH")

    def test_robot_command_move_with_missing_position(self):
        with self.assertRaises(MissingPosition):
            self.robot.action_move()

    def test_robot_command_left(self):
        self.robot.place(Direction("NORTH"), Position(0, 0))
        self.robot.action_rotate(1)
        self.assertEqual(self.robot.direction.name, "WEST")
        self.robot.action_rotate(1)
        self.assertEqual(self.robot.direction.name, "SOUTH")
        self.robot.action_rotate(1)
        self.assertEqual(self.robot.direction.name, "EAST")

    def test_robot_command_right(self):
        self.robot.place(Direction("NORTH"), Position(0, 0))
        self.robot.action_rotate(-1)
        self.assertEqual(self.robot.direction.name, "EAST")
        self.robot.action_rotate(-1)
        self.assertEqual(self.robot.direction.name, "SOUTH")
        self.robot.action_rotate(-1)
        self.assertEqual(self.robot.direction.name, "WEST")

    def test_robot_command_in_combination(self):
        self.robot.place(Direction("NORTH"), Position(0, 0))
        self.robot.action_rotate(-1)
        self.assertEqual(self.robot.direction.name, "EAST")
        self.robot.action_rotate(1)
        self.assertEqual(self.robot.direction.name, "NORTH")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)