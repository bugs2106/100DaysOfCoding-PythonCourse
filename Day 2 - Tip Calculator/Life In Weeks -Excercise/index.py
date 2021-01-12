age = input("What is your current age? ")
till_year = input("Enter the age till where you want to calculate your days, weeks and months.")

#Write your code below this line 👇
age_int = int(age);
till_year_int = int(till_year);

years_remaining = till_year_int - age_int;
days_remaining = years_remaining * 365;
weeks_remaining = years_remaining * 52;
months_remaining = years_remaining * 12;
print(f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left.")







