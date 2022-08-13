import os
import csv
import statistics

# path to the csv file
csv_path = os.path.join("Resources", "budget_data.csv")

## creating a list where the monthly data is added




count_month = 0
monthly_profit_loss = []
month = []
net_profit_loss = 0
profit_loss_change = 0
initial_profit = 0

with open(csv_path, encoding='utf') as csvfile:
    bank_data = csv.reader(csvfile, delimiter=",")

    # print (csvreader)
    # read header row first
    csv_header = next(bank_data)
    print(f'CSV header: {csv_header}')

    for row in bank_data:
        count_month += 1
        month.append(row[0])
        monthly_profit_loss.append(int(row[1]))
        net_profit_loss = net_profit_loss + int(row[1])
        final_profit = int(row[1])
        month_change = final_profit - initial_profit
        monthly_profit_loss.append(month_change)
        profit_loss_change = profit_loss_change + month_change
        initial_profit = final_profit


## create an output

    monthly_average = round((month_change/count_month),2)

    output = ["FINANCIAL REPORT",
        f"--------------------------------------------------------------------",
        f"The total number of months for the report is: {len(month)}",
        f"The total profit during this period is: ${sum(monthly_profit_loss)}",
        f"The average monthly profit is : ${monthly_average}",
        f"Greatest highest monthly profit is: ${max(monthly_profit_loss)}",
        f"The lowest monthly profit is: ${min(monthly_profit_loss)}",
        f"--------------------------------------------------------------------",
    ]
    print(monthly_average)
    print(len(month))
    print(month)
    print(final_profit)
    #print(monthly_profit_loss)

    for i in output:
        print(i)

    # write output txt file
    Output_path = os.path.join("..","..", "Python-Challenge", "Pybank", "resources", "budget_data.txt")
    with open(Output_path, 'w') as textfile:
        textfile.write("\n".join(output))





