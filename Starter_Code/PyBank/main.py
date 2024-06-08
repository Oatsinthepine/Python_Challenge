# import all required modules for this task.
import os
import csv

# use os.path to join the csv file to ensure the robust and portable file access.
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# using file handle to open the csv file in read mode.
with open (budget_data_csv, "r") as f:
    # using reader to read through the file with comma as seperator.
    csv_reader = csv.reader(f, delimiter=",")
    #skip the file header by reading the next line.
    csv_header = next(csv_reader)

    # creates all required variables for later.
    total_month = 0 # this will be the total month
    net_profit = 0 # this will be the total.
    value_from_pre_month = None # Here I set this variable to special value None for later reassignment when calculating profit/loss betweem each month.
    average_change = 0 # this will be Average change.

    # Here I create two empty lists for storing the data extracted from the loop.
    value_change = [] # this will store the difference between the value from adjacent month
    Dates = [] # This will store the Month-year.

    # Using for loop to iterate over the csv data by reading each line.
    for line in csv_reader:
        #assign date to the first element of the list
        date = line[0]
        #assign the value to be the second element of the list.
        value = int(line[1])
        #now increment total month as looping each time by adding one.
        total_month += 1
        # here increment the total value by adding the values one by one.
        net_profit += value

        #This part is important, as I initially set the variable to Nonetype. When looping, to ensure it calculate correctly, to kick start, we need to
        # discard the very first varible value, which is None, then the value of differnt can be calculated correctly by peforming the second subtract the first then moving on.
        # as Nonetype cannot perform mathematical operations. This if also severe as a condition filter to check if there are other None type
        # when parsing the csv file, even though we do not have none type in the following csv files.
        if value_from_pre_month != None:
            change_between_each_month = value - value_from_pre_month #To calculate the change in profit/loss, subtract the current value by the previous one.
            value_change.append(change_between_each_month) # add the value change to the list.
            Dates.append(date) # add the corresponding date to the list as well.

    #Here is important, As looping, we set the base of next value to subtract to be the previous month's value.
        value_from_pre_month = value
    #Here we calculate the average of changes by using the sum of all value changes divided by the total number of date, andwe round it to 2 decimals
    # as requested.
    average_change = round(sum(value_change) / len(value_change), 2)

    #here I check if the two lists have the same length, because later I will combine two list into one list using zip()
    #just to ensure they have the same length.
    if len(value_change) == len(Dates):

        combined = list(zip(Dates, value_change)) # I combined the lists.
        greatest_increase_value = float('-inf') #Here I set the comparison marker to be negative infinity in order to compare the biggest value change.
        greatest_decrease_value = float('inf') # the same idea, comparison marker to positive infinity for biggest decrease.
        # this will be the date corresponding to bigest increase/decrease.
        max_date = ''
        min_date = ''
        # using for loop to go through the combined list, after combined the data will be stroed in tuple, so tuple[0] is the date
        # and tuple[1] is the value.
        for date, value in combined:
        #here we compre each value in each tuple with the comparision marker, if the current > marker, current will be the
        #marker, if the next value greater than the current value. The next value will be the biggest one. Same as the smallest.
            if value > greatest_increase_value:
                greatest_increase_value = value
                max_date = date #when find the required value, the date in it's tuple will be the month-year we need.
            if value < greatest_decrease_value:
                greatest_decrease_value = value
                min_date = date

# Print all the required values in the format.
print("Financial Analysis")
print("----------------------------")
print(f"Total Month: {total_month}")
print(f"Total : {net_profit}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {max_date} " +  "$" + "("+str(greatest_increase_value)+")")
print(f"Greatest Decrease in Profits: {min_date} " + "$" + "("+str(greatest_decrease_value)+")")

#declear the output file path.
output_file_path = os.path.join("analysis", "analysis_report.txt")

#write the results line by line to the required path.
with open(output_file_path, "w") as out_file:
    out_file.write(f"Financial Analysis \n")
    out_file.write(f"---------------------------- \n")
    out_file.write(f"Total Month: {total_month}\n")
    out_file.write(f"Total : {net_profit}\n")
    out_file.write(f"Average Change: {average_change}\n")
    out_file.write(f"Greatest Increase in Profits: {max_date} " +  "$" + "("+str(greatest_increase_value)+")\n")
    out_file.write(f"Greatest Decrease in Profits: {min_date} " + "$" + "("+str(greatest_decrease_value)+")\n")
