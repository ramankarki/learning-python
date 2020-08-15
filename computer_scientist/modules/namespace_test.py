import mymodule1, mymodule2

if __name__ == "__main__":
    print("my name is", __name__)
print(mymodule2.myage - mymodule1.myage == mymodule2.year - mymodule1.year)
