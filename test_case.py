import unittest
from craft_control import chandrayaan_3

class TestSpacecraft(unittest.TestCase):
    def test_case(self):
        result = chandrayaan_3()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()