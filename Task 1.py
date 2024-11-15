

#Here I have printed the welcome message to the program using the print command,
#these are strings that let the user know what the use of the bot is.
print ("Hello, Welcome to the TechComp system health monitoring bot!")
print ("We will first check your CPU utilisation")

#Here i create a variable for the cpu health, this allows the program to know what is being enetered into it
#this also allows us to gain an input from the user and to rpint out the status message

cpu_health = float(input("Please enter your CPU usage as a percentage (%):"))

#here i have inserted a conditional statement, this is a rule that states a certain output for a certain condition
#first I used an if statement to dictate the amount for the cpu being underutilised
#Then because i used an if previously i used an elif statement to dictate what the other outcome would be if the input did not meet the requirements of the if statement.
#I have used and to show a range of numbers this is telling the program that between to floats is the desired input to get that particular answer.
#I then use an else statement in order to dictate that anything outside of the if or elif will give a certain result
if cpu_health <40:
    print ("Your CPU is underutilised!")
elif cpu_health >=40 and cpu_health <=75:
    print ("your CPU is overloaded, try and close some processes in task manager, or run a scan.")
else:
    print ("Your CPU is being utilised optimally!")

#here i have inserted a conditional statement, this is a rule that states a certain output for a certain condition
#first I used an if statement to dictate the amount for the RAM being underutilised
#Then because i used an if previously i used an elif statement to dictate what the other outcome would be if the input di not meet the requirements of the if statement.
#I have used and to show a range of numbers this is telling the program that between to floats is the desired input to get that particular answer.
#I then use an else statement in order to dictate that anything outside of the if or elif will give a certain result
print ("Now we will check your memory usage (RAM)")
memory_usage = float(input("Please enter your memory usage in GB (Gigabytes):"))
if memory_usage <4:
    print ("Your RAM is being underutilised.")
elif memory_usage >= 4 and memory_usage <=8:
    print ("Your RAM is overloaded, please consider closing processes, tabs or programs on your computer.")
else:
    print("Your RAM is being optimally utilised.")
#Here i print out the cosing message for the program using the print command
print("These are the results of your computer health check")
print(f"Thank you for using the TechComp computer monitoring bot.")


