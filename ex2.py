# From the given array that has any number of sub-lists, dict, nested dicts find out all the positive integers
# and store them in an array. In case of dicts take both keys & values positive integers.
# From the final array create an occurrence dictionary to figure out the occurrence of each number.
# Don't use any built-ins. Please remember the input array can have any levels of nested lists, sub-lists
# and nested dictionaries

# Function to find the frequency of each element in a list and store them in a dictionary
def find_freq(arr):
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


# Function to handle dictionary element encountered in the list
def handle_dict(args):
    for arg in args:
        if isinstance(arg, int) and arg > 0:
            yield arg
        if isinstance(args[arg], int) and args[arg] > 0:
            yield args[arg]
        elif isinstance(args[arg], list):
            for item in list(handle_list(args[arg])):
                yield item
        elif isinstance(args[arg], dict):
            for item in list(handle_dict(args[arg])):
                yield item


# Function to handle list element encountered in the list
def handle_list(args):
    for arg in args:
        if isinstance(arg, int) and arg > 0:
            yield arg
        elif isinstance(arg, list):
            for item in list(handle_list(arg)):
                yield item
        elif isinstance(arg, dict):
            for item in list(handle_dict(arg)):
                yield item


res = list(handle_list([1, 2, 3, 4, 5, [True, False, -110.100, -200, 500, [1, 2, 3, 4, 5]],
                        {0: 1, 1: 2, 3: 4, 5: [10, True, -1100, 200, 300]}
                        ]))
freq = find_freq(res)
print(freq)
