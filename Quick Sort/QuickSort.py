import random

def random_list(ran, elements):
    return random.sample(range(ran), elements)

def quick_sort(list):
    # from small to large
    if len(list) <= 1:
        return list
    less = []
    greater = []
    pivot = list.pop()  # Extract the tail
    for i in list:
        if i < pivot:
            less.append(i)
        else:
            greater.append(i)
    list.append(pivot)

    return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == '__main__':
    data = random_list(100, 10)
    print("\nUnsorted data: \n{}\n".format(data))
    sorted_data = quick_sort(data)
    print("\nResult: \n{}".format(sorted_data))