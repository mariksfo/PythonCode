for i in range(1,10):
    print('Hello world')

for i in range(1,10,2):
    print(i)
    print("hi there as you can see i am the best",i)

    fruits = ['apples', 'bananas', 'peach']

for i in fruits:
    print(i)
    index = fruits.index(i)
    print("the index of {} is {}".format(i,index))

    


data = {
        'name':'alex',
        'age': 12,
        'isTall':True,
    }

for key, value in data.items():
    print(key,  ":", value)

fruits = {
    'name':'apple'
    'taste':'sweet'
    'color';'red'
}

for keys in fruits.keys():
    print(keys,  " : ", fruits[keys])