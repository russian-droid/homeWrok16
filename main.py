'''
CodeWars kata from codewars.com

Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
'''

def duplicate_count(text):
    # initializing a list to append all the duplicate characters
    duplicates = []
    for char in text:
    # checking whether the character have a duplicate or not
    # str.count(char) returns the frequency of a char in the str
        if text.count(char) > 1:
            # appending to the list if it's already not present
            if char not in duplicates:
                duplicates.append(char)
    #how many elements in the list
    duplicate_count = (len(duplicates))
    return duplicate_count

#-----someone else's way
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
