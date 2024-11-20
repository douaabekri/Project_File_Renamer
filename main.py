from FileRenamer import File  

USER_DATA_FILE = "users1.txt"

usernames = []
passwords = []

def load_users():
    try:
        with open(USER_DATA_FILE, 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                usernames.append(username)
                passwords.append(password)
    except FileNotFoundError:
        pass

def save_user(username, password):
    with open(USER_DATA_FILE, 'a') as file:
        file.write(f"{username},{password}\n")

def sign_up():
    username = input("\033[33m" +"Enter a username: "+"\033[0m").strip()
    if username in usernames:
        print("\033[31m"+"Username already taken. Please try another."+"\033[0m")
        return
    
    password = input("\033[33m" +"Enter a password: "+"\033[0m").strip()
    usernames.append(username)
    passwords.append(password)
    save_user(username, password)  
    
    print("\033[34m "+"Sign-up successful! You can now log in."+"\033[0m")

def login():
    username = input("\033[33m" +"Enter your username: "+"\033[0m").strip()
    if username not in usernames:
        print("\033[31m "+"Username not found. Please sign up first."+"\033[0m")
        return
    
    password = input("\033[33m" +"Enter your password: "+"\033[0m").strip()
    user_index = usernames.index(username)
    
    if passwords[user_index] == password :
        print("\033[34m "+f"Login successful! Welcome, {username}."+"\033[0m")
        File.FileRenamer() 
    else:
        print("\033[31m" +"Incorrect password. Please try again."+"\033[0m")

if __name__ == "__main__":
    load_users() 
    
    while True:
        print("\033[33m" +"\n __________|| Menu ||__________"+"\033[0m")
        print("1. Sign Up")
        print("2. Login")
        print("3. Quit")
        
        choice = input("\033[33m" +"Choose an option: "+"\033[0m").strip()
        
        if choice == "1":
            sign_up()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("\033[31m" +"Invalid option. Please try again."+"\033[0m")