
def HeapAdjust(list, m, n):     #默认第0项为哨兵项
    list[0] = list[m]
    i = 2 * m
    while i <= n:
        if i < n and list[i] < list[i+1]:
            i = i + 1
        if list[0] > list[i]:
            break
        list[m] = list[i]
        m = i
        i *= 2
    list[m] = list[0]

def HeapSort(list):
    size = len(list) - 1
    for i in range((int(size / 2)), 0, -1):     #建堆
        HeapAdjust(list, i, size)
    for i in range(size, 1, -1):        #排序
        list[0] = list[i]
        list[i] = list[1]
        list[1] = list[0]
        HeapAdjust(list, 1, i-1)

def main():
    list = [ 0.0, 6.0, 2.2, 7.2, 4.0, 9.0, 0.8, 5.0, 6.0 ]
    print(list[1::])
    HeapSort(list)
    print(list[1::])

if __name__ == '__main__':
    print(__name__)
    main()
