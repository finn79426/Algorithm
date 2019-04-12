import random

def random_list(ran, elements):
    return random.sample(range(ran), elements)

def heap_sort(list):
    # from small to large

    def heapify(list, n, i):
        largest = i     # Initialize largest as root
        L = 2 * i + 1   # Left
        R = 2 * i + 2   # Right

        # 檢查右邊子樹的child元素是否存在，且大於root
        if L < n and list[i] < list[L]:
            largest = L

        # 檢查右邊子樹的child元素是否存在，且大於root
        if R < n and list[largest] < list[R]:
            largest = R

        # Change root, if needed
        if largest != i:
            list[i],list[largest] = list[largest],list[i]  # swap
            # Heapify the root.
            heapify(list, n, largest)

    n = len(list)

    for i in range(n, -1, -1):
        heapify(list, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        list[i], list[0] = list[0], list[i]   # swap
        heapify(list, i, 0)

if __name__ == '__main__':
    data = random_list(100, 10)
    print("\nUnsorted data: \n{}\n".format(data))
    heap_sort(data)
    print("\nResult: \n{}".format(data))