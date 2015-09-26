# *-* coding: utf-8 *-*
__author__ = 'Guangzhan'


# 插入排序
def insert_sort(lists):
    count = len(lists)
    for j in range(1, count):
        key = lists[j]
        i = j - 1
        while i >= 0 and key < lists[i]:
            lists[i + 1] = lists[i]
            i -= 1
        lists[i + 1] = key


if __name__ == '__main__':
    ls = [2, 5, 7, 0, 4, 3, 6]
    insert_sort(ls)
    for i in ls:
        print i,
