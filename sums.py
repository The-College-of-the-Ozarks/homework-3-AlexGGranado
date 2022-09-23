# sums.py
#
# 

#Define menu function
def menu():
    print('Which function would you like to use?')
    print('1: Sum')
    print('2: Sum of squares')
    print('3: Sum of cubes')
    print('4: Change x value')
    print('5: Exit')
    choice = input('Input the number corresponding to your choice: ')
    return choice

#Takes user input
x = input('Input a nonnegative integer: ')
x = float(x)

choice = menu()


#Define sums command
def GetSums():
    counter = 0
    addition = 0
    while counter < x:
        counter = counter + 1
        addition = addition + counter
    return addition

#Define sum of squares command
def GetSumSqrs():
    counter = 0
    square = 0
    while counter < x:
        counter = counter + 1
        square = counter * counter + square
    return square

#Define sum of cubes command
def GetSumCubes():
    counter = 0
    cube = 0
    while counter < x:
        counter = counter + 1
        cube = counter * counter * counter + cube
    return cube
#Defines functions as variables
#GetSum = GetSums()
#GetSumSqr = GetSumSqrs()
#GetSumCube = GetSumCubes

#Prints output
while choice != '5':
    GetSum = GetSums()
    GetSumSqr = GetSumSqrs()
    GetSumCube = GetSumCubes()
    if choice == '1':
        print("The sum of the parameter of ",x," is",GetSum,".")
    elif choice == '2':
        print("The sum of all squares of the paramater",x,"is",GetSumSqr,".")
    elif choice == '3':
        print("The sum of all cubes of the parameter of",x,"is",GetSumCube,".")
    elif choice == '4':
        x = input("Input new x value: ")
        x = float(x)
    else:
        print("Invalid menu option")
    
    choice = menu()

print("Exiting program.")