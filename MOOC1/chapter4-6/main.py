def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
    return pay

hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

pay = computepay(hours, rate)
print("Pay {:.2f}".format(pay))