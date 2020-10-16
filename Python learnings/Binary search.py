InputArray = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def binarysearch(InputArray,low,High,InputValue):
    if High >= low:
        mid = int((low + High) / 2)

        if InputArray[mid] == InputValue:
            return mid;
        elif InputArray[mid] < InputValue:
            return binarysearch(InputArray, mid + 1, High, InputValue)
        else:
            return binarysearch(InputArray, low, mid - 1, InputValue)

    else:
          return 0



print('enter an integer between 10 and 100 in multiples of 10')
InputValue = int(input())
Index = binarysearch(InputArray, 0, int(len(InputArray)), InputValue)
if Index == 0:
    print('Element not available in array')
else:
    print('Element is available at index '+str(Index))
