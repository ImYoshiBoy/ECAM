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

print(rough_sort([1, 4, 2, 5, 6]))