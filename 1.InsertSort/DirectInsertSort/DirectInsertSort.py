
def DirectInsertSort(list):     #默认第0项为哨兵项
    size = len(list)
    for i in range(2, size):
        if list[i] < list[i-1]:
            list[0] = list[i]
            list[i] = list[i-1]
            j = i - 2
            while list[j] > list[0]:
                list[j+1] = list[j]
                j = j - 1;
            list[j+1] = list[0]

def main():
    list = [ 0.0, 6.0, 2.2, 7.2, 4.0, 9.0, 0.8, 5.0, 6.0 ]
    print(list[1::])
    DirectInsertSort(list)
    print(list[1::])

if __name__ == '__main__':
    print(__name__)
    main()
