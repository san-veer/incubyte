import unittest
from craft_control import chandrayaan_3

class TestSpacecraft(unittest.TestCase):
    def test_case(self):

        initial_position = [0, 0, 0]
        initial_direction = 'N'
        commands = ['f']

        returned_position, returned_direction = chandrayaan_3(initial_position, initial_direction, commands)

        expected_position = [0, 1, 0]
        expected_direction = 'N'
        
        self.assertEqual(returned_position, expected_position)
        self.assertEqual(returned_direction, expected_direction)

if __name__ == '__main__':
    unittest.main()