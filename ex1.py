# Write python function to find the powers of numbers. Each item in the Array must take the next element in the
# array as it pow and return.
# If any number is left-behind without next number, then it shall take the min number in the array as its pow.
# The max pow that can be taken is 5. If there is any item in the Array whose next number in the array is > 5,
# then pow will not apply and its value remains the same.

# Function to find the minimum number in the list
def find_min(arr):
    mini = arr[0]
    for num in arr:
        if num < mini:
            mini = num
    return mini


# Function to find the power of a number x raised to n
def power(arr, x, n=-1):
    if n == -1:
        n = find_min(arr)
    if n <= 5:
        return x ** n
    return x


# Function to find the length of the list
def find_length(args):
    length = 0
    for _ in args:
        length += 1
    return length


# Function to find the power series
def find_power_series(*args):
    n = find_length(args)
    res = [power(args, args[i], args[i + 1]) if i + 1 != n else power(args, args[i]) for i in
           range(0, find_length(args), 2)]
    print(res)


find_power_series(10, 3, 50, 1, 20, 3, 8, 2)
find_power_series(10, 3, 50, 2, 20, 3, 8, 2, 100)
find_power_series(10, 6, 50, 2, 20, 3, 8, 2, 100)
