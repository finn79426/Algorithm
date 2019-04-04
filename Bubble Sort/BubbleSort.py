import random

def random_list(ran, elements):
    return random.sample(range(ran), elements)

def bubble_sort(list):
    # from small to large
    flag = True
    while flag == True:
        for i in range(0, len(list)-1):         # n-1 Round
            flag = False
            for j in range(0, len(list)-i-1):   # Compare range per round
                if list[j] > list[j+1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                    flag = True

            print("Round ", i, ":", list)

    return list


if __name__ == '__main__':
    data = random_list(100, 10)
    print("\nUnsorted data: \n{}\n".format(data))
    sorted_data = bubble_sort(data)
    print("\nResult: \n{}".format(sorted_data))