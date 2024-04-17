a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def binSearch(d):
    start = 0
    end = len(a) - 1

    while (start <= end):
        mid = (start + end)//2
        if a[mid] == d:
            print("find")
            return
        else:
            if a[mid] > d: end = mid - 1
            else: start = mid + 1
    print('not found')


binSearch(int(input("찾는 값: ")))
