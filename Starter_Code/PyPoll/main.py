#import required modules for the task.
import os
import csv

#use os.path to join the csv file to ensure the robust and portable file access.
election_data_csv = os.path.join("Resources", "election_data.csv")
# using file handle to open the csv file in read mode.
with open(election_data_csv, "r") as f:
    # using reader to read through the file with comma as seperator.
    csv_reader = csv.reader(f, delimiter=",")
    # skip the file header by reading the next line.
    csv_header = next(csv_reader)

    total = 0 #set the variable to store the total votes in the loop.

    candidates_votes_dic = {} # Here I decided to use dictionary for storing the candiates/votes as key/value pairs.
    # loop throught the file line by line to extract data.
    for line in csv_reader:
        # increment total votes each time.
        total += 1
        candiate = line[2] # using list index slicing to get candidates' name.

    #Here is the main part, while looping, initially the dict is empty, so we set the condition that if we ever encounter
    #the same candiate again, the vote of this candiate will increment by 1. but if we never encounter the candidate before
    # after first enconter we will store this candiate once. so according to the key/value pair, candidates_votes_dic[candidate]
    #is the name of candidate. and as it's in the same list, so when candiate increments, the corresponding votes (as values) will
    #also increment as we expected.
        if candiate in candidates_votes_dic:
            candidates_votes_dic[candiate] += 1
        else:
            candidates_votes_dic[candiate] = 1

#create an empty list to store all the results need to be printed later.
print_result = []
print_result.append('Election Results\n')
print_result.append("-------------------------\n")
print_result.append(f"Total Votes: {total}\n")
print_result.append("-------------------------\n")

#here I set the variables to find the candiate with the most votes.
most_vote = 0
winner = ''

# Here is another important step, use loop to go through all the key/value pair in dict. .item() will enables the
#loop to parse as list contain tuple form, so in the tuple we will have the information we need to extract.
for candiate, vote in candidates_votes_dic.items():
    percentage_vote = round((float(vote / total)* 100), 3) # Apply the correct formating as required.
    print_result.append(f"{candiate}: {percentage_vote}% ({vote})\n") # Also store the value in the list.

    # Here we compare the votes between each other, the largest vote will become the variable and it's corrspond key
    # is the candiate.
    if vote > most_vote:
        most_vote = vote
        winner = candiate

#keep storing the result.
print_result.append("-------------------------\n")
print_result.append(f"Winner: {winner}\n")
print_result.append("-------------------------\n")

#now print all the results line by line.
for line in print_result:
    print(line, end="")

# export the result in to .txt file into the required directory.
output_file_path = os.path.join("analysis", "election_data_analysis.txt")
with open(output_file_path, "w") as out_file:
    for line in print_result:
        out_file.write(line)


