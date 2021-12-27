# given a list of integers, nums, and an integer target:
# nums has been rotated as to have a pivot point where the ascending order starts over, ie [7, 8, 9, 1, 2] --> first 3 items are in ascending and the last 2 are also in ascending, the 3rd index (1) is the pivot
# search through the list and return the target index
# if the target isn't there return -1
# solution must have better than O(n) time complexity
# length of nums is between 1 and 100
# integers in nums are between 1 and 100
# all values of nums are unique

def pivot_search(nums, target):
    # init min and max search window
    min = 0
    max = len(nums) - 1
    # init pivot_idx
    pivot_idx = -1
    # while loop min <= max
    while min <= max:
        # look for the pivot index
        pivot_guess = (min + max) // 2
        # if pivot_guess is the target, return the pivot index
        if nums[pivot_guess] == target:
            print("target == pivot")
            return pivot_guess
        # elseif nums[pivot_guess] is less than nums[pivot_guess -1]
        if nums[pivot_guess] < nums[pivot_guess - 1]:
            # set pivot_idx = pivot_guess
            pivot_idx = pivot_guess
            # break the loop
            break
        # elseif nums[pivot_guess] > nums[max], pivot is to the right
        elif nums[pivot_guess] > nums[max]:
            # move min to pivot_guess + 1
            min = pivot_guess + 1
        # else pivot is to the left
        else:
            # move max to pivot_guess - 1
            max = pivot_guess -1

    # loop finished, we have a pivot point, reset min and max for new binary search within the correct side of the pivot
    # if the target is greater than the last integer in nums, the target must be between nums[0] and nums[pivot_idx - 1]
    if target > nums[len(nums) - 1]:
        # set min to 0 and max to pivot_idx -1
        min = 0
        max = pivot_idx - 1
    # else the target is between pivot_idx and the last integer in nums
    else:
        # set min to pivot_idx + 1 and max to len(nums) - 1
        min = pivot_idx + 1
        max = len(nums) - 1
    # while loop for binary search
    while min <= max:
        guess = (min + max) // 2
        if target == nums[guess]:
            return guess
        elif target > nums[guess]:
            min = guess + 1
        else:
            max = guess - 1
    # target not found
    return -1
    

print(pivot_search([6,7,1,2,3,4,5], 1)) #--> 2 
print(pivot_search([6,7,1,2,3,4,5], 3)) #--> 4
print(pivot_search([6,7,8, 9, 10, 11, 14, 19, 987, 1024, 5487 ,1,2,3,4,5], 3)) #--> 4
print(pivot_search([1], 2)) #--> 1