def unique_elements(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


lst = [1,2,2,2,3,4,5,5,6]
print(unique_elements(lst))