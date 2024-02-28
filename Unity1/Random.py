def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    modified_string = ''.join(char for char in input_string if char not in vowels)
    return modified_string

input_string = "Hello, World!"
print(remove_vowels(input_string))