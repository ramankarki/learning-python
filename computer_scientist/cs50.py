from csv import reader, DictReader
from sys import argv

if len(argv) != 3:
    print("Usage: python dna.py sequence.txt database.csv")
    exit()

# read the dna sequence from the file 
with open(argv[2]) as dnafile:
    dnareader = reader(dnafile)
    for row in dnareader:
        dnalist = row

print(dnareader)
print(dnalist)
