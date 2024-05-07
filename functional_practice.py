# Write a function flatten_dict() to flatten a nested dictionary by joining the keys with . character.
# >>> flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}) {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}
# Hint: You can assume that all dictionary keys will be of type string, and that nested dictionaries will only be nested one layer deep (a dictionary of dictionaries will not have another dictionary nested inside it).
def flatten_dict(nested):
    flat_dict = {}
    for key, value in nested.items():
        if isinstance(value, dict):
            for subkey, subvalue in flatten_dict(value).items():
                flat_dict[f"{key}.{subkey}"] = subvalue
        else:
            flat_dict[key] = value
    return flat_dict
nested_dictionary = {'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}
print(flatten_dict(nested_dictionary))

# Write a function unflatten_dict() to do reverse of flatten_dict.
# >>> unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}) {'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}
# Hint: You can assume that the keys for the dictionary will all be of type string, and that you never need to create more than one layer of nested dictionary. It may be helpful to create an empty dictionary as the value for the outer key ('b' in this example), then fill it in iteratively as you find keys that belong to that dictionary.
def unflatten_dict(flat_dict):
    unflattened_dict = {}
    for key, value in flat_dict.items():
        keys = key.split('.')
        new_dict = unflattened_dict
        for i in range(len(keys) - 1):
            if keys[i] not in new_dict:
                new_dict[keys[i]] = {}
            new_dict = new_dict[keys[i]]
        new_dict[keys[-1]] = value
    return unflattened_dict

flat_dict = {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}
print(unflatten_dict(flat_dict))

# Write a function treemap() to map a function over nested list.
# >>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]]) [1, 4, [9, 16, [25]]]
# Hint: Using recursion may make this function easier to code. Don't forget to check the type of the element you are iterating over.
def treemap(func, nested_list):
    if isinstance(nested_list, list):
        return [treemap(func, item) for item in nested_list]
    else:
        return func(nested_list)
    
nest_list = [1, 2,[3, 4, [5]]]
print(treemap(lambda x: x*x, nest_list))