import os
import csv

# Set pathh for file
data_csv = os.path.join("Resources", "PyPoll_election_data.csv")

# Open csv
with open(data_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter="," )

# Remove header
    print(next(csv_reader))

# Create list of votes etc
    Total_votes = 0
    Khan = 0
    Correy = 0
    Li = 0
    OTooley = 0
    Candidate = set()
    Winner = 0

# Looping
    for row in csv_reader:
        Total_votes += 1
        Candidate.add(row[2])
    

# Votes per candidate
        if (row[2] == "Khan"):
            Khan += 1
        elif (row[2] == "Correy"):
            Correy += 1
        elif (row[2] == "Li"):
            Li += 1
        else:
            OTooley += 1

# Percentage of votes per candidate
Khan_percent = (Khan/Total_votes)
Correy_percent = (Correy/Total_votes)
Li_percent = (Li/Total_votes)
OTooley_percent = (OTooley/Total_votes)

# Winner based on votes
Total_votes = [Khan, Correy, Li, OTooley]
WinnerCount = max(Total_votes)
Name = ""

# Check for winner
if WinnerCount == Khan :
    Name = "Khan"
elif WinnerCount == Correy :
    Name = "Correy"
elif WinnerCount == Li :
    Name = "Li"
elif WinnerCount == OTooley :
    Name = "O'Tooley"

else :
    Name = "No winner"


# Print
print("Election Results")
print("---------------------")
print("Total Votes: " + str(Total_votes))
print("---------------------")
print("Khan: " + "{:.3%}".format(Khan_percent) + " " + (str(Khan)))
print("Correy: " + "{:.3%}".format(Correy_percent) + " " + (str(Correy)))
print("Li: " + "{:.3%}".format(Li_percent) + " " + (str(Li)))
print("O'Tooley: " + "{:.3%}".format(OTooley_percent) + " " + (str(OTooley)))
print("---------------------")
print("Winner: " +  Name)
print("---------------------")

# Export 
output = os.path.join("Analysis", 'PyPoll_output.txt')
with open(output, "w") as pp:
    pp.write("Election Results")
    pp.write("\n")
    pp.write("---------------------")
    pp.write("\n")
    pp.write("Total Votes: " + str(Total_votes))
    pp.write("\n")
    pp.write("---------------------")
    pp.write("\n")
    pp.write("Khan: " + "{:.3%}".format(Khan_percent) + " " + (str(Khan)))
    pp.write("\n")
    pp.write("Correy: " + "{:.3%}".format(Correy_percent) + " " + (str(Correy)))
    pp.write("\n")
    pp.write("Li: " + "{:.3%}".format(Li_percent) + " " + (str(Li)))
    pp.write("\n")
    pp.write("O'Tooley: " + "{:.3%}".format(OTooley_percent) + " " + (str(OTooley)))
    pp.write("\n")
    pp.write("---------------------")
    pp.write("\n")
    pp.write("Winner: " +  Name)
    pp.write("\n")
    pp.write("---------------------")
    pp.write("\n")