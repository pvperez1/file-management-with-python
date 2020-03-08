#import libraries
import os, shutil

#Enter '.' for current directory
#Otherwise enter directory_name/subdirectory_name
path = input("Enter Directory Name:")

#Scan all entries in the given directory
dir_entries = os.scandir(path)
file_types = []
#Loop thru all entries
for entry in dir_entries:
    if entry.is_file():
        cleaned_file_ext = os.path.splitext(entry.name)[1][1:].strip().lower()
        if cleaned_file_ext != '':
            file_types.append(cleaned_file_ext)

# Create a set -> unique values
set_of_file_types = set(file_types)

#Create directories
for dir in set_of_file_types:
    os.mkdir(path+'/'+dir+'_files')

#Move the files according to filetype
dir_entries = os.scandir(path)
for entry in dir_entries:
    if entry.is_file():
        cleaned_file_ext = os.path.splitext(entry.name)[1][1:].strip().lower()
        if cleaned_file_ext != '':
            shutil.move(path+'/'+entry.name, path+'/'+cleaned_file_ext+"_files/"+entry.name)
