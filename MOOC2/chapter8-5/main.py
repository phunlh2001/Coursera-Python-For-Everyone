fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    print('Cannot open file:', fname)
    quit()

count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('From:'):
        count = count + 1
        email = line.split()[1]
        print(email)

print("There were", count, "lines in the file with From as the first word")