#!/user/bin/env python3
'''Regex Search
Author: Carissa Jones
'''

import argparse
import os, re, shutil

filenameRegex = re.compile(r'''
^(.*?)
(\d{3})
(.*?)$
''', re.VERBOSE)

folder_path = '~\Documents\courses\hw6\ch10\gaps'
os.chdir(folder_path)

def fill_in_gaps(folder_path):
    '''Given a path to a folder, find all files with a given prefix, such
    as spam001.txt, spam002.txt, and so on, in a single folder(folder_path)
    and locates any gaps in the numbering (such as if there is a 
    spam001.txt and spam003.txt but no spam002.txt). Rename all the later
    files to close this gap.

    Args:
    folder_path (str): Path to a folder in the file system

    Returns:
    None '''
    mo = filenameRegex.search(files)
    beforePart = mo.group(1)
    digitPart = mo.group(2)
    afterPart = mo.group(3)
    print(f'File found {folder_path} is {files}')
    print('Need to rename: ' + digitPart + '\n')

newDigitPart = 1
def fill_in_gaps(folder_path):
    newFilename = beforePart + str(newDigitPart).zfill(3) + afterPart
    newDigitPart += 1
    source = os.path.join(folder_path, files)
    destination = os.path.join(folder_path, newFilename)

    if newFilename in os.listdir(folder_path):
        print(f'{newFilename} already exists!')
    else:
        print(f'Renaming {files} to {newFilename}')
        shutil.move(source, destination)
print('Done')

    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', help='Folder to search for .txt files')

    args = parser.parse_args()

    fill_in_gaps(args.folder)

if __name__ == '__main__':
    main()