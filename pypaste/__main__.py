#!/usr/bin/python3.7

import sys, os, requests, argparse

PASTEBIN_DEV_KEY = os.getenv('PASTEBIN_DEV_KEY')

def paramParse():
    parser = argparse.ArgumentParser(description='Optional params for Pastebin Pastes')
    parser.add_argument('-t', '--title', help='Title/Name of the paste')
    parser.add_argument('-e', '--expire', help='Time until paste expiration (default is 10 minutes)')
    parser.add_argument('-v', '--visibility', help='Visibility of paste public=0 unlisted=1 private=2 (default is 0)')
    args = parser.parse_args()
    return args

def generatePayload(text):
    args = paramParse()
    payload = {'api_option': 'paste', 
               'api_dev_key': PASTEBIN_DEV_KEY,
               'api_paste_code': text,
               'api_paste_expire_date': args.expire or '10M',
               'api_paste_name': args.title or '',
               'api_paste_private': args.visibility or '0'
               }
    return payload

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

def post(payload):
    r = requests.post('https://pastebin.com/api/api_post.php', data=payload)
    if requestError(r.text):
        print ("An error occured: {}".format(r.text))
        return 1
    print("The provided text is now hosted at the following URL {}".format(r.text))
    return 0

def generateUserKey(user, password):
    payload = {'api_dev_key': PASTEBIN_DEV_KEY, 'api_user_name': user, 'api_user_password': password}
    r = requests.post("https://pastebin.com/api/api_login.php", data=payload)
    if requestError(r.text):
        print ("An error occured: {}".format(r.text))
        return

def main():
    text = readStdin()
    if text != '' and PASTEBIN_DEV_KEY != None:
        payload = generatePayload(text)
        post(payload)
        return 0
    return 1

if __name__ == '__main__':
    main()
