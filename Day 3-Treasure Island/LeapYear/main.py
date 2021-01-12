year = int(input("Which year do you want to check? "));

if(1000 <= year < 10000):
 if(year % 4 == 0):
   if(year % 100 == 0):
     if(year % 400 == 0):
       print("It is a Leap Year.");
     else:
      print("Not a Leap Year");
   else:
    print("It is a Leap Year");
 else:
  print("Not a Leap Year.");
else:
  print("Not a valid input.");
