def main():
    value1 = True

    while value1: # make a loop to repeat until entering valid values
        date1 = input('Enter the start date as \'DD-MM-YYYY\':')
        date2 = input('Enter the end date as \'DD-MM-YYYY\':')

        # making a list contains three elements (day, month, year)
        date1_list = date1.split('-')
        date2_list = date2.split('-')
        ## conditions to check if the dates entered are valid
        #
        if  date1_list[2].isdigit() and int(date1_list[2]) > 0: # checking the years
            if date1_list[1].isdigit() and int(date1_list[1]) > 0 and int(date1_list[1]) <= 12: # checking the months
                ## check the days for every month, since each month has different number of days
                #

                if date1_list[1] == '01':
                    if date1_list[0].isdigit() and int(date1_list[0]) > 0 and int(date1_list[0]) <= 31:
                        value1 = False
                    else:
                        print("Error! First date is not valid.")

                elif date1_list[1] == '02':
                    ## check if it is a leap year
                    # if it is a leap year then the days of Feb will be 29 days instead of 28 days

                    if int(date1_list[2]) %4 == 0:
                        if int(date1_list[2]) %100 == 0:
                            if int(date1_list[2]) %400 == 0:
                                if date1_list[0].isdigit() and int(date1_list[0]) > 0 and int(date1_list[0]) <= 29:
                                    value1 = False
                                else:
                                    print("Error! First date is not valid.")
                            else:
                                if date1_list[0].isdigit() and int(date1_list[0]) > 0 and int(date1_list[0]) <= 28:
                                    value1 = False
                                else:
                                    print("Error! First date is not valid.")
                        else:
                            if date1_list[0].isdigit() and int(date1_list[0]) > 0 and int(date1_list[0]) <= 29:
                                value1 = False
                            else:
                                print("Error! First date is not valid.")
                    else:
                        if date1_list[0].isdigit() and int(date1_list[0]) > 0 and int(date1_list[0]) <= 28:
                            value1 = False
                        else:
                            print("Error! First date is not valid.")

                elif date1_list[1] == '03':
                    if date1_list[0].isdigit() and int(date1_list[0]) > 0 and int(date1_list[0]) <= 31:
                        value1 = False
                    else:
                        print("Error! First date is not valid.")

                elif date1_list[1] == '04':
                    if date1_list[0].isdigit() and int(date1_list[0]) > 0 and int(date1_list[0]) <= 30:
                        value1 = False
                    else:
                        print("Error! First date is not valid.")

                elif date1_list[1] == '05':
                    if date1_list[0].isdigit() and int(date1_list[0]) > 0 and int(date1_list[0]) <= 31:
                        value1 = False
                    else:
                        print("Error! First date is not valid.")

                elif date1_list[1] == '06':
                    if date1_list[0].isdigit() and int(date1_list[0]) > 0 and int(date1_list[0]) <= 30:
                        value1 = False
                    else:
                        print("Error! First date is not valid.")

                elif date1_list[1] == '07':
                    if date1_list[0].isdigit() and int(date1_list[0]) > 0 and int(date1_list[0]) <= 31:
                        value1 = False
                    else:
                        print("Error! First date is not valid.")

                elif date1_list[1] == '08':
                    if date1_list[0].isdigit() and int(date1_list[0]) > 0 and int(date1_list[0]) <= 31:
                        value1 = False
                    else:
                        print("Error! First date is not valid.")

                elif date1_list[1] == '09':
                    if date1_list[0].isdigit() and int(date1_list[0]) > 0 and int(date1_list[0]) <= 30:
                        value1 = False
                    else:
                        print("Error! First date is not valid.")

                elif date1_list[1] == '10':
                    if date1_list[0].isdigit() and int(date1_list[0]) > 0 and int(date1_list[0]) <= 31:
                        value1 = False
                    else:
                        print("Error! First date is not valid.")

                elif date1_list[1] == '11':
                    if date1_list[0].isdigit() and int(date1_list[0]) > 0 and int(date1_list[0]) <= 30:
                        value1 = False
                    else:
                        print("Error! First date is not valid.")

                elif date1_list[1] == '12':
                    if date1_list[0].isdigit() and int(date1_list[0]) > 0 and int(date1_list[0]) <= 31:
                        value1 = False
                    else:
                        print("Error! First date is not valid.")
            else:
                print("Error! First date in not valid.")

        else:
            print("Error! First date is not valid.")


        ## Now, the second date
        # same as in the first date
        if date2_list[2].isdigit() and int(date2_list[2]) > 0:  # checking the years
            if date2_list[1].isdigit() and int(date2_list[1]) > 0 and int(date2_list[1]) <= 12:  # checking the months
                if date2_list[1] == '01':
                    if date2_list[0].isdigit() and int(date2_list[0]) > 0 and int(date2_list[0]) <= 31:
                        value1 = False
                    else:
                        print("Error! Second date is not valid.")

                elif date2_list[1] == '02':
                    ## check if it is a leap year
                    #
                    if int(date2_list[2]) % 4 == 0:
                        if int(date2_list[2]) % 100 == 0:
                            if int(date2_list[2]) % 400 == 0:
                                if date2_list[0].isdigit() and int(date2_list[0]) > 0 and int(date2_list[0]) <= 29:
                                    value1 = False
                                else:
                                    print("Error! Second date is not valid.")
                            else:
                                if date2_list[0].isdigit() and int(date2_list[0]) > 0 and int(date2_list[0]) <= 28:
                                    value1 = False
                                else:
                                    print("Error! Second date is not valid.")
                        else:
                            if date2_list[0].isdigit() and int(date2_list[0]) > 0 and int(date2_list[0]) <= 29:
                                value1 = False
                            else:
                                print("Error! Second date is not valid.")
                    else:
                        if date2_list[0].isdigit() and int(date2_list[0]) > 0 and int(date2_list[0]) <= 28:
                            value1 = False
                        else:
                            print("Error! Second date is not valid.")

                elif date2_list[1] == '03':
                    if date2_list[0].isdigit() and int(date2_list[0]) > 0 and int(date2_list[0]) <= 31:
                        value1 = False
                    else:
                        print("Error! Second date is not valid.")

                elif date2_list[1] == '04':
                    if date2_list[0].isdigit() and int(date2_list[0]) > 0 and int(date2_list[0]) <= 30:
                        value1 = False
                    else:
                        print("Error! Second date is not valid.")

                elif date2_list[1] == '05':
                    if date2_list[0].isdigit() and int(date2_list[0]) > 0 and int(date2_list[0]) <= 31:
                        value1 = False
                    else:
                        print("Error! Second date is not valid.")

                elif date2_list[1] == '06':
                    if date2_list[0].isdigit() and int(date2_list[0]) > 0 and int(date2_list[0]) <= 30:
                        value1 = False
                    else:
                        print("Error! Second date is not valid.")

                elif date2_list[1] == '07':
                    if date2_list[0].isdigit() and int(date2_list[0]) > 0 and int(date2_list[0]) <= 31:
                        value1 = False
                    else:
                        print("Error! Second date is not valid.")

                elif date2_list[1] == '08':
                    if date2_list[0].isdigit() and int(date2_list[0]) > 0 and int(date2_list[0]) <= 31:
                        value1 = False
                    else:
                        print("Error! Second date is not valid.")

                elif date2_list[1] == '09':
                    if date2_list[0].isdigit() and int(date2_list[0]) > 0 and int(date2_list[0]) <= 30:
                        value1 = False
                    else:
                        print("Error! Second date is not valid.")

                elif date2_list[1] == '10':
                    if date2_list[0].isdigit() and int(date2_list[0]) > 0 and int(date2_list[0]) <= 31:
                        value1 = False
                    else:
                        print("Error! Second date is not valid.")

                elif date2_list[1] == '11':
                    if date2_list[0].isdigit() and int(date2_list[0]) > 0 and int(date2_list[0]) <= 30:
                        value1 = False
                    else:
                        print("Error! Second date is not valid.")

                elif date2_list[1] == '12':
                    if date2_list[0].isdigit() and int(date2_list[0]) > 0 and int(date2_list[0]) <= 31:
                        value1 = False
                    else:
                        print("Error! Second date is not valid.")
            else:
                print("Error! Second date in not valid.")

        else:
            print("Error! Second date is not valid.")


    days = calculator(date1, date2, date1_list, date2_list) # putting the returned value of (calculate) function in variable
    print(f'Difference is {days} days')


def calculator(date1, date2, date1_list, date2_list): # function to calculate the difference
    from datetime import datetime

    d1 = datetime.strptime(date1, '%d-%m-%Y') # defining the first date
    d2 = datetime.strptime(date2, '%d-%m-%Y') # defining the second date

    difference = d2 - d1 # calculating the difference between the two dates
    return difference.days # return the difference in days


main()

