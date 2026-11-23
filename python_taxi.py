
import time
import random
print("welcome a TTTTS (Trinidad and Tobago taxi and transtiast servers)")

#unfinished
def book_taxi():
    print("you are in booking page")

#unfinished
def payment():
    print("you are in payment page")

#main dashboard where users can book and pay
def dashboard():
    distances = [1.5, 2.7, 3.8, 5.2, 7.9]

    while True:
        distance = random.choice(distances)
        print("closest Taxi distance:", distance, end="\r", flush=True)
        time.sleep(1)
        print("\n--- TTTTS DASHBOARD ---")
        print("1. Book a taxi")
        print("2. Payment")
        print("3. Logout")
        
        userin = input("What would you like to do? ")

        if userin == "1":
            book_taxi()

        elif userin == "2":
            payment()

        elif userin == "3":
            print("Logging out...")
            auth_logout()
        

        else:
            print("Invalid selection")
    


    loginuser = ""
    loginpass = ""

# page after getting the login wrong
def auth_login():
    print("That user or password is not correct. Please try again.")
    user = input("username:")
    passw  = input("password:")      
    
    if user == loginuser and passw == loginpass:
        print("Enjoy TTTTS")
        dashboard()
    else:
        auth_login()

def auth_logout():
    print("you logged out enter username and password to log in.")
    user = input("username:")
    passw  = input("password:")      
    
    if user == loginuser and passw == loginpass:
        print("Enjoy TTTTS")
        dashboard()
    else:
        auth_login()

#login page
def login():
    global loginuser, loginpass
    print("please create an account")
    loginuser = input("Create username:")
    loginpass = input("Create password:")

    print(" account created! Please login")
    user = input("username:")
    passw  = input("password:")

    if user == loginuser and passw == loginpass:
        print("Enjoy TTTTS")
        dashboard()
    else:
        auth_login()


login()