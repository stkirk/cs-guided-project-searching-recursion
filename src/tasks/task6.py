# given a sorted list of integers and a target integer:
# find the target integer in the list of nums
# return the target's index
# if the tager isn't present, return -1

def binary_search(nums, target):
    # intialize max and min range for our search window
    min = 0
    max = len(nums) - 1
    pivot = 5
    # loop as long as min < max
    while min <= max:
        # initialize middle of list of nums as guess_index
        guess_idx = (min + max) // 2
        # if target == nums[guess_index]
        if target == nums[guess_idx]:
            # return guess_index 
            return guess_idx
        # elseif target > nums[guess_index], target is to the right
        elif target > nums[guess_idx]:
            # move min to guess_index + 1
            min = guess_idx + 1
        # else target < nums[guess_index], target is to the left
        else:
            # move max to guess_index - 1
            max = guess_idx - 1
    # loop finished without returning, target is not in nums
    return -1

print(binary_search([-1,0,3,5,9,12], 9)) #--> 4 
print(binary_search([-1,0,3,5,9,12], 2)) #--> -1 
print(binary_search([46, 176, 487, 551, 980, 1020, 1098, 1354, 1381, 1414, 1578, 1579, 1596, 1634, 1810, 1882, 1924, 1999, 2021, 2074, 2083, 2269, 2579, 2616, 2626, 2645, 2871, 2874, 2889, 2987, 2999, 3106, 3126, 3191, 3217, 3304, 3342, 3516, 3557, 3579, 3617, 3655, 4022, 4049, 4059, 4386, 4510, 4600, 4792, 4799, 4937, 5257, 5466, 5489, 5574, 5623, 5915, 5929, 5976, 6011, 6047, 6136, 6173, 6175, 6331, 6333, 6368, 6631, 6673, 6847, 6960, 7034, 7042, 7167, 7186, 7352, 7604, 7879, 7945, 7991, 8225, 8226, 8330, 8370, 8394, 8500, 8528, 8563, 8786, 8831, 8837, 8861, 8976, 9236, 9251, 9388, 9436, 9532, 9708, 9891], 2871)) #--> 26
