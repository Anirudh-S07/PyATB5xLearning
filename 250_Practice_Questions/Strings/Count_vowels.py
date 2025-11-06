# count the number of vowels in a string

def count_vowels(string):
    vowel_set = {"a", "e", "i", "o", "u"}
    count = 0
    lowered_string = string.lower()
    for char in lowered_string:
        if char in vowel_set:
            count += 1
    return count


print(count_vowels("hi, aeiou"))

