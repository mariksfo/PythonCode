def highlight_word(sentence, word):
    uppercase = word.upper()
    sentence = sentence.replace(word, uppercase)
    return sentence

print(highlight_word("Hi there, How are you", "you"))