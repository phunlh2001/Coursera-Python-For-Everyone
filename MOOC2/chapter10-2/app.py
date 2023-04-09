name = input("Enter file: ")
if len(name) < 1:
   name = "mbox-short.txt"

hour_count = dict()

try:
   with open(name, 'r') as file:
      for line in file:
         if line.startswith("From "):
            words = line.split()
            time = words[5]
            hour = time.split(":")[0]
            hour_count[hour] = hour_count.get(hour, 0) + 1
   for hour, count in sorted(hour_count.items()):
      print(hour, count)
except:
   print('Cannot open file:', name)
   quit()
