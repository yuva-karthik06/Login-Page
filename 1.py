import random
import string

users = {
    "YUVA": "yuva@11223",
    "Karthik": "Karthik122@",
    "yuvakarthik": "karthik2*&23344"
}

def generate_password(password):
    characters = list(password)
    new_password = ''

    list1 = list(string.ascii_letters + string.digits + string.punctuation)
    list2 = list(string.digits + string.ascii_letters)

    random.shuffle(list2)

    while len(list2) < len(list1):
        list2.extend(list2)
    list2 = list2[:len(list1)]

    for char in characters:
        if char in list1:
            index = list1.index(char)
            new_password += list2[index]
        else:
            new_password += char

    return new_password

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password!")

def forgot_password():
    username = input("Enter username: ")

    if username in users:
        new_password = generate_password(users[username])
        print(f"New password for {username}: {new_password}")
    else:
        print("User not found!")

def main():
    while True:
        print("1. Login")
        print("2. Forgot Password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            login()
        elif choice == '2':
            forgot_password()
        elif choice == '3':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()
