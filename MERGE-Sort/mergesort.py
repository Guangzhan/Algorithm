# *-* coding: utf-8 *-*


def merge(lists, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = [0] * n1
    right = [0] * n2

    for i in range(0, n1):
        left[i] = lists[p + i]
    for j in range(0, n2):
        right[j] = lists[q + j + 1]

    print left, right

    k = p
    i = 0
    j = 0
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            lists[k] = left[i]
            i += 1
        else:
            lists[k] = right[j]
            j += 1
        k += 1

    while i != n1:
        lists[k] = left[i]
        i += 1
        k += 1
    while j != n2:
        lists[k] = right[j]
        j += 1
        k += 1

    '''
    if i < n1:
        for i in range(i, n1):
            lists[k] = left[i]
            i += 1
            k += 1
    if j < n2:
        for j in range(j, n2):
            lists[k] = right[j]
            j += 1
            k += 1
    '''


def merge_sort(lists, p, r):
    if p < r:
        q = (p + r) / 2
        merge_sort(lists, p, q)
        merge_sort(lists, q + 1, r)
        merge(lists, p, q, r)


if __name__ == '__main__':
    list1 = [1, 9, 2, 5, 7, 4, 6, 8]
    merge_sort(list1, 0, len(list1) - 1)
    print list1
