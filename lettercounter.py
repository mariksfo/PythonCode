ignore = [" ", "+", "=", "!", ".", "?"]

def count_letters(sentence):
    count = {}
    for letter in sentence:
        if letter in ignore:
            sentence = sentence.replace(letter, "")
    
    for letter in sentence:
        if letter.lower() in count:
            count[letter.lower()] += 1
        else:
            count [letter.lower()] = 1
    
    print(count)

    return count

x = count_letters("Hi Man! Wow you have designed a nice website. Cool")
