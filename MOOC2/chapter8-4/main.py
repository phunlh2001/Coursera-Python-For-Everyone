fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Cannot open file:', fname)
    quit()

lst = list()
for line in fh:
    words = line.rstrip().split()
    for word in words:
        if word not in lst:
            lst.append(word)
    

lst.sort()
print(lst)
