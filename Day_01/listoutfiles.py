import os
import glob
import pathlib

def main():
    print("List out the files")
    
    folder_paths = input("Enter a list of folders name separated by spaces: ").split()
    file_format = input("please enter the which file format want to list out: ")

    """
    'glob' module
    The glob module finds all the pathnames matching a specified pattern
    glob.glob() function to achieve our task but without recursion
    """

    for path in folder_paths:
        files = glob.glob(path+"/*."+file_format)#os.listdir(path)
        if files:
            for file in files:
                print(file)

    """
    'pathlib' module
    Recursively Listing With pathlib.rglob()
    """
    print("pathlib module - Recursively Find all Files in Current and Subfolders")
    for path in folder_paths:
        flist = pathlib.Path(path)
        lst = flist.rglob("*."+file_format)
        for i in lst:
            print(i)

if __name__ == "__main__":
    main()