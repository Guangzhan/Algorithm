# *-* coding: utf-8 *-*
__author__ = '3403'

#调整堆
def max_heap(heap, i):
    left = i << 1
    right = left | 1
    if left < heap_size and heap[left] > heap[i]:
        largest = left
    else:
        largest = i
    if right < heap_size and heap[right] > heap[largest]:
        largest = right
    assert isinstance(i, int)
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heap(heap, largest)

#建堆的过程
def build_max_heap(heap):
    for i in range(1, heap_size / 2 + 1)[::-1]:
        max_heap(heap, i)

#堆排序
def heap_sort(heap):
    global heap_size
    heap_size = len(heap)
    build_max_heap(heap)
    for i in range(2, heap_size)[::-1]:
        heap[1], heap[i] = heap[i], heap[1]
        heap_size -= 1
        max_heap(heap, 1)


if __name__ == '__main__':
    lists = [' ', 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

    heap_sort(lists)
    print lists[1:]



