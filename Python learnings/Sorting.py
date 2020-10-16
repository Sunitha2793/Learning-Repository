InputArray = [30, 40, 10, 50, 80, 70, 20, 60, 100, 90]

def  selectionsort(InputArray):
    for i in range (0,len(InputArray)):
        if i == len(InputArray):
            break
        else:
            for j in range (i+1,len(InputArray)):
                if j == len(InputArray):
                    break
                elif InputArray[i] > InputArray[j]:
                    temp = InputArray[i]
                    InputArray[i] = InputArray[j]
                    InputArray[j] = temp
    return InputArray

def insertionsort(InputArray):
    for i in range(0, len(InputArray)):
        while (i>=0 and i!=len(InputArray)-1):
            if InputArray[i+1] < InputArray[i]:
                temp = InputArray[i+1]
                InputArray[i+1] = InputArray[i]
                InputArray[i] = temp
            i -= 1
    return InputArray

def bubblesort(InputArray):
    for i in range(len(InputArray)):
        Swap = False
        for j in range(len(InputArray)-1):
            if InputArray[j+1] < InputArray[j]:
                temp = InputArray[j+1]
                InputArray[j+1] = InputArray[j]
                InputArray[j] = temp
                Swap = True
        if Swap == False:
            break
    return InputArray


print("""Select the sort you want to proceed with:
         1. Selection Sort
         2. Insertion Sort
         3. Bubble Sort
         4. Merge Sort
         5. Quick Sort""")
Selection = int(input())
if Selection == 1:
    Output = selectionsort(InputArray)
    print("The elements in Selection Sorted order is:" + str(Output))
elif Selection == 2:
    Output = insertionsort(InputArray)
    print("The elements in Insertion Sorted order is:" + str(Output))
elif Selection == 3:
    Output = bubblesort(InputArray)
    print("The elements in Bubble Sorted order is:" + str(Output))
else:
    print("Invalid selection")














