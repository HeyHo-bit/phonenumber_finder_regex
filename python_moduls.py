from zipfile import ZipFile 
import os
import re

file_name = "unzip_me_for_instructions.zip"
newfilename = 'result.txt'

def search(file,pattern= r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'):
    f = open(file,'r')
    text = f.read()
    
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''
    
with ZipFile(file_name, 'r') as zip:

    #zip.printdir() 
  
    # extracting all the files 
    print('Extracting all the files now...') 
    zip.extractall() 
    print('Done!') 
    print('\n')

with open('extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)

results = []
for folder , sub_folders , files in os.walk(os.getcwd() + "\\extracted_content"):
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+ f)
        full_path = folder+'\\'+f
        results.append(search(full_path)) 
    
print("The secret phone number is: ")
for r in results:
    if r != '':
        print(r.group())