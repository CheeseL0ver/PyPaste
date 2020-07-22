import unittest
from pypaste.__main__ import main
class TestSum(unittest.TestCase):

  def testPaste(self):
    self.assertEqual(main(), 0, 'Should be zero.')

if __name__ == '__main__':
  unittest.main()
