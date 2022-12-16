
import shutil
import os
path=input("Enter the name of first Directory: ")
src_path="C:/Users/Administrator/Desktop"
dir_path=os.path.join(src_path,path)
print(dir_path)
path2=input("Enter the name of second Directory: ")
mkdir="C:/Users/Administrator/Desktop"
print(mkdir)
dir_path2=os.path.join(mkdir,path2)
files=os.listdir(dir_path)
print(files)
shutil.copytree(dir_path,dir_path2)
