def GetInput():
    num_1 = int(input('Enter First number: '))
    num_2 = int(input('Enter Second number: '))
    return num_1,num_2

def Add():
    a,b = GetInput()
    return a+b

def Sub():
    a,b = GetInput()
    return a-b

def Div():
    a,b = GetInput()
    return a/b

def Mul():
    a,b = GetInput()
    return a*b

def Exit():
    pass

while True:
    print(
        '''
        Enter number for the opration:
        1.Addtion
        2.Subtraction
        3.Divison
        4.Multipication
        5.Exit
    ''')
    choice = int(input('Enter your choice: '))
    opration =[Add,Sub,Div,Mul,Exit]
    output = opration[choice - 1]()
    if choice == 5:
        print('Thank you for using calculator')
        break
    else:
        print(f'The result is:{output}')