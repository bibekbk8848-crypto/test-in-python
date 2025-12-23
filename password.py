set_password = "admin123"
for i in range(5):
    user_input = input("enter a password :")
    if set_password == user_input:
        print("login successfully")
        break
    elif user_input == "":
        print("please write something")
        continue
    elif set_password != user_input:
        print("password is incorrect , please try again")
        continue