#a leap year on Mars is divisible by 10 or is an odd year

year="" #set initial value for year variable

while year!="exit":
    year= input("Enter a year or type exit:")
    if year.isnumeric():
                year= int(year)
                if year%10==0:
                    print(year, "is a leap year on Mars.")
                    print(year," is divisible by 10.")
                else:
                    if year%2==0:
                          print(year,"is not a leap year on Mars.")
                          print(year,"is an even number.")
                    else:
                          print(year,"is a leap year on Mars.")
                          print(year,"is an odd number.")
    else:
        if year.lower()=="exit":
            year= year.lower()
            print("Goodbye")
        else:print("I don't understand. Please try again.\n")
                                
                                
                        
                            
