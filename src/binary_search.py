# Binary Search--> ask yourself a question that greatly reduces the amount of search space
# Must have order in the collection of items that are searched through
# O(log n) time complexity --> halving

def iterative_binary_search(array, target):
    # 1. Declare min = 0 and max = length of array - 1
    # this initializes the sliding search space
    min = 0
    max = len(array) - 1
    while min < max:
        # 2. Figure out the guess value by getting the middle integer between min and max
        guess = (max + min) // 2
        # 3. if array[guess] equals the target, we found the element, return the index
        if array[guess] == target:
            return guess
        # 4. if the guess was too low, reset min to be one more than the guess
        elif array[guess] < target:
            min = guess + 1
        # 5. if the guess was too high, reset max to be one less than the guess
        else:
            max = guess - 1
    # no match found
    return -1

print(iterative_binary_search([-8, -4, -2, -1, 9, 17, 36, 44], 36)) #6

def recursive_binary_search(array, target):
    # base case
    if len(array) == 0:
        return False
    # get the middle of the array for our guess
    guess = len(array) // 2

    # compare the value of the array at guess index to the target
    if array[guess] == target:
        # return the target index
        return True
    
    # intitialize variables to store recursive return values
    is_found_in_left = False
    is_found_in_right = False

    # if the target is smalled than array[guess]
    if target < array[guess]:
        # repeat recursive search function over the array from start to guess
        is_found_in_left = recursive_binary_search(array[0:guess], target)

    # if the target is larger than array[guess]
    if target > array[guess]:
        # repeat recursive search funtion over the array from guess+1 to the end
        is_found_in_right = recursive_binary_search(array[guess + 1:], target)
    
    # return whichever variable resolves true
    return is_found_in_left or is_found_in_right


print(recursive_binary_search([-8, -4, -2, -1, 9, 17, 36, 44], 36)) #True
print(recursive_binary_search([-8, -4, -2, -1, 9, 17, 36, 44], 23)) #False
