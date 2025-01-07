import os

filepath = "."
manga_name = print(os.path.basename(os.path.abspath(filepath)))

for file in os.listdir(filepath):
    oldname = os.path.join(filepath,file)
    newname = os.path.join(filepath,f"{manga_name} - {file}")
    os.rename(oldname,newname)