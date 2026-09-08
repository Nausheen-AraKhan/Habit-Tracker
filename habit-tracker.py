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
   



