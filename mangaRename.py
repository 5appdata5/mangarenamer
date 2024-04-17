import os

manga_name = input("Whats the name of the manga:")
filepath = input("Whats the directory path:")

for file in os.listdir(filepath):
    oldname = os.path.join(filepath,file)
    newname = os.path.join(filepath,f"{manga_name} - {file}")
    os.rename(oldname,newname)