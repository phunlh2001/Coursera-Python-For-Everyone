largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    if num == "done":
        break
    
    try:
        num = int(num)
        if largest is None or num > largest:
            largest = num

        if smallest is None or num < smallest:
            smallest = num
    except ValueError:
        print('Invalid input')
        continue

if largest is not None and smallest is not None:
    print('Maximum is', largest)
    print('Minimum is', smallest)