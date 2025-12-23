  # wap using match case
month = input("enter a month")
match month:
    case "janurary":
        print("janurary is very cold month")
    case "feburary":
        print("feburary is second month")
    case "march":
        print("march is beautiful month")
    case "april":
        print("april is fourth month")
    case _:
        print("invalid score")