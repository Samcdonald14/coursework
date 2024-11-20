

#Here I have printed the welcome message to the program using the print command,
#These are strings that let the user know what the use of the bot is.
print ("Hello, Welcome to the TechComp system health monitoring bot!")
print ("We will first check your CPU utilisation")
#Here I create a variable for the CPU health, this allows the program to know what is being entered into it.
#This also allows us to gain an input from the user and to print out the status message.


cpu_health = float(input("Please enter your CPU usage percentage as an integer."))

#Here I have inserted a conditional statement, this is a rule that states a certain output for a certain condition
#First I used an if statement to dictate the amount for the CPU being underutilised
#Then because I used an if previously I used an elif statement to dictate what the other outcome would be if the input did not meet the requirements of the if statement.
#I have used and to show a range of numbers this is telling the program that between to floats is the desired input to get that particular answer.
#I then use an else statement in order to dictate that anything outside of the if or elif will give a certain result.
#I used a while loop in order to allow the user to try and enter another input if they choose a number that isn't between 0-100.
#The loop will continue until the user inputs a value that correlates with the rule that is dictated within the loop.
#Once the user inputs a correct value the loop will break and go on to the next stage of the program.
#The value error is used in order to ensure that the user inputs an integer and not letters for example.
#The value error exception is raised when the input cannot be interpreted as a float it is used in order to stop the user inputting strings or special characters.
while True:
    try:
        cpu_health = float(input("Please enter your CPU usage percentage as an integer (0-100): "))
        if cpu_health < 0 or cpu_health > 100:
            print("You have entered an invalid percentage. Please enter a value between 0 and 100.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a numeric value for CPU percentage.")
if cpu_health < 40:
        print("Your CPU is underutilised!")
elif cpu_health >=40 and cpu_health <=75:
    print("Your CPU is being utilised optimally!")
else:
    print("your CPU is overloaded, try and close some processes in task manager, or run a scan.")

#Here I have inserted a conditional statement, this is a rule that states a certain output for a certain condition.
#First I used an if statement to dictate the amount for the RAM being underutilised.
#Then because I used an if previously I used an elif statement to dictate what the other outcome would be if the input did not meet the requirements of the if statement.
#I have used and to show a range of numbers this is telling the program that between to floats is the desired input to get that particular answer.
#I then use an else statement in order to dictate that anything outside of the if or elif will give a certain result.

print("Now we will check your memory usage (RAM)")

while True:
    try:
        memory_usage = float(input("Please enter your memory usage (GB) as an integer:"))
        if memory_usage < 0 or memory_usage > 64:
            print("You have entered an invalid value. Please enter a value between 0 and 64.")
        else:
            break
    except ValueError:
        print("You have entered an invalid value, could you please try again with a value between 0 and 64.")

if memory_usage < 4:
    print("Your RAM is being underutilized.")
elif 4 <= memory_usage <= 8:
    print("Your RAM is being optimally utilized.")
else:
    print("Your RAM is overloaded, please consider closing processes, tabs, or programs on your computer.")


print("These are the results of your computer health check")
print(f"Thank you for using the TechComp computer monitoring bot.")
#These are the closing statements for the program after the checks have been completed.