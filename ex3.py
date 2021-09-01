# Function to find out ways to form a string from another string. Function will take 2 strings as inputs.
# You must find out all possible ways by which you can form string A from String B.
# You must validate to ensure that the strings are Alpha-numeric only, it must contain
# only strings and numbers.
# No other types are allowed. The length of String B must be >er than String A.
# Char once used from String B must not be used again.
# Return the final Output in dictionary format with indexes and values.
# Indexes represent the index value in String B that has occurrence of a char from String A

# Function to find the minimum of the list
def find_min(arr):
    mini = arr[0]
    for item in arr:
        if item < mini:
            mini = item
    return mini


# Function to find the length of the list
def find_length(arr):
    length = 0
    for _ in arr:
        length += 1
    return length


# Function to find the occurence index of a particular character in the string
def find_index(val, string):
    return [i for i in range(find_length(string)) if string[i] == val]


# Function to make the occurence character dictionary
def make_substring(stringA, stringB, min_length=None):
    res = [find_index(char, stringB) for char in stringA]
    length = [find_length(item) for item in res]
    min_length = find_min(length)
    temp = [item[:min_length] for item in res]
    temp_len = find_length(temp)
    dicta = [{temp[j][i]: stringA[j] for j in range(temp_len)} for i in range(min_length)]
    print(dicta)


make_substring("abc", "agcb xyzbc amnopq copnotab coscabbb")
