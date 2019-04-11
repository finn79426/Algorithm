import random

def random_list(ran, elements):
    return random.sample(range(ran), elements)

def merge_sort(list):
    print("Splitting: {}".format(list))
    if len(list) >1:
        mid = len(list) // 2
        L = list[:mid]
        R = list[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i+=1
            else:
                list[k] = R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            list[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            list[k] = R[j]
            j+=1
            k+=1
    print("\033[92mMerging: {}\033[0m".format(list))

if __name__ == '__main__':
    data = random_list(100, 10)
    print("\nUnsorted data: \n{}\n".format(data))
    merge_sort(data)
    print("\nResult: \n{}".format(data))