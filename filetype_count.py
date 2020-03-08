# import libraries
import os
# Ask user for inputs
path = input("Enter Directory Name:")
# create file
fhandle = open('file_stats.txt','w')
#declare dictionary
file_dict = {}
#loop thru the list of files and save the count of file type in the dictionary
for folderName, subfolders, filenames in os.walk(path):
    for filename in filenames:
        cleaned_file_extension = os.path.splitext(filename)[1][1:].strip().lower()
        file_dict[cleaned_file_extension] = file_dict.get(cleaned_file_extension,0) + 1

#write the dictionary in a text file
for k,v in file_dict.items():
    fhandle.write(k+' : '+str(v)+'\n')
#save and close file
fhandle.close()
