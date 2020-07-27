import os
import unittest
import pypaste.__main__ as paste
class TestSum(unittest.TestCase):

  PASTEBIN_DEV_KEY = os.getenv('PASTEBIN_DEV_KEY')
  PASTEBIN_USER_KEY = os.getenv('PASTEBIN_USER_KEY')

  def testPaste(self):
    self.assertEqual(paste.main(), 0, 'Should be zero.')

  '''def testPrivate(self):
    payload = {'api_option': 'paste',
               'api_dev_key': self.PASTEBIN_DEV_KEY,
               'api_paste_code': 'TESTING',
               'api_paste_expire_date': '10M',
               'api_paste_name': '',
               'api_paste_private': '2',
               'api_user_key': self.PASTEBIN_USER_KEY
              }
    self.assertEqual(paste.post(payload), 0, 'Private post failed.')
  '''

  def testUnlisted(self):
    payload = {'api_option': 'paste',
               'api_dev_key': self.PASTEBIN_DEV_KEY,
               'api_paste_code': 'TESTING',
               'api_paste_expire_date': '10M',
               'api_paste_name': '',
               'api_paste_private': '1'
              }
    self.assertEqual(paste.post(payload), 0, 'Unlisted post failed.')

  def testTitle(self):
    payload = {'api_option': 'paste',
               'api_dev_key': self.PASTEBIN_DEV_KEY,
               'api_paste_code': 'TESTING',
               'api_paste_expire_date': '10M',
               'api_paste_name': 'TEST TITLE',
               'api_paste_private': '1'
              }
    self.assertEqual(paste.post(payload), 0, 'Titled post failed.')

  '''def testExpiration(self):
    expirations = ['N','10M','1H','1D','1W','2W','1M','6M','1Y']
    for expiration in expirations:
        payload = {'api_option': 'paste',
                   'api_dev_key': self.PASTEBIN_DEV_KEY,
                   'api_paste_code': 'TESTING EXPIRATION',
                   'api_paste_expire_date': expiration,
                   'api_paste_name': '',
                   'api_paste_private': '1'
                  }
        self.assertEqual(paste.post(payload), 0, 'Post with expiration {} failed.'.format(expiration))
   '''
if __name__ == '__main__':
  unittest.main()
