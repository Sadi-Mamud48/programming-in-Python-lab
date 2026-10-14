char = input("Enter a character: ")
if char in 'aeiou':
    print(f"{char} is a vowel.")
elif char in 'AEIOU':
    print(f"{char} is a vowel.")
else:
    print(f"{char} is not a vowel.")