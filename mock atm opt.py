import random

database = database_user = {
   'Mark':'markanthony',
    'Lebron':'lebronjames',
    'Donald':'donaldtrump'
}
 
def init():


    print("Welcome to Bankcardano")


    have_account = int(input("Do you have an account with us: 1(Yes) 2 (No) \n"))

    if (have_account == 1):
        
        login()
    elif (have_account == 2 ):
        
        register()
    else:
        print("You have selected an invalid option")

        init()

def login():
   print("Sign in")
user_account_number = int(input("What is your account number? \n"))
password = input("What is your password \n")

for user_details, account_number in database.items():
    if (account_number == user_account_number):
             if (user_details[1] == password):
              bank_operations(user_details)
                  

    print("Invalid password")
    login()

def register():
    print("*********Register************")
    email = input("Email Address \n")
    first_name = input("First Name \n")
    last_name = input("Last Name \n")
    address = input("Residential Address \n")
    nationality = input("Nationality \n")
    number = input("Phone Number \n")
    password = input("Password \n")

    account_number = generate_account_number()

    database[account_number] = [email, first_name, last_name, address, nationality, number,password]

    print("Your account has been created")
    print("Your account number is: %d" % account_number)
    print("Do not disclose this to anyone")

    login()

def bank_operations(user):
    print("Welcome %s %s " % (user[1], user[2]))
    selected_option = int(input("What would you like to do? (1) Withdrawal (2) Deposit (3) Logout (4) Exit \n"))

    if(selected_option == 1):
        withdrawal_option()
    elif(selected_option == 2 ):
        deposit_option()
    elif(selected_option == 3):
        logout()
    elif(selected_option == 4):
        exit()
    else:
        print("Invalid option selected")
        bank_operations(user)


def withdrawal_option():
    print("Withdrawal")


def deposit_option():
    print("Deposit")

def generate_account_number(): 
    return random.randrange(1111111111,9999999999)

    print (generate_account_number())

def logout():
    login()

init()
