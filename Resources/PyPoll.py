# The data we need to retrieve 
# 1. the total # of votes cast
# 2. a complete list of candidates who receied votes
# 3. The % of votes each candidate won 
# 4. The total # of votes each candidate won
# 5. the winner of the election based on popular votes

import csv
import os
# Assigning variable to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assigning variable to save file to path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the file to just read
with open(file_to_load) as election_data:
    # read and analyze the data using reader function
    file_reader = csv.reader(election_data)
    # print each row in the csv file
    headers = next(file_reader)
    print(headers)

#writing to files

#opening the file with the 'w' mode to write data to the file
# open(file_to_save, "w") //// This code to open a working document in vs code
# using the with statment, open the file as text file
#with open(file_to_save, "w") as txt_file:
    # write data to test
    # txt_file.write("Arapahoe, Denver, Jefferson") --- outputs all on the same line
    # to write on separate lines, between each county type '\n' essentially saying return
    #txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")
