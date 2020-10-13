yes = ['Y', 'Yes', 'Yeah', 'Sure', 'Ok']
no = ['N', 'No', 'Nope']

print('''Welcome to Date Asker\n
I enjoyed our first date and would like to hang out
and get to know you better.''')

loop = 1

while loop == 1:
    answer = input('Would you like to go on another date? y/n \n').title()
    if answer in yes:
        print("That's great! Let's do something fun. Send me a message. :) ")
        break
    if answer in no:
        print('Aww. Sorry to hear that. Take it easy!')
        break
    else:
        print("Please enter a valid entry. I can't handle maybes. Only, y/n. \n")
        loop == 1
        
