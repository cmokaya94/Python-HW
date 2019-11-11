import os 
import csv
voter_id = []
county = []
candidate = []
candidate_count = []
winner = 0

cvspath_1 = os.path.join("Resources","election_data.csv")
output_file = os.path.join("Output.txt")

with open(cvspath_1,newline='') as file_1:
    filereader = csv.reader(file_1)
    filereader_1 = next(filereader)
    for lines  in filereader:
        voter_id.append(lines[0])
        county.append(lines[1])
        candidate.append(lines[2])
        
total_votes = len(voter_id)              
khan_count = candidate.count("Khan")
corey_count = candidate.count("Correy")
li_count = candidate.count("Li")
OTooley_count = candidate.count("O'Tooley")

winner_1 = {
    "Khan": khan_count,
    "Correy": corey_count,
    "Li": li_count,
    "Otooley":OTooley_count
    }

winner =max(zip(winner_1.values(),winner_1.keys()))
winner_final = winner[1]


khan_percent = (khan_count / total_votes) * 100
corey_percent = (corey_count / total_votes) * 100
li_percent = (li_count/total_votes) * 100
OTooley_percent = (OTooley_count/total_votes) * 100

percent_khan = (round(khan_percent,2))
percent_corey = (round(corey_percent,2))
percent_li =  (round(li_percent,2))
percent_otooley = (round(OTooley_percent,2))
round(10.5,2)

print(total_votes)
print(khan_count)
print(corey_count)
print(winner_final)
print(percent_khan)
#print(li_count)
#print(OTooley_count)
#print(round(khan_percent,2))
#print(corey_percent)
#print(li_percent)
#print(OTooley_percent)


print("Election Results")
print("-----------------------")
print("Total Votes: " + str(total_votes) )
print("-----------------------")
print("Khan: " + str(percent_khan)+ "00" + " ("+  str(khan_count) +")")
print("Correy: " + str(percent_corey) +"00" + " (" + str(corey_count)+")")
print("Li: " + str(percent_li) +"00" + " (" +  str(li_count) +")")
print("O" + "'" + "Tooley:"   +str(percent_otooley) +"00" + " (" + str(OTooley_count) + ")")
print("-----------------------")
print("Winner: " + str(winner_final))



with open(output_file,"w") as file_1:
    file_1.write(f"Election Results\n")
    file_1.write(f"-----------------------------\n")
    file_1.write(f"Total Votes: " + str(total_votes)+ "\n")
    file_1.write(f"-----------------------------\n")
    file_1.write(f"Khan: " + str(percent_khan) +"00" + " (" +  str(khan_count) +")" + "\n")
    file_1.write(f"Correy: " + str(percent_corey) +"00" +  " (" + str(corey_count) +")" + "\n")
    file_1.write(f"Li: " + str(percent_li) +"00" + " (" + str(li_count) + ")" + "\n")
    file_1.write(f"O" + "'" + "Tooley:"  + str(percent_otooley) +"00" + "("+  str(OTooley_count) +")" + "\n")
    file_1.write(f"-----------------------------\n")
    file_1.write(f"Winner: " + str(winner_final) +"\n")
    file_1.write(f"-----------------------------\n")
    


    

