import os 
import csv

months = []
total = []
changes = []
final_changes = []
min_month = 0
max_month = 0


cvspath = os.path.join ("Resources","budget_data.csv")
output_file = os.path.join("Output.txt")


with open(cvspath,newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    csvreader1 = next(csvreader)
    for lines in csvreader:  
        months.append(lines[0])
        total.append(int(lines[1]))
        changes = [total[i+1] - total[i] for i in range(len(total)-1)]
        total_change = sum(changes)
        total_sum = sum(total)
        months_total = len(months)

    avg_change = total_change/(len(months) - 1)
    max_change = max(changes)
    min_change = min(changes)

    
for i in range(len(changes)): 
     if changes[i] == max_change:
         max_change = changes[i]
         max_month = months[i+1]

     elif changes[i] == min_change:
        min_change = changes[i]
        min_month = months[i+1]
     else:
        continue




print("Financial Analysis")
print("-----------------------")
print("Total Months: " + str(months_total) )
print("Total: " + "$" + str(total_sum))
print("Average Change: " + str(avg_change))
print("Greatest Increase in Profits: " + str(max_month) + ": " +  "($" + str(max_change) + ")")
print("Greatest Decrease in Profits: " + str(min_month) + ": " +  "($" + str(min_change) + ")")



with open(output_file,"w") as file_1:
    file_1.write(f"Financial Analysis\n")
    file_1.write(f"-----------------------------\n")
    file_1.write(f"Total Months: " + str(months_total)+ "\n")
    file_1.write("Total : " + "$" + str(total_sum) + "\n")
    file_1.write(f"Average Change : " + "$" + str(avg_change) + "\n")
    file_1.write(f"Greatest Increase in Profits: " + str(max_month) + ": " +"(" + "+$" + str(max_change) +")" + "\n")
    file_1.write(f"Greatest Decrease in Profits: " + str(min_month) + ": " +"(" + "-$" + str(min_change) +")" + "\n")



