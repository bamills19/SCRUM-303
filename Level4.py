Go = True 
#utilize lists
expenses = []
#ask expenses
print("Enter your expenses ")
print("Enter 0 when complete")
#loop so multiple variables can be entered... use list to store multiple
while Go == True:
    value = int(input("Enter your expenses here: $"))
    if value == 0:
        Go = False
    elif value < 0:
        print("Invalid value. Try again.")
    else:
        expenses.append(value)
#Make counts for each range as well as avoid empty list error
if len(expenses) == 0:
    print("No expenses were entered!")
else: 
    small_count = 0
    med_count = 0
    large_count =0
    #clarify expense ranges
for i in expenses:
    if i <= 25:
        small_count += 1
    elif i >= 25 and i <= 100:
        med_count += 1
    else:
        large_count += 1





#clarify expense ranges

if i <= 25:
    print("Small expense")
elif i >= 25 and i <= 100 :
    print("Medium expense")
elif i >100:
    print("Large expense")

#compiling results before print
total_count=len(expenses)
total=sum(expenses)
average=total/total_count
mini=min(expenses)
maxi=max(expenses)

#Printing results:
print("RESULT SHEET: ")
print(f"Total number of expenses: {total_count}")
print(f"Total expenses: ${total}")
print(f"Average expense: ${average}")
print(f"Smallest expense: ${mini}")
print(f"Largest expense: ${maxi}")
print(f"Number of small, medium, and large expenses: ")
print(f"Small expenses: {small_count}")
print(f"Medium expenses: {med_count}")
print(f"Large expenses: {large_count}")