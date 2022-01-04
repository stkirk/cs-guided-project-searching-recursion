# given a sorted array with a pivot at an unknown index and a target value
# return the target's index in the array
# if the target is not present, return -1
# no duplicates in the array
# solution must be O(log n) runtime

def ex(nums, target):
    # STEP 1: perform a binary search to find the pivot index:
    pivot_index = 0
    # init lower and upper search boundary
    lower = 0
    upper = len(nums) - 1
    # while loop through nums as long as lower is less than upper
    while lower <= upper:
        # init pivot_guess to middle index value using floor division
        pivot_guess_index = (lower + upper) // 2
        pivot_guess = nums[pivot_guess_index]
        # if pivot_guess is the target, return pivot_guess index
        if pivot_guess == target:
            return pivot_guess_index
        # elif pivot_guess is less than preceding index
        elif pivot_guess < nums[pivot_guess_index - 1]:
            # set pivot index to pivot_guess's index
            pivot_index = pivot_guess_index
            break
        # elif pivot_guess is greater than upper
        elif pivot_guess > nums[upper]:
            # ser lower to pivot_guess index + 1
            lower = pivot_guess_index + 1
        # else pivot_guess is less than upper
        else:
            # set upper to pivot_guess_index - 1
            upper = pivot_guess_index - 1


    # loop should break when pivot_index is found
    # STEP 2: use pivot index to complete a binary search for the target:
    # reset upper and lower bounds
    lower = 0
    upper = len(nums) - 1
    if target > nums[upper]:
        upper = pivot_index - 1
    else:
        lower = pivot_index + 1
    
    # while loop
    while lower <= upper:
        # find middle idx for guess
        guess_idx = (lower + upper) // 2
        # if nums[guess_idx] is the target
        if target == nums[guess_idx]:
            # return guess_idx
            return guess_idx
        # elif the target is greater than nums at guess_idx
        elif target > nums[guess_idx]:
            # set lower to guess_idx + 1
            lower = guess_idx + 1
        # else the target is less than nums at guess_idx
        else:
            # set upper to guess_idx - 1
            upper = guess_idx - 1
    
    # loop finishes without returning, target not present in nums
    return -1


print(ex([4,5,6,7,0,1,2], 0)) #--> 4

print(ex([4,5,6,7,9,48,0,1,2], 48)) #--> 5

print(ex([4,5,6,7,0,1,2], 3)) #--> -1