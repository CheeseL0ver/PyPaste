#!/usr/bin/python3.7

import sys, os, requests

PASTEBIN_DEV_KEY = os.getenv('PASTEBIN_DEV_KEY')

def readStdin():
    text = ''
    if not sys.stdin.isatty():
        for line in sys.stdin:
           text += line

    return text

def post():
    text = readStdin()
    if text != '' and PASTEBIN_DEV_KEY != None:
        payload = {'api_option': 'paste', 'api_dev_key': PASTEBIN_DEV_KEY, 'api_paste_code': text, 'api_paste_expire_date': '10M'}
        r = requests.post('https://pastebin.com/api/api_post.php', data=payload)
        print("The provided text is now hosted at the following URL {}".format(r.text))

def main():
    post()

if __name__ == '__main__':
    main()
