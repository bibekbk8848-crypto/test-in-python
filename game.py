serect_number = 38
for i in range(8):
    user_input =int (input("guess the number :"))
    if serect_number == user_input:
        print("correct number")
        break
    elif user_input > serect_number:
        print("high number")
        continue
    elif user_input < serect_number:
        print("low number")
        continue