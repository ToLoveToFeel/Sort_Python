
def Merge(list2, list, left, middle, right):
    #list为合并后的目标数组，将有序的序列 list2[s..m] 和 list2[m+1..t]归并为有序的序列 list[s..t]
    i = left
    j = middle + 1
    k = left
    while (i <= middle) and (j <= right):
        if list2[i] <= list2[j]:
            list[k] = list2[i]
            i = i + 1
        else:
            list[k] = list2[j]
            j = j + 1
        k = k + 1
    if i <= middle:
        while i <= middle:
            list[k] = list2[i]
            k = k + 1
            i = i + 1
    if j <= right:
        while j <= right:
            list[k] = list2[j]
            k = k + 1
            j = j + 1

def Msort(list2, list, start, end):
    #将 list2[s..t] 通过 list3[] 归并排序为 list[s..t]
    list3 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    if start == end:
        list[start] = list2[start]
    else:
        middle = int((start + end) / 2)
        Msort(list2, list3, start, middle)
        Msort(list2, list3, middle+1, end)
        Merge(list3, list, start, middle, end)

def MergeSort(list):     #默认第0项为哨兵项
    size = len(list) - 1
    Msort(list, list, 1, size)

def main():
    list = [ 0.0, 6.0, 2.2, 7.2, 4.0, 9.0, 0.8, 5.0, 6.0, 2.0 ]
    print(list[1::])
    MergeSort(list)
    print(list[1::])

if __name__ == '__main__':
    print(__name__)
    main()
