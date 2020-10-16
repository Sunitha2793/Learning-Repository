InputArray = ['30', '40', '10', '50', '80', '70', '20', '60', '100', '90']

def linearsearch(InputValue):
    count = 0
    for i in InputArray:
        if i == InputValue:
            return count
        else:
            count += 1
    return 0


print("Enter an element between 10 and 100 in multiples of 10")
InputValue = input()
Index = linearsearch(InputValue)
if Index != 0:
    print('Element is found at index ' + str(Index))
else:
    print('Element entered is not valid')







