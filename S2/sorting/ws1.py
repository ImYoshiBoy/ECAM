def minimum(any_list:list)->list:
    mini = any_list[0]
    for i in range(1, len(any_list)):
        if mini > any_list[i]:
            mini = any_list[i]
    return mini

def rough_sort(int_list:list) -> list:
    sorted_list = []
    for i in range(len(int_list)):
        mini = minimum(int_list)
        sorted_list.append(mini)
        int_list.remove(mini)
    return sorted_list

def bubblesort(any_list:list)->list:
    n = len(any_list)
    for j in range(n - 1):
        for i in range(n - 1 - j):
            if any_list[i] > any_list[i + 1]:
                any_list[i],any_list[i + 1] = any_list[i + 1],any_list[i]
            print(any_list)
    return any_list

#THIS IS NOW THE WORKSHEET