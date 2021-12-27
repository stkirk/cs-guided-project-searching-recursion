# Recursion: a function that calls itself, kind of a loop

def f(n):
    # base case: work towards n being 0
    # will always return a value
    if n == 0:
        return
    # first print of hello world
    print("hello word")

    #recursive case: get us closer to the base case
    # repeats printing hello world by calling this function and passing in every decrementing values of n until n==0 and the conditional statement above is triggerd to return out
    f(n-1)
    return

f(3)
'''
***Call Stack***
### what happends when we call this function, f, and pass in 3 for n?
1) f is added to the call stack with n==3 and runs, n!=0 so it doesnt return
2) print("hello world") runs to completion
3) f is called again and added to top of stack with n==2, n!=0 so it doesn't return
4) print("hello world") runs to completion
5) f is called again and added to top of stack with n==1, n!=0 so it doesn't return
6) print("hello world") runs to completion
7) f is called again and added to top of stack with n==0, n==0 so it does return! and is popped off the stack
8) the f with n==1 is now on top and has no more lines to run, it returns and it pops off the stack
9) the f with n==2 is now on top and has no more lines to run, it returns and it pops off the stack
10) the f with n==3 is now on top and has no more lines to run, it returns and it pops off the stack
11) the orginal f with n==4 is now on top and has no more lines to run, it returns and it pops off the stack
'''




# Is an item in our array? return true or false
# same problem as in linear search

def search_in_first_spot(array, target):
    if len(array) == 0:
        return False
    if array[0] == target:
        return True
    return search_in_first_spot(array[1:], target)
'''
This is essentially whats happening in the recursive search function
Each time it is passed into search_in_first_spot the array gets smaller by 1 item
"I've already looked at the first index of the array, lets just lop that off and search through the rest"
search_in_first_spot(array[1:], 5)
search_in_first_spot(array[2:], 5)
search_in_first_spot(array[3:], 5)
search_in_first_spot(array[4:], 5)
'''

our_array = [1, 2, 3, 4, 5]
print(search_in_first_spot(our_array, 5))
