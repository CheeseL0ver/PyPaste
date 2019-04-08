import sys

text = ''

if not sys.stdin.isatty():
    for line in sys.stdin:
        text += line

if text != '':
    print (text)

