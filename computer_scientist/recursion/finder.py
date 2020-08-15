import os, os.path
from sys import argv


# returns the list of files and directories of the path
def get_dirlist(path="/home"):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


# returns the each and every list of files with fullpath of the current path
def return_all_file_path(path="/home"):
    fullpath_list = []
    if os.path.exists(path):
        dirlist = get_dirlist(path)
        for fd in dirlist:
            fullpath = os.path.join(path, fd)
            if os.path.isdir(fullpath):
                fullpath_list.extend(return_fullpath(fullpath))
            else:
                fullpath_list.append(fullpath)
        return fullpath_list


# removes user given files from the current path
def search_files(file_name, path="/home"):
    files = []
    path_list = sorted(return_all_file_path(path))

    if path_list != None and len(path_list) != 0:
        print()
        for element in path_list:
            if element.endswith(file_name):
                print(element)
                files.append(element)

    print(f"Total:{len(files)}", file_name, "in", path)
    return files


def remove_files(file_name, path="/home", remove=False):
    files = search_files(file_name, path)
    if len(files) > 0 and remove:
        ask = input("\nDo you want to delete these files? [y/n] ")
        if ask.lower() == "y" or ask.lower() == "yes":
            print() # newline
            for element in files:
                print("removing", element)
                os.remove(element)
            print("Completed")


if len(argv) == 3:
    search_files(argv[1], argv[2])
elif len(argv) == 4 and argv[3] == "rm":
    remove_files(argv[1], argv[2], argv[3])
else:
    print("Usage: python finder.py file-extension filepath/directory [rm]")


# Search files using extension
