"""
I was bored one day and decided to look at last names in the phonebook for my
area.

I flipped open the phonebook to a random page near the middle and started
perusing. I wrote each last name that I was unfamiliar with down on paper in
increasing order. When I got to the end of the phonebook, I was having so much
fun I decided to start from the beginning and keep going until I reached the
page where I had started.

When I was finished, I had a list of interesting last names that were mostly
alphabetical. The problem was that my list starts somehere near the middle of
the alphabet, reaches the end, and then starts from the beginning of the
alphabet. In other words, my list of names is sorted, but it is "rotated."

Example:

surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]

Write a function that finds the index of the "rotation point". The "rotation
point" is where I started working from the beginning of the phone book. The
list I came up was absolutely huge, so make sure your solution is efficient.

*Note: you should be able to come up with a solution that has O(log n) time
complexity.*
"""
def find_rotation_point(surnames):
    # initialize min and max
    min = 0
    max = len(surnames) - 1

    while min <= max:
        # Look in the middle, compare surnames[i] and surnames[i-1] for alphabetization
        guess = (min + max) // 2

        # if surnames[i] < surnames[i-1] alphabetically, we've found the rotation point, return it
        if surnames[guess] < surnames[guess-1]: # beware negative index edge cases
            return surnames[guess]

        # otherwise, compare against the first and last names in the list to figure out where to search
        elif surnames[guess] >= surnames[0]:
            # if the guess comes after the surname or is the first surname, search the right half
            min = guess + 1

        # otherwise, go left
        else:
            # search the left half
            max = guess - 1

    # If we end up here with no rotation point
    return -1

print(find_rotation_point(['liu', 'mcdowell', 'nixon', 'sparks', 'zhang', 'ahmed', 'brandt', 'davenport', 'farley', 'glover', 'kennedy'])) # "ahmed"

