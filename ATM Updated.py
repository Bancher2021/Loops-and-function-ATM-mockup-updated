allowedUsers = ['Seyi','Mike','Love']
allowedPassword = ['passwordSeyi','passwordMike','passwordLove']

import random

def generation_account_number():
    return random.randrange(1111111111, 9999999999)
def init():
    print("***Welcome to Bancher Community Bank***")

    print("Do you have account with us: \n 1.YES \n 2.NO")

    actionSelect = int(input("please select an option: \n"))

    if actionSelect == 1:
        login()
    elif actionSelect == 2:
        print("Do you want to register with us?")
        print("1.yes")
        print("2.No")
        selectedOption = int(input('Please select an option: \n'))
        if(selectedOption == 1):
            register()
        elif(selectedOption == 2):
            print("Have a nice day")
            exit()
    else:
        print("You have selected invalid option please try again later")
        print("Do you wish to continue?")
        print("1.yes")
        print("2.No")
        selectedOption = int(input('Please select an option: \n'))
        if(selectedOption == 1):
            init()
        elif(selectedOption == 2):
            exit()

def login():
     #login function here

    name = input("Input your name? \n")
    if(name in allowedUsers):
        password = input('Your password? \n')
        userId = allowedUsers.index(name)
        if(password == allowedPassword[userId]):
            print('Welcome %s' % name)
    elif(name not in allowedUsers):
        print("Name not found")
        print("Do you want to register with us?")
        print("1.yes")
        print("2.No")
        selectedOption = int(input('Please select an option: \n'))
        if(selectedOption == 1):
            register()
        elif(selectedOption == 2):
            print("Have a nice day")
            exit()
             
    else:
        print("Password or Username Incorrect. Please try again")
    
def register():
    #registration function
    print("****** Register *******")

    email = input("What is your email address? \n")
    newUser = input("Enter your name? \n")
    newpassword = input("Enter password \n")
    allowedUsers.insert(0,newUser)
    allowedPassword.insert(0,newpassword)
    
    account_number = generation_account_number()

    print('Welcome %s' % newUser)
    
    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % account_number)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")
    print("You can now login")
    
    login()
    
def bankOperations():
    print('Available Options')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')

    selectedOption = int(input('Please select an option: \n'))
            
    if(selectedOption == 1):
        print("How much do you want to withdraw? ")
        amount = int(input("Enter amount \n"))
        print("Please take your cash %s" % amount)
        return amount
                   
    elif(selectedOption == 2):
        print("How much do you want to deposit")
        deposit = int(input("Enter amount \n "))
        print("You deposited %s" % deposit)
                
    elif(selectedOption == 3):
        print(input("Please enter complain \n"))
        print("Your complain is recevied thank you")
        
    elif(selectedOption == 4):
        exit()   
    else:
        print('Invalid Option selected, please try again')

init()
bankOperations()







        






























