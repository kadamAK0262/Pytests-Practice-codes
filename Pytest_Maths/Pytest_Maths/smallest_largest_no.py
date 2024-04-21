def find_smallest_largest(my_list):
    if not my_list:
        return None, None  # Return None for empty list

    smallest = largest = my_list[0]

    for num in my_list:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    return smallest, largest
