import unittest
from diskspace import diskspace


class MainTests(unittest.TestCase):

    def test_blocks_0(self):
        blocks = 0
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('0.00B', bytes_size)

    def test_blocks_1(self):
        blocks = 1
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('512.00B', bytes_size)


if __name__ == '__main__':
    unittest.main()