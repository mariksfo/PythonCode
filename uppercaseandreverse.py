def uppercase_and_reverse(sentence):
    uppercase = sentence.upper()
    uppercase_list = list(uppercase)
    uppercase_list.reverse()
    result = "".join(uppercase_list)
    return result


print(uppercase_and_reverse("Hi there, i would be uppercase and reversed"))