
def partition(list, low, high):
    list[0] = list[low]
    while low < high:
        while (low < high) and (list[high] > list[0]):
            high = high - 1
        if low < high:
            list[low] = list[high]
            low = low + 1
        while (low < high) and (list[low] < list[0]):
            low = low + 1
        if low < high:
            list[high] = list[low]
            high = high - 1
    list[high] = list[low]
    return high

def QuickSort(list, low, high):     #默认第0项为哨兵项
    if low < high:
        t = partition(list, low, high)
        QuickSort(list, low, t-1)
        QuickSort(list, t+1, high)

def main():
    list = [ 0.0, 6.0, 2.2, 7.2, 4.0, 9.0, 0.8, 5.0, 6.0 ]
    print(list[1::])
    QuickSort(list, 1, len(list)-1)
    print(list[1::])

if __name__ == '__main__':
    print(__name__)
    main()
