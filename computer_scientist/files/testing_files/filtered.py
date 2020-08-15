# filtered from try.py file using "try copy.py" script






myfile3 = open("helloworld.zip", "rb")
myfile4 = open("test.zip", "wb")
content = myfile3.read() #
myfile4.write(content)
myfile3.close()
myfile4.close()

