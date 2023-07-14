#Write a python script to enter any string and count vowel.

def count_vowels(string):
    vowel_count = 0
    vowels = "aeiouAEIOU"  # List of vowels

    for char in string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

user_input = input("Enter a string: ")
result = count_vowels(user_input)
print("Number of vowels:", result)
