#import libraries
import shutil, os
from datetime import datetime

#this function will be used later to make .st_mtime
#a more readable date format for humans
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%d-%b-%Y')
    return formatted_date

#Enter '.' for current directory
#Otherwise enter directory_name/subdirectory_name
path = input("Enter Directory Name:")

#A counter to be used for file naming
counter = 0
#Scan all entries in the given directory
dir_entries = os.scandir(path)
#Loop thru all entries
for entry in dir_entries:
    if entry.is_file(): # if entry is a file
        if entry.name.endswith('png'): # if filename ends with 'png'
            info = entry.stat()
            print(entry.name)
            shutil.move(path+'/'+entry.name, path+'/'+'Image'+str(counter)+'-'+str(convert_date(info.st_ctime))+'.png')
            counter += 1
