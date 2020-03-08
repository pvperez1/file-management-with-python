# import libraries
import glob, os
# Ask user for inputs
path = input("Enter Directory Name:")
filetype = input("What filetype are you looking for?").strip().lower()
#glob.glob returns an iterator object
files = glob.iglob(path+'/**/'+'*.'+filetype, recursive=True)
# create file
fhandle = open(filetype+'_list.txt','w')
#loop thru the list of files and write it in the txt file
for f in files:
    fhandle.write(f+'\n')
#save and close the text file
fhandle.close()
