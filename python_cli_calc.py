#continue operations provided the calculator is on
on = True
while on:

#getting user inputs
# -- first number --
    num_1 = int(input("Enter the first number: "))
    
    # -- operation( +,-,*,/,%) --
    operator = input("Please enter the operation you want to carry out: ")
    
    # -- second number --
    num_2 = int(input("Enter the second number: "))


    #check what opertion was entered
    #performs the suitable operation
    #prints the result
    if operator == "+":
        print(str(num_1) + ' + ' + str(num_2) + ': ' + str(num_1 + num_2))
    elif operator == "-":
        print(str(num_1) + ' - ' + str(num_2) + ': ' + str(num_1 - num_2))
    elif operator == "*":
        print(str(num_1) + ' * ' + str(num_2) + ': ' + str(num_1 * num_2))
    elif operator == "/":
        print(str(num_1) + ' / ' + str(num_2) + ': ' + str(num_1 / num_2))
    elif operator == "%":
        print(str(num_1) + ' mod ' + str(num_2) + ': ' + str(num_1 % num_2))
    #return an error if a non-operator is entered
    else:
        print("The operation you are trying to carry out is invalid")

    #prints a short message to the user
   
    switch = input("\nThank you for using our calculator. Enter 'q' to exit or 'c' to continue. \n")

    #turns off the calculator if the user enters 'q'
    if switch == 'q':
        on = False
