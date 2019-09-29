#!/usr/bin/python3.7

import sys, os, requests

PASTEBIN_DEV_KEY = os.getenv('PASTEBIN_DEV_KEY')


def requestError(response):
    if 'Bad API request' in response:
        return True
    return False

def readStdin():
    text = ''
    if not sys.stdin.isatty():
        for line in sys.stdin:
           text += line
    print("INPUT: %s" % text)

    return text

def post():
    text = readStdin()
    if text != '' and PASTEBIN_DEV_KEY != None:
        payload = {'api_option': 'paste', 'api_dev_key': PASTEBIN_DEV_KEY, 'api_paste_code': text, 'api_paste_expire_date': '10M'}
        r = requests.post('https://pastebin.com/api/api_post.php', data=payload)
        if requestError(r.text):
            print ("An error occured: {}".format(r.text))
            return
        print("The provided text is now hosted at the following URL {}".format(r.text))

def generateUserKey(user, password):
    payload = {'api_dev_key': PASTEBIN_DEV_KEY, 'api_user_name': user, 'api_user_password': password}
    r = requests.post("https://pastebin.com/api/api_login.php", data=payload)
    if requestError(r.text):
        print ("An error occured: {}".format(r.text))
        return
    #r.text is the user key, store it securely in keychain

def main():
    post()

if __name__ == '__main__':
    main()
