import json
import os
from datetime import date
if os.path.exists("habits.json"):
    with open("habits.json", "r") as f:
        old_data=json.load(f)
else:
    old_data={}
no_of_habits=int(input("How many habits do you want to track:\n"))
habits=[]
for i in range(no_of_habits):
    habit=input("Enter your habit: \n")
    habits.append(habit)
completed=0
status={}
for habit in habits:
    ans=input(f"Did you complete {habit} today? (y/n) \n")
    if ans=="y":
        completed+=1
        status[habit]=True
    else:
        status[habit]=False
percentage=(completed/no_of_habits)*100
print("\n")
print("*************TODAY'S SUMMARY************")
print("\n")
for habit, done in status.items():
    if done:
        print(f"{habit}: ✅")
    else:
        print(f"{habit}: ❌")
print(f"Habits Completion {percentage:.2f}%!")
today=str(date.today())
old_data[today]=status
with open("habits.json", "w") as f:
    json.dump(old_data, f, indent=4)
print("\nYour data has been stored Succesfully!\n")
print("\n========HABIT HISTORY========\n")
for saved_data, status in old_data.items():
   print((f"\n📅 {saved_data}"))
   for habit, done in status.items():
       if done:
           print(f"{habit}: ✅ Completed")
       else:
           print(f"{habit}: ❌ Not Completed")

   



