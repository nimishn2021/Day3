# Program to flatten a list using recursions. Input list can contain any levels of sub-lists

# Function to flatten out nested lists into a simple list using recursion
def flatten_list(arg):
    for item in arg:
        if isinstance(item, list):
            for num in list(flatten_list(item)):
                yield num
        else:
            yield item


print(list(flatten_list([1, 2, 3, 4, 5, [10, 20, 30, 4, 50, 60, 100], 90, 200, [300, 10]])))
