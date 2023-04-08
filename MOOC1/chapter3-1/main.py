hrs = input("Enter Hours:")
rate = input("Enter rate:")

h = float(hrs)
r = float(rate)
total = 0
if h > 40:
    total = (40 * r) + ((h - 40) * r * 1.5)
else:
    total = h * r

print(total)