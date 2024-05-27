import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Enter your username: ")
    if username in password_manager:
        print("Username already exists. Try another one.")
        return
    
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password  # Store the username and hashed password in the dictionary
    print("Account created")

def login():
    username = input("Type username: ")
    password = getpass.getpass("Password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager and password_manager[username] == hashed_password:  # Check if the username and password match what's stored in the dictionary
        print("Login successful")
    else:
        print("Invalid username or password")

def main():
    while True:
        choice = input("Type 1 to create an account, 2 to login, or 3 to quit: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()