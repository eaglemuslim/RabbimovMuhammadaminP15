from test import *

user = dict(
    username=input('username: '),
    password=input('password: ')
)

response = login(user)
if response:
    print('OK')
    print("1 - Tarix")
    print("2 - Matematika")
    print("3 - Ingliz tili")
    print("4 - Ona tili")
    print("5 - Adabiyot")
    update()


else:
    print("Let's register")
    data = dict(
        first_name=input("Enter your first name: "),
        last_name=input("Enter your last name: "),
        birth_day=input("Enter your birth_day (yyyy-dd-mm): "),
        phone=input("Enter your phone number: "),
        username=input("Enter your username: "),
        password1=input("Enter your password: "),
        password2=input("Password confirm: ")
    )

    create_table_user()
    response = insert_user(data)
    if response == 201:
        print('OK')

# data = dict(
#     name=input('Enter name: ')
# )
# insert_kurs(data)