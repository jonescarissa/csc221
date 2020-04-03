#!/usr/bin/env python
''' Link Verification
Author: Carissa Jones
'''

import argparse
import requests
import bs4

def verfiy_links(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
        soup = bs.BeautifulSoup(res.text, 'html.parser')
        pageLinks = [link.get('href') for link in soup.select('a')
                    if link.get('href')]
        
        brokenCount = 0
        goodCount = 0

        for link in pageLinks:
            if link.startswith('http'):
                res2 = requests.get(link)

                try:
                    res2.raise_for_status()
                    print(f'Good: {link}')
                    goodCount += 1

                except Exception as exc:
                    print(f'Broken: {link}')
                    brokenCount += 1

        print(f'{goodCount} Good {brokenCount} Broken')

    except Exception as exc:
        print('There was a problem: %s' % (exc))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help = 'URL to verify links')

    args = parser.parse_args()

    verfiy_links(args.url)

if __name__ == '__main__':
    main()
    