import os
import csv

# Set path for file
data_csv = os.path.join("Resources", "PyBank_budget_data.csv")

# Open the CSV
with open(data_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter="," )

# Remove header
    print(next(csv_reader))

# Empty lists
    months = []
    profit = []
    profit_chg = []

# Go through values, add to list
    for row in csv_reader:
        months.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        profit_chg.append(profit[i+1]-profit[i])

# Max & Min amounts
inc = max(profit_chg)
dec = min(profit_chg)

month_inc = profit_chg.index(max(profit_chg))+1
month_dec = profit_chg.index(min(profit_chg))+1

# Print info
print("Finacial Analysis")
print("------------------------")
print(f"Total Months:{len(months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(profit_chg)/len(profit_chg),2)}")
print(f"Greatest Increase in Profits: {months[month_inc]} (${(str(inc))})")
print(f"Greatest Decrease in Profits: {months[month_dec]} (${(str(dec))})")

# Export
output = os.path.join("Analysis", 'PyBank_output.txt')
with open(output, "w") as pb:
    pb.write("Financial Analysis")
    pb.write("\n")
    pb.write("------------------------")
    pb.write("\n")
    pb.write(f"Total Months:{len(months)}")
    pb.write("\n")
    pb.write(f"Total: ${sum(profit)}")
    pb.write("\n")
    pb.write(f"Average Change: {round(sum(profit_chg)/len(profit_chg),2)}")
    pb.write("\n")
    pb.write(f"Greatest Increase in Profits: {months[month_inc]} (${(str(inc))})")
    pb.write("\n")
    pb.write(f"Greatest Decrease in Profits: {months[month_dec]} (${(str(dec))})")
    pb.write("\n")

