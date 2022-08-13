
#import dependances
import os
import csv



# direct python to the input file
poll_data_path = os.path.join("Resources", "election_data.csv")

#Results dictionary to store the results of the election
results = {}

# Open and read the results of the election
with open(poll_data_path, encoding='utf') as csvfile:
    poll_data = csv.reader(csvfile, delimiter=",")

    # loop through the rows and append the results dictionary
    for row in poll_data:
        candidate = row[2]
        if candidate in results:
            # add 1 to the current value;
            results[candidate] = results[candidate] + 1
        else:
            # create a new dictionary entry with 1 vote.
            results[candidate] = 1

    votes_cast = sum(results.values())

    # calculate the winner:
    winner = ""
    winningvotes = 0
    for winning_candidate in results:
        if results[winning_candidate] > winningvotes:
            winner = winning_candidate
            winningvotes = results[winning_candidate]

    # write out summary
    output = [
              f"----------------",
              f"Total votes cast: {votes_cast}",
              f"----------------"]
    # Election Results
    for participant in results:
        output.append(f"{participant}: {round((results[participant] / votes_cast * 100), 2)}% ({results[participant]})")

    output.append(f" ")
    output.append(f"The election winner is: {winner}")

# print output string
print()
for i in output:
    print(i)

# write output txt file
    Output_path = os.path.join("..","..", "Python-Challenge", "PyPoll", "resources", "election_data.txt")
    with open(Output_path, 'w') as textfile:
        textfile.write('Election Results')
        textfile.write('-----------------------------------------------------')
        textfile.write("\n".join(output))