from db_config import User

introduction = f"""===== Welcome to CRM Application =====
[S]how: Show all users info
[A]dd: Add new user
[Q]uit: Quit The Application
======================================"""

print(introduction)

while True:

    your_command = input("your command > ")

    if your_command == "S":
        users = User.select()
        for person in users:
            print(f"Name: {person.user} Age: {person.age}")

    elif your_command == "A":
        new_user_name = input("New User Name > ")
        new_user_age = input("New User Age > ")
        User.create(user=new_user_name, age=new_user_age)
        print(f"Add New User: {new_user_name}")

    elif your_command == "Q":
        print("Bye!")
        break

    else:
        print(f"{your_command}: command not found")
        continue
