def cp(old_file):
    '''
    file1:
    a
    b
    c
    
    file2:
    c
    b
    a
    '''
    old_myfile = open(old_file, "r")
    new_myfile = open(f"new_{old_file}", "w")

    content = old_myfile.readlines()
    for i in range(len(content)-1, -1, -1):
        new_myfile.write(content[i])
        
    old_myfile.close()
    new_myfile.close()


def print_line_snake(file_name):
    '''
    print the line that contains snake
    '''
    myfile = open(file_name, "r")
    content = myfile.readlines()
    for i in content:
        if "snake" in i:
            print(i)
    myfile.close()


def numbering_file(file_name):
    '''
    print 4 digit numbering before starting the lines i.e. 
    0000
    0001
    .
    .
    9999
    '''
    first = 0
    second = 0
    third = 0
    forth = 0
    myfile = open(file_name, "r")
    myfile1 = open(f"num_{file_name}", "w")
    content = myfile.readlines()
    for i in range(1, len(content)+1):
        first = i // 1000
        second = (i - first * 1000) // 100
        third = (i - first * 1000 - second * 100) // 10
        forth = (i - first * 1000 - second * 100 - third * 10)
        num = f"{first}{second}{third}{forth} "
        myfile1.write(num + content[i-1])
    myfile.close()
    myfile1.close()


def unnumbering_file(file_name):
    myfile = open(file_name, "r")
    myfile1 = open(f"unnum_{file_name}", "w")
    while True:
        content = myfile.readline()
        if len(content) == 0:
            break
        cut = content.find(" ")
        content = content[cut+1:]
        myfile1.write(content)
    myfile.close()
    myfile1.close()



unnumbering_file("num_download.txt")
# cp("download.txt")
# print_line_snake("download.txt")
