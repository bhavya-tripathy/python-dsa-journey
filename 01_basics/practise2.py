#seconds to minutes conversion
seconds = int(input("Enter seconds: "))
minutes = seconds / 60
print(f"{seconds} seconds is equal to {minutes} minutes.")

#miles to kilometers conversion
miles = float(input("Enter miles: "))
kilometers = miles * 1.60934
print(f"{miles} miles is equal to {kilometers} kilometers.")

#kilometrs to miles conversion
kilometers = float(input("Enter kilometers: "))
miles = kilometers / 1.60934
print(f"{kilometers} kilometers is equal to {miles} miles.")

#if you run a 10 killometr race in 42 minutes 42 seconds, what is your avergae pace? what is yoyur average speed in miles per hour?
total_seconds = 42 * 60 + 42
total_kilometers = 10
pace_seconds_per_km = total_seconds / total_kilometers
pace_minutes = int(pace_seconds_per_km / 60)
pace_seconds = int(pace_seconds_per_km % 60)
speed_mph = (total_kilometers / 1.60934) / (total_seconds / 3600)
print(f"Average pace: {pace_minutes} minutes {pace_seconds} seconds per kilometer")
print(f"Average speed: {speed_mph:.2f} miles per hour")

name = input("what is your name:")
print ("hello "  + name)  #concatenation


first = input("Enter first number: ")
second = input("Enter second number: ")
sum = float(first) + float(second)
print("the sum is:" + str(sum))