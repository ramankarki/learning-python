def ft(string):
    lines = string.lower()
    text = lines.split()
    ft_table = dict()
    ft_list = []

    for letter in text:
        ft_table[letter] = ft_table.get(letter, 0) + 1

    for k,v in ft_table.items():
        ft_list.append((k,v))

    return sorted(ft_list)


def word_book(file_name):
    myfile = open(file_name, "r")
    myword = myfile.read()
    myfile.close()
    return ft(myword)


def print_wordlist(ft_table):
    myfile = open("record.txt", "w")
    myfile.write("   word\t\tcount\n")
    myfile.write("====================\n\n")
    for k,v in ft_table:
        print(k,"\t",v)
        myfile.write(f"{k}\t\t{v}\n")
    myfile.close()


print_wordlist(word_book("file.txt"))

