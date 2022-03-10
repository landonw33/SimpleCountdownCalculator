import datetime

# date formate day.month.year so 26.03.2022 is March, 26th, 2022
user_input = input("Enter your goal with a deadline separated by a colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
# How many days from now to deadline?
time_remaining = deadline_date - today_date

print(f"You have {time_remaining.days} days until {goal}" )

