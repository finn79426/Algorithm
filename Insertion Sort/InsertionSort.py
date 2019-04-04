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

        print("Round ", i, ":", list)

    return list


if __name__ == '__main__':
    data = random_list(100, 10)
    sorted_data = insertion_sort(data)
    print("\nResult: \n", sorted_data)