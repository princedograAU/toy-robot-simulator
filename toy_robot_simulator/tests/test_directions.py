import unittest
import test_setup

# Relative path
from simulator.direction import Direction, InvalidDirection


class TestDirection(unittest.TestCase):

    def test_direction(self):
        direction = Direction("NORTH")
        self.assertEqual(direction.name, "NORTH")

    def test_invalid_direction(self):
        with self.assertRaises(InvalidDirection) as ex:
            Direction("NO-DIRECTION")
        self.assertTrue(str(ex.exception), "invalid direction: NO-DIRECTION")

    def test_invalid_direction_change(self):
        direction = Direction("NORTH")
        with self.assertRaises(InvalidDirection) as ex:
            direction.name = "NO-DIRECTION"
        self.assertTrue(str(ex.exception), "invalid direction: NO-DIRECTION")

    def test_valid_direction_change(self):
        direction = Direction("NORTH")
        self.assertTrue(direction.name, "NORTH")
        direction.name = "SOUTH"
        self.assertTrue(direction.name, "SOUTH")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
