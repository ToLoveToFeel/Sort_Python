
def ShellSort(list, d):     #默认第0项为哨兵项
    size = len(list)
    for i in range(d+1, size):
        if list[i] < list[i-d]:
            list[0] = list[i]
            list[i] = list[i-d]
            j = i - 2 * d
            while (j > 0) and (list[0] < list[j]):
                list[j+d] = list[j]
                j = j - d
            list[j+d] = list[0]


def main():
    list = [ 0.0, 6.0, 2.2, 7.2, 4.0, 9.0, 0.8, 5.0, 6.0 ]
    print(list[1::])
    a = [5, 3, 1]
    for i in range(len(a)):
        ShellSort(list, a[i])
    print(list[1::])

if __name__ == '__main__':
    print(__name__)
    main()
