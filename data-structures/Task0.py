#!/usr/bin/python3

#Task0

# Python function that prints all integers of a list, one per line
# Without importing modules or casting integers into strings


# The user is expected to pass in only a list of integers

def print_all_int(list):
    for int in list:
        print(int)
print_all_int([1, 2, 3, 4, 5])


#Task1

#Python function that retrieves an element from a list.
#If idx is negative or out of range (greater than the number of elements in my_list), the function
#returns None.
#Without importing modules or using try/except.

def el_at_list(list,idx):
    my_list_len = len(list)
    if idx >= my_list_len or idx < 0:
        return None
    else:
        return list[idx]

print(el_at_list([-1, -2, -3],3))

#Task6
#Python function that returns a set of common elements in two sets.
#Without importing modules.

def common_elements_in_two_sets(set_a, set_b):
    return set_a.intersection(set_b)

print(common_elements_in_two_sets({1, 10, 11}, {1, 11, 15}))

#Task 7
#Python function that returns a set of all elements present in only one set.
#Without importing modules.

def unique_elements_in_two_sets(set_a, set_b):
    return set_a.symmetric_difference(set_b)
print(unique_elements_in_two_sets({1, 10, 11}, {1, 11, 15}))



#Task8
#Python function that returns the number of keys in a dictionary.
#Without importing modules.

presidents_of_ke = {
    "First President": "Mzee Jomo Kenyatta",
    "Second President": "Daniel Arap Moi",
    "Third President": "Mwai Kibaki",
    "Fourth President": "Uhuru Kenyatta",
    "Fifth President": "William Ruto",
}

def no_of_keys_in_dict(dict):
    return len(dict.keys())
print("no of keys in presidents_of_ke: ", no_of_keys_in_dict(presidents_of_ke))

#Task 10

#Python function that replaces or adds key/value pairs in a dictionary.
#The parameter key is always a string.
#The parameter value is any type.
#If a key exists in the dictionary, the value is replaced.
#If a key does not exist in the dictionary, it is created.
#Without importing modules.

colors_of_rainbow = {
    "Color 1": "Red",
    "Color 2": "Orange",
    "Color 3": "Yellow",
    "Color 4": "Green"
}
def update_values_in_dict(dict, key, value):
    dict[key] = value
    return dict

print(update_values_in_dict(colors_of_rainbow,"Color 5", "Violet"))

#Task 11

#Python function that deletes a key in a dictionary.
#The paramter key is always a string.
#If the key does not exist, the dictionary does not change.
#Without importing modules.

colors_of_rainbow = {
    "Color 1": "Red",
    "Color 2": "Orange",
    "Color 3": "Yellow",
    "Color 4": "Green"
}

def del_key_in_dict(dict, key):
    if key in dict:
        del dict[key]
    return dict
print(del_key_in_dict(colors_of_rainbow, "Color 4"))
