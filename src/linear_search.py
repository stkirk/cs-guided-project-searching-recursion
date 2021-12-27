# Is an item in our array? return true or false

def linear_search(array, target):
    # traditionally we would loop through the array, one item at a time and in order, until we found target
    for item in array:
        if item == target:
            return True
    return False
# O(n) time complexity

our_array = list(range(20)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print(our_array)
print(linear_search(our_array, 10))
print(linear_search(our_array, 100))