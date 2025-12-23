# grade checking.....
score=int(input("enter your score"))
if score <=90 and score> 80:
    print("grade A:")
elif score <=70 and score> 60:
    print("grade B:")
elif score <=50 and score> 40:
    print("grade C:")
elif score <=40 and score> 30:
    print("grade D:")
elif score == 25:
    print("pass")
else:
    print("fail") 