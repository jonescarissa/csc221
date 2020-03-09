#!/user/bin/env python3
''' Regex Search
Author: Carissa Jones
'''

import argparse
import os, re

def regex_search(folder_path, regex, txt): 
   searchRegex = re.compile(regex)
   result = searchRegex.findall(txt)
   print(result)

while True:
    folder_path = input('Enter the absolute path of the folder')
    if os.path.exists(folder_path) == True:
        print('This folder exists')

folder = os.listdir(folder_path)

for file in folder:
    if file.endswith('.txt'):
        print(os.path.join(folder_path, file), 'r+')
        msg = txtfile.read()
        search(msg)


    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', help='Folder to search for .txt files')
    parser.add_argument('regex', help='Regular expression to search for')

    args = parser.parse_args()

    for line in regex_search(args.folder, args.regex):
        print(line)

if __name__ == '__main__':
    main()
