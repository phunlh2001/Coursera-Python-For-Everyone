# Use words.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('File cannot be opened', fname)
    quit()

for line in fh:
    print(line.rstrip().upper())