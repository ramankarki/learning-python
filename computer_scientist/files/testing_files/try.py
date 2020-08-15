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

# myfile = open("/usr/share/dict/words", "r")
# content = myfile.readlines()
# print(content[102773])
# myfile.close()

#############################################################################################

# import urllib.request

# url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
# destination_filename = "download.txt"
# urllib.request.urlretrieve(url, destination_filename)

#############################################################################################

import urllib.request

def retrieve_page(url):
    ''' Retrieve the contents of a web page.
    The contents is converted to a string before returning it.
    '''
    my_socket = urllib.request.urlopen(url)
    dta = my_socket.readlines()
    my_socket.close()
    return dta

the_text = retrieve_page("https://www.w3.org/TR/PNG/iso_8859-1.txt")
myfile = open("download.txt", "w")
for i in range(len(the_text)):
    print(the_text[i].decode("utf-8").strip())
    content = the_text[i].decode("utf-8")
    myfile.write(content)
myfile.close()
