
class SLCell:
    keys = ""
    next = 0

class SLList:
    r = []
    keynum = 0
    recnum = 0

MAX_NUM_OF_NUM = 8	#关键字项数的最大值,此时整数最多8位
NUM_OF_NUM = 3	#实际关键字个数
RADIX = 10	#关键字的基数，此时是十进制整数的基数
MAX_SPACE = 100

def ord(keys, i):
    if i > len(keys):
        return 0
    else:
        return int(keys[i])

def Distribute(R, t, f, r, head):
    for i in range(0, RADIX):
        f[i] = -1
        r[i] = -1
    p = head
    while -1 != p:
        i = ord(R[p].keys, NUM_OF_NUM - t - 1)
        if -1 == f[i]:
            f[i] = p
        else:
            R[r[i]].next = p
        r[i] = p
        p = R[p].next

def Collect(R, f, r, head):
    i = 0
    while (i < RADIX) and (-1 == f[i]):
        i = i + 1
    head = f[i]
    t = r[i]
    while i < RADIX:
        i = i + 1
        while (i < RADIX - 1) and (-1 == f[i]):
            i = i + 1
        if (i < RADIX) and (-1 != f[i]):
            R[t].next = f[i]
            t = r[i]
    R[t].next = -1
    return head


def RadixSort(list):
    global head
    head = 0
    for i in range(list.recnum):
        list.r[i].next = i + 1
    list.r[list.recnum - 1].next = -1
    f = [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ]
    r = [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ]
    for i in range(list.keynum):
        Distribute(list.r, i, f, r, head)
        head = Collect(list.r, f, r, head)

def RadixPrint(list):
    p = head
    for i in range(list.recnum):
        print(list.r[p].keys)
        p = list.r[p].next

def main():
    y = [ 369, 367, 167, 239, 237, 138, 230, 139 ]
    list = SLList()
    list.recnum = len(y)
    list.keynum = NUM_OF_NUM

    for i in range(list.recnum):
        slcell = SLCell()
        slcell.keys = str(y[i])
        list.r.append(slcell)
    print("Before Sort : ")
    print(y)
    RadixSort(list)
    print("After Sort  : ")
    RadixPrint(list)
    
if __name__ == '__main__':
    print(__name__)
    main()









