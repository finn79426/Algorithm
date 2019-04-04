import random

def random_list(ran, elements):
    return random.sample(range(ran), elements)

def insertion_sort(list):
    # from small to large
    for i in range(1, len(list)):
        tmp = list[i]
        j = i-1
        while j >= 0 and tmp < list[j]:
            list[j+1] = list[j] # right shift
            j = j-1
        list[j+1] = tmp
    return list

def binary_search(list, keyword):
    head = 0
    tail = len(list)
    while head < tail:
        mid = head + (tail - head) // 2     # Integer division
        midVal = list[mid]
        if keyword == midVal: return mid
        elif keyword > midVal:
            if head == mid: break
            head = mid
        elif keyword < midVal:
            tail = mid
    return False

if __name__ == '__main__':
    data = random_list(10, 10)
    print("\nUnsorted data: \n{}\n".format(data))
    sorted_data = insertion_sort(data)
    print("\nSorted data: \n{}\n".format(sorted_data))
    keyword = random.randint(0, 9)
    print("Search: {}".format(keyword))

    result = binary_search(data, keyword)

    if result is False: print("Not Found!")
    else: print("Found {} in array, index : {}".format(keyword, result))