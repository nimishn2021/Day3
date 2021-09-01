# Using Dict Comprehension find the Occurences of Numbers. Your function will take an Integer X followed
# by any number of Arrays. You need to parse each array and find out elements in the Array that is divisible by X and
# return the count of numbers that's divisible by X with its position.

# Function to find the count of the numbers in a list divisible by x
def find_count(x, arr):
    count = 0
    for num in arr:
        if num % x == 0:
            count += 1
    return count


# Function to find out the dictionary with the list index as the key and frequency as the value
def find_divisible_freq(x, *args):
    temp = list(enumerate(args))
    return {arg[0]: find_count(x, arg[1]) for arg in temp}


print(find_divisible_freq(5, [1, 20, 35, 45, 90], [100, 20, 30, 45, 60, 75, 90], [2, 3, 30, 19, 90, 25, 80],
                          [5, 6, 9, 10, 15, 25, 30]))
