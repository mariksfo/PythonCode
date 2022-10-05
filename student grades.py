percentages = [
    {'name':'Ali', 'Percentage':91},
    {'name':'ben', 'Percentage':89},
    {'name':'alex', 'Percentage':65},
    {'name':'michelle', 'Percentage':96},
    {'name':'stark', 'Percentage':50},
]

grade = {}

for students in percentages:
    percentage = students['Percentage']
    name = students['name']
    if percentage >=95:
        print("{} got A+ grade".format(name))
        grade[name] = 'A+'
    elif percentage > 90 and percentage <95:
        print("{} got A grade".format(name))

    elif percentage < 90 and percentage > 80:
        print("{} got B grade".format(name))
        grade[name] = 'B'

    elif percentage < 80 and percentage > 60:
        print("{} got D grade".format(name))

    else:
        print("{} failed".format(name))
        grade[name] = 'F'