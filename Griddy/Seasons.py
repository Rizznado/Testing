#month input
def month_season():
    while True:
        global month
        month = int(input("Enter month by number: "))
        if month not in range(1,13):
                    print("Please enter months between 1-12")
        else:
            break
#Calculation
month_season()

if month in range(1,3) or month == 12:
    print("The season is winter")
elif month in range (3,6):
    print("The season is spring")
elif month in range(6,9):
    print("The season is summer")
elif month in range(9,12):
    print("The season is autumn")



