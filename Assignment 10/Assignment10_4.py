import shutil
import os
import glob
path=input("Enter the name of first Directory: ")
src_path="C:/Users/Administrator/Desktop"
dir_path=os.path.join(src_path,path)
print(dir_path)
path2=input("Enter the name of second Directory: ")
des_path=os.path.join(src_path,path2)
os.mkdir(des_path)
print(des_path)
ext1="."+input("Enter the file Extension: ")

srcfile=os.listdir(dir_path)
for file in srcfile:
    if file.endswith(ext1):
        shutil.copy(os.path.join(dir_path,file),os.path.join(des_path,file))