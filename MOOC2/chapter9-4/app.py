name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"

email_count = dict()

try:
  with open(name, 'r') as file:
    for line in file:
      if line.startswith('From '):
        email = line.split()[1]
        email_count[email] = email_count.get(email, 0) + 1
except:
  print('Cannot open file:', name)
  quit()

most_sent_email = max(email_count, key=email_count.get)

print(most_sent_email, email_count[most_sent_email])