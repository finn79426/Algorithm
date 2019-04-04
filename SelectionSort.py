import random

def random_list(ran, elements):
    return random.sample(range(ran), elements)

def selection_sort(list):
    # from small to large
    for i in range(0, len(list)-1):
        min = 1
        for j in range(i+1, len(list)):
            if(list[min] > list[j]):
                min = j
        if(min != i):
            list[min], list[i] = list[i], list[min]
        print("Round ", i+1, ":", list)

    return list

if __name__ == '__main__':
    data = random_list(100, 10)
    sorted_data = selection_sort(data)
    print("\nResult: \n", sorted_data)