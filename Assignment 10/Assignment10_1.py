import os
def main():
    path = input("Enter the name of Directory: ")
    target_path = "C:/Users/Administrator/Desktop"
    dir_path = os.path.join(target_path, path)
    ext = input("Enter the Extension: ")
    for x in os.listdir(dir_path):
        if x.endswith(ext):
            print(x)
if __name__=="__main__":
    main()


