# set_operations

def get_unique_elements(input_set):
    return set(input_set)

def set_intersection(set1, set2):
    return set1.intersection(set2)

def set_union(set1, set2):
    return set1.union(set2)


# dict_operations

def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

def get_dict_keys(dictionary):
    return list(dictionary.keys())
