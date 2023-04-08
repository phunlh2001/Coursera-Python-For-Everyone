# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('Cannot open file:', fname)
    quit()

    
count = 0
length = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.rstrip()
    length = length + 1
    pos = line[line.find(':')+2:]
    count = count + float(pos)

print('Average spam confidence:', count / length)
