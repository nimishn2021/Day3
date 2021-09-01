# Using List comprehension flatten a List. Your Function will take 2 Lists namely ListA and List B.
# You need to pick elements from ListA which are divisible by any element in ListB.
# Note ListB must contain atleast 2 elements else dont process.
# Return the final list.

# Function to check if how many numbers are divisible by x
def find_divisible(num, arr):
    count = 0
    for item in arr:
        if num % item == 0:
            count += 1
        if count >= 2:
            return True
    return False


# Function to find out the final list of divisibility
def find_result(arr1, arr2):
    return [num for num in arr1 if find_divisible(num, arr2)]


print(find_result([10, 30, 35, 40, 45, 28, 39, 50, 61, 78], [2, 5, 10, 20, 50]))
