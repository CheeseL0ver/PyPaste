import unittest
from pypaste.__main__ import post
class TestSum(unittest.TestCase):

  def testPaste(self):
    self.assertEqual(post(), 0, 'Should be zero.')

if __name__ == '__main__':
  unittest.main()