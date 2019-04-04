import random

def random_list(ran, elements):
    return random.sample(range(ran), elements)

def linear_search(list, keyword):
    for i in range(len(list)):
        if list[i] == keyword: return i
    return False

if __name__ == '__main__':
    data = random_list(10, 10)
    print("\nUnsorted data: \n{}\n".format(data))
    keyword = random.randint(0, 9)
    print("Search: {}".format(keyword))
    result = linear_search(data, keyword)

    if result is False: print("Not Found!")
    else: print("Found {} in array, index : {}".format(keyword, result))