
def BinaryInsertSort(list):     #默认第0项为哨兵项
    size = len(list)
    for i in range(2, size):
        list[0] = list[i]
        high = i - 1
        low = 1
        while low <= high:
            middle = int(( high + low ) / 2)
            if list[0] > list[middle]:
                low = middle + 1
            else:
                high = middle - 1
        j = i - 1
        while j >= ( high + 1 ):
            list[j+1] = list[j]
            j = j - 1
        list[high+1] = list[0]

def main():
    list = [ 0.0, 6.0, 2.2, 7.2, 4.0, 9.0, 0.8, 5.0, 6.0 ]
    print(list[1::])
    BinaryInsertSort(list)
    print(list[1::])

if __name__ == '__main__':
    print(__name__)
    main()
