# given two string of equal length, check if they are blanagrams of each other
# blanagrams - words are anagrams, EXCEPT, one letter is substituted for another
# if anagrams --> false
# return True if blanagrams, otherwise return false

def is_blanagram(word1, word2):
    # map word1 to a dictionary with letters as keys and count as value
    word1_dict = {}
    for letter in word1:
        if letter in word1_dict:
            word1_dict[letter] += 1
        else:
            word1_dict[letter] = 1

    # initialize a counter to keep track of letters in word2 that arent in word1
    diff_letter_count = 0

    #loop through word2
    for letter in word2:
        # if the letter isnt in word1_dict
        if letter not in word1_dict:
            # increment diff_letter_count
            diff_letter_count += 1
        # elif the letter is in word1_dict with a value of 0
        elif word1_dict[letter] == 0:
            # increment the diff_letter_count
            diff_letter_count += 1
        # else the letter is in word1_dict with a value > 0
        else:
            # decrement the value of that key in word1_dict
            word1_dict[letter] -= 1
    # if diff_letter count is 1, we have a blanagram, if not we don't
    if diff_letter_count == 1:
        return True
    else:
        return False

print(is_blanagram("tangram", "anagram")) #--> true
print(is_blanagram("tangram", "pangram")) #--> true
print(is_blanagram("aba", "bab")) #--> true
print(is_blanagram("silent", "listen")) #--> false