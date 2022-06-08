import brutescrap
import sys

if len(sys.argv) > 1 and sys.argv[1] in ('-g', '--get'):
    if len(sys.argv) > 2:
        brutescrap.get(sys.argv[2])
else:
    print('Usage: python -m brutescrap [-g | --get] [url] [browser]')
    print()
    print('Supported browser: msedge, firefox, chrome')
    print('If a website is successfully fetched, the page source ')
    print('will be copied to the clipboard. Paste the text into ')
    print('any text editor to view it. The page source has not been')
    print('parsed, so parsing had to be done manually.')
