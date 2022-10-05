from msilib.schema import EventMapping


even_and_odd = [1,2,3,4,5,6,7,8,9,24,123,534,64,624,1221,13,33,15]



even = []
odd = []

count = 0

for number in even_and_odd:
    if number % 2 == 0:
        print("{} is an even number".format(number))
        even.append(str(number))
        count += 1
    else:
        print("{} is an odd number".format(number))
        odd.append(str(number))

even = ", ".join(even)
odd = ", ".join(odd)

print("There are {} even numbers in the given list".format(count))
print("Here are all the even numbers in the list {}".format(even))
print("Here are all the odd numbers in the list {}".format(odd))