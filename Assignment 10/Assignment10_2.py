
import os
path=input("Enter the name of Directory: ")
target_path="C:/Users/Administrator/Desktop"
dir_path=os.path.join(target_path,path)
print(dir_path)
ext1="."+input("Enter the first file Extension: ")
ext2="."+input("Enter the second file Extension: ")
print()
list_of_file=0
with os.scandir(dir_path)as files_and_folders:
    for element in files_and_folders:
        if element.is_file():
            #tuple_root_ext=os.path.splitext(element.path)
            #root=tuple_root_ext[0]
            #ext=tuple_root_ext[1]

            root,ext=os.path.splitext(element.path)
            if ext==ext1:
                new_path=root+ext2
                os.rename(element.path,new_path)
                list_of_file+=1
print()
print("no of file processed:{}".format(list_of_file))
print("Extension:from {} to {}".format(ext1,ext2))






list_of_file=os.listdir(dir_path)
for file in list_of_file:
    if file.endswith(ext1):
        os.rename(file,ext1+".txt")
print(os.listdir(dir_path))

