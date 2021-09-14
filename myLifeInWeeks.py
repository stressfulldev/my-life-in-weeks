print("How Many Weeks Left Your Live Have?")
while True :
    age = input("What is your current age? ")

    ninetyonmonth = (90 * 12) - (int(age) * 12)
    ninetyonweeks = (90 * 52) - (int(age) * 52)
    ninetyondays = (90 * 365) - (int(age) * 365)

    print(f"You have {ninetyondays} days, {ninetyonweeks} weeks, and {ninetyonmonth} months left. \n")

    while True :
        restart = input("Do you want to know how many weeks left for other people? (y/n): ")
        if restart in ("yu, n"):
            break
    if restart == "y":
        continue
    else :
        print("Thanks for using the Apps, Have a Good Life !")
        break