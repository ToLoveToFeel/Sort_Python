
def BubbleSort(list):     #默认第0项为哨兵项
    size = len(list) - 1
    change_flag = 1     #如果没发生交换说明已经排序完成，不需要继续运行，1代表发生变化
    i = size
    while (i > 1) and (1 == change_flag):
        change_flag = 0;
        for j in range(1, i):
            if(list[j] > list[j+1]):
                list[0] = list[j]
                list[j] = list[j+1]
                list[j+1] = list[0]
                change_flag = 1

def main():
    list = [ 0.0, 6.0, 2.2, 7.2, 4.0, 9.0, 0.8, 5.0, 6.0 ]
    print(list[1::])
    BubbleSort(list)
    print(list[1::])

if __name__ == '__main__':
    print(__name__)
    main()
