score = input("Enter Score: ")

try:
    score = float(score)
except:
    print('Not a number')
    quit()

if score > 1 or score < 0:
    print('out of range')
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.5:
    print('D')
else:
    print('F')