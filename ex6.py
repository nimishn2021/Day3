# Write a Program to update dictionary Values using dict comprehensions.
# Your function will take 3 inputs, A dict, an Integer X and Integer Y.
# Find keys whose values are >er than Integer X and multiply them by Integer Y.

# Function to multiply the dictionary value with y
def multiply_by_y(dicti, x, y):
    return {key: dicti[key] * y for key in dicti if dicti[key] > x}


print(multiply_by_y({1: 3, 10: 20, 3: 4, 5: 60}, x=50, y=10))
