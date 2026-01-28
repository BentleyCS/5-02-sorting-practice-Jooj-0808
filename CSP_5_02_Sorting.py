import random


def bubbleSort(items:list):
    n = len(items)
    swaps = 0
    comparisons = 0
    changed = True
    while changed:
        changed = False
        for j in range(n - 1):
            comparisons += 1
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swaps += 1
                changed = True
    return items, swaps, comparisons

def insertionSort(items: list):
    n = len(items)
    swaps = 0
    comparisons = 0

    for i in range(1, n):
        j = i
        while j > 0:
            comparisons += 1
            if items[j] < items[j - 1]:
                items[j], items[j - 1] = items[j - 1], items[j]
                swaps += 1
                j -= 1
            else:
                break

    return items, swaps, comparisons

def selectionSort(items : list):
    n = len(items)
    swaps = 0
    comparisons = 0

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if items[j] < items[min_idx]:
                min_idx = j

        items[i], items[min_idx] = items[min_idx], items[i]
        swaps += 1

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
