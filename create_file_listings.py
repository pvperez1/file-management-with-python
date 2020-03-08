#import necessary libraries
from datetime import datetime
import os
import pathlib

#this function will be used later to make .st_mtime
#a more readable date format for humans
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%d %b %Y')
    return formatted_date

#Enter '.' if you want to create listings in the current Directory
#Otherwise, enter 'directory_name/subdirectory_name'
basepath = input("Enter Directory:")
cur_directory = pathlib.Path(basepath)

#Creates a CSV file named listings.csv
filename = "listings.csv"
fhandler = open(filename,'w')
fhandler.write("Filename,Last Modified,File Size (bytes)\n")

#loop through the files in the specified directory
dir_entries = os.scandir(cur_directory)
for entry in dir_entries:
    if entry.is_file():
        info = entry.stat()
        fhandler.write(entry.name+","+str(convert_date(info.st_mtime))+","+str(info.st_size)+"\n")

#save and close the file listing
fhandler.close()
