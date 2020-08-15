import os, os.path


# returns the list of files and directories of the path
def get_dirlist(path="/home"):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


# returns the each and every list of files with fullpath of the current path
def return_fullpath(path="/home"):
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


# creates trash files in every sub_directories from the current directory
def create_trash(file_name, path):
    if os.path.exists(path):
        dirlist = get_dirlist(path)
        file = open(path + "/" + file_name, "w+")
        file.write("this is trash")
        file.close()
        for element in dirlist:
            fullpath = os.path.join(path, element)
            if os.path.isdir(fullpath):
                create_trash(file_name, fullpath)


# removes user given files from the current path
def search_file(file_name, path="/home", remove=False):
    files = []
    path_list = sorted(return_fullpath(path))

    if path_list != None and len(path_list) != 0:
        print()
        for element in path_list:
            if element.endswith(file_name):
                print(element)
                files.append(element)

    print(f"Total:{len(files)}", file_name, "in", path)
    if len(files) > 0 and remove:
        ask = input("\nDo you want to delete these files? [y/n] ")
        if ask.lower() == "y" or ask.lower() == "yes":
            print() # newline
            for element in files:
                print("removing", element)
                os.remove(element)
            print()



search_file(".ttf", "/home")
# create_trash("trash.txt", "/home/raman/python/test")

