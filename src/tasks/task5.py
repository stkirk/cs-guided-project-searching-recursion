# given a positive integer, n:
# F0 = 0, F1 = 1. For each i > 1: Fi = Fi - 1 + Fi - 2
# n is >= 1 and less than 2*10^9

# n == fib1 + fib2
# n - fib1 = fib2

def sum_of_fibs(n):
    # STEP 1: find fibonacci numbers with values up to n and put into a list
    # edge case: if n is 1, return true
    # if n == 1 or n == 2 or n == 3:
    #     return True
    # initialize list of fib numbers to append to
    fibs = [0, 1]
    # break while loop if fibs last index is greater than or equal to n
    # init count to calculate fib number
    count = 2
    while n:
        next_fib = fibs[count - 1] + fibs[count - 2]
        if next_fib > n:
            break
        fibs.append(next_fib)
        count += 1

    # STEP 2: search through fibs to see if two indicies add up to target n

    # init a dict with the complement of each integer and n as keys and their index as values
    complements = {(n - fib): True for fib in fibs}

    # loop through fibs
    for fib in fibs:
        # if a complement exists in list of fibonacci nums, we have a good sum, return True
        if fib in complements:
            return True
    # loop finished without finding a complement, return false
    return False

print(sum_of_fibs(1)) #-->True
print(sum_of_fibs(11)) #-->True
print(sum_of_fibs(13)) #-->True
print(sum_of_fibs(60)) #-->True
print(sum_of_fibs(66)) #-->False
print(sum_of_fibs(811)) #-->False
