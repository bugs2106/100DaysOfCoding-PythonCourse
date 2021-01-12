#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the Tip Calculator!");
total_bill = input("What was the total bill? ₹");
tip = input("What percentage tip would you like to give? 10, 12, 0r 15? ");
total_ppl = input("How many people to split the bill? ");

total_bill = float(total_bill);
tip = int(tip);
total_ppl = int(total_ppl);

tip_percent = tip / 100;

tip_totalbill = tip_percent * total_bill + total_bill;

final_bill = round(tip_totalbill / total_ppl, 2);


print(f"Each person should pay: ₹{final_bill}");






