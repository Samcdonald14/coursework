
#Here is the opening statement for the chatbot this is a print command that details what the chatbot is and what the user should enter.
#I used a /n to make the rest of the string go to another line, this makes the formatting look nicer.
print ("Welcome to the Moodsense chatbot,\nThis application will advise you what steps to take depending on how you score your mood from 1-10.")
#here I created a variable  and asked the user for an input, the input wants their mood as a score from 1-10
#then I used conditional statements to dictate what response will be given to the user depending on what score they entered
#if the score is less than three it will give them advice
#if the score is between 4-7 it will accept the answer and give a recommendation, the elif statement is used below the if, it is used when the if statement is not true.
#I have used and to show a range of numbers this is telling the program that between to floats is the desired input to get that particular answer.
#the else statement then congratulates the user on any other number they input because the two other statement already dictated the other scores between 1-10
#I used a while loop in order to allow the user to try and enter another input if they choose a number that isn't between 0-100.
#The loop will continue until the user inputs a value that correlates with the rule that is dictated within the loop.
#Once the user inputs a correct value the loop will break and go on to the next stage of the program.
#The value error is used in order to ensure that the user inputs an integer and not letters for example.
#The value error exception is raised when the input cannot be interpreted as a float it is used in order to stop the user inputting strings or special characters.
while True:
    try:
        mood_score = float(input("Please enter your mood as a score from 1-10, we will then advise you what steps you should take!:"))
        if mood_score < 1 or mood_score > 10:
            print("You have entered an invalid integer. Please enter a value between 1 and 10.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a numeric value between 1 and 10.")

if mood_score < 4:
    print("Sorry you don't feel good, you should consider speaking to someone whether a friend, loved one, or therapist.")
elif mood_score >= 4 and mood_score <= 7:
    print("Your mood is okay, try to remember to look after yourself both physically and mentally.")
else:
    print("It's great to hear that you are feeling so good!!")
