import random


def bubbleSort(items:list):
    swaps = 0
    comparisons = 0

    return items, swaps, comparisons

def insertionSort(items: list):
    swaps = 0
    comparisons = 0

    return items, swaps, comparisons

def selectionSort(items : list):
    swaps = 0
    comparisons = 0

    return items, swaps, comparisons


y = [9,8,7,6,5,4,3,2,1]
print(bubbleSort(y.copy()))
print(insertionSort(y.copy()))
print(selectionSort(y.copy()))
print()
x = [x for x in range(50)]
random.shuffle(x)
print(bubbleSort(x.copy()))
print(insertionSort(x.copy()))
print(selectionSort(x.copy()))
