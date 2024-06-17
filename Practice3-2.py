##Robert Fernandez
#Complete
#Display the days of the week given an integer 1-7


weekday = int(input("Enter a number for the day of the week from 1 to 7. "))

if weekday < 1 or weekday > 7:
    print("Invalid input.")
else:
    if weekday == 1:
        print("Monday")
    else:
        if weekday == 2:
            print("Tuesday")
        else:
            if weekday == 3:
                print("Wednesday")
            else:
                if weekday == 4:
                    print("Thursday")
                else:
                    if weekday == 5:
                        print("Friday")
                    else:
                        if weekday == 6:
                            print("Saturday")
                        else:
                            if weekday == 7:
                                print("Sunday")
                            else:
                                print("Invalid input.")
        
