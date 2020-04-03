#!/usr/bin/env python3
# mapIt.py - Launches a map in the browser using an address from the 
# command line or clipboard

import webbrowser
import sys
import argparse
import pyperclip

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('address', nargs='?')

    args = parser.parse_args()
    return args

def main():
    args = get_args()

    print('The given address:', args.address)

    if args.address is None: # Pull it from clipboard
        address = pyperclip.paste() 
    else:
        address = args.address

    webbrowser.open(
        'http://www.google.com/maps/place/' + address
    )

if __name__ == '__main__':
    main()