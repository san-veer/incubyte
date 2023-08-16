import unittest
from craft_control import chandrayaan_3

class TestSpacecraft(unittest.TestCase):
    def test_case(self):
        commands = []
        expected_position = [0, 0, 0]
        expected_direction = 'N'

        returned_position, returned_direction = chandrayaan_3(expected_position, expected_direction, commands)
        
        self.assertEqual(expected_position, returned_position)
        self.assertEqual(expected_direction, returned_direction)

if __name__ == '__main__':
    unittest.main()