#code adapted from http://automatetheboringstuff.com/2e/chapter10/
#import library
import os

#Enter '.' to specify current directory
#Otherwise enter directory_name/subdirectory_name
directory = input("Enter directory:")

#create text file
fname = "all_listings.txt"
fhandle = open(fname,'w')

#loop using os.walk()
for folderName, subfolders, filenames in os.walk(directory):
    fhandle.write('The current folder is ' + folderName+'\n')
    for subfolder in subfolders:
        fhandle.write('SUBFOLDER OF ' + folderName + ': ' + subfolder+'\n')
    for filename in filenames:
        fhandle.write('FILE INSIDE ' + folderName + ': '+ filename+'\n')
    fhandle.write('---------------------------\n')
