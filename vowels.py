word = "He is an honest man"

count = 0
found_vowels = []

for letter in word:
    if letter in ['a','e','i','o','u']:
        print("Vowel found")
        count += 1
        found_vowels.append(letter)
    else:
        continue

print("There are {} vowels in the given word".format(count))

found_vowels = ", ".join(found_vowels)

print("Following vowels were found in the given list :")
print("{} were found in the word".format(found_vowels))
-