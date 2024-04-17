#이것저것 sort
def bubbleSort(a):
    n = len(a)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                swapped = True
                a[j], a[j+1] = a[j+1], a[j]
        if not swapped:
            return

def selectionSort(a):
    for i in range(len(a)):
        min_i = i

        for j in range(i+1, len(a)):
            if a[j] < a[min_i]:
                min_i = j
        (a[i], a[min_i]) = (a[min_i], a[i])

def insertionSort(a):
    if (n := len(a)) <= 1: return
    for i in range(1,n):
        k = a[i]
        j = i - 1
        while j >= 0 and k < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = k
        

b = [6, 4, 2, 1, 22, 9, 17]
s = [6, 4, 2, 1, 22, 9, 17]
i = [6, 4, 2, 1, 22, 9, 17]
bubbleSort(b)
selectionSort(s)
insertionSort(i)
print(b)
print(s)
print(i)
