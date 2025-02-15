
def library():
    a=int(input('Press 1 to explore library\nPress 2 to exit\n'))
    if a==2:
        print('Thanks for visit')
    elif a==1:
        b=int(input('For Programming press 1\nFor Data Science / Business press 2\nFor Business / Entrepreneurship press 3\nFor Software Development press 4\nForSelf-Help / Productivity press 5\n'))
        if b==1:
            print('Book code 101\nName:Python Crash Course\nEdition:2016')
        if b==2:
            print('Book code 102\nName;Data Science for Business\nEdition:2012')
        if b==3:
            print('Book code 103\nName:The Lean Startup\nEdition:2023')
        if b==4:
            print('Book code 104\nName:The Pragmatic Programmer\nedition:2024')
        if b==5:
            print('Book code 105\nName:Atomic Habits\nEdition:2010')
        return library()
    else:
        print('Please take a look into your command')
        return library()

print('Welcome to library management system')
library()





