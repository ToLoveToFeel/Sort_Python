
def SimpleSelectSort(list):     #默认第0项为哨兵项
    size = len(list)
    for i in range(1, size-1):
        min = i
        for j in range(i+1, size):
            if list[j] < list[min]:
                min = j
        if min != i:
            list[0] = list[i]
            list[i] = list[min]
            list[min] = list[0]

def main():
    list = [ 0.0, 6.0, 2.2, 7.2, 4.0, 9.0, 0.8, 5.0, 6.0 ]
    print(list[1::])
    SimpleSelectSort(list)
    print(list[1::])

if __name__ == '__main__':
    print(__name__)
    main()
