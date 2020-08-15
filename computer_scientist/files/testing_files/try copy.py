# myfile = open("text.py", "r")
# myfile.write("my first file written from python\n")
# myfile.write("---------------------------------\n")
# myfile.write('''print("hello world")\n''')
# myfile.close()

#############################################################################################

# while True:
#     line = myfile.readline() #
#     if len(line) == 0:
#         break
#     print(line.strip())
# myfile.close()

#############################################################################################

# myfile2 = open("helloworld.txt", "w")
# line = myfile.readlines() #
# myfile.close()

# for i in line:
#     myfile2.write(i)
# myfile2.close()

#############################################################################################

# myfile3 = open("helloworld.zip", "rb")
# myfile4 = open("test.zip", "wb")
# content = myfile3.read() #
# myfile4.write(content)
# myfile3.close()
# myfile4.close()

#############################################################################################

myfile = open("try.py", "r")
myfile1 = open("filtered.py", "w")
while True:
    content = myfile.readline()
    if len(content) ==  0:
        break
    if content[0] == "#":
        continue
    myfile1.write(content)
myfile.close()
myfile1.close()