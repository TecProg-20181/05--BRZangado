import unittest
from diskspace import diskspace


class BytesSizeTests(unittest.TestCase):

    def test_blocks_0(self):
        blocks = 0
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('0.00B', bytes_size)

    def test_blocks_1(self):
        blocks = 1
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('512.00B', bytes_size)

    def test_return_type(self):
        blocks = 0
        bytes_size = diskspace.bytes_to_readable(blocks)
        self.assertIsInstance(bytes_size, str)

    def test_labels_0(self):
        blocks = 10000000000
        bytes_size = diskspace.bytes_to_readable(blocks)
        label = bytes_size[-2:]
        self.assertEqual('Tb', label)

    def test_labels_1(self):
        blocks = 10000000
        bytes_size = diskspace.bytes_to_readable(blocks)
        label = bytes_size[-2:]
        self.assertEqual('Gb', label)

    def test_labels_2(self):
        blocks = 100000
        bytes_size = diskspace.bytes_to_readable(blocks)
        label = bytes_size[-2:]
        self.assertEqual('Mb', label)

    def test_labels_3(self):
        blocks = 1000
        bytes_size = diskspace.bytes_to_readable(blocks)
        label = bytes_size[-2:]
        self.assertEqual('Kb', label)

    def test_labels_3(self):
        blocks = 1
        bytes_size = diskspace.bytes_to_readable(blocks)
        label = bytes_size[-1:]
        self.assertEqual('B', label)


if __name__ == '__main__':
    unittest.main()