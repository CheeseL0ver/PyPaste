#!/usr/local/bin/python3.7

import sys, requests

class Main():
    text = ''
    PASTEBIN_DEV_KEY = ''

    def readStdin(self):
        if not sys.stdin.isatty():
            for line in sys.stdin:
                self.text += line

    def post(self):
        payload = {'api_option': 'paste', 'api_dev_key': self.PASTEBIN_DEV_KEY, 'api_paste_code': self.text}
        r = requests.post('https://pastebin.com/api/api_post.php', data=payload)
        print(r.text)

    def main(self):
        self.readStdin()
        if self.text != '':
            #print (self.text)
            self.post()

if __name__ == '__main__':
    Main().main()
