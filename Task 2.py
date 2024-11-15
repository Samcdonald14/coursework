
#Here is the opening statement for the chatbot this is a print command that details what the chatbot is and what the user should enter.
#I used a /n to make the rest of the string go to another line, this makes the formatting look nicer.
print ("Welcome to the Moodsense chatbot,\nThis application will advise you what steps to take depending on how you score your mood from 1-10.")
#here I created a variable  and asked the user for an input, the input wants their mood as a score from 1-10
#then I used conditional statements to dictate what response will be given to the user depending on what score they entered
#if the score is less than three it will give them advice
#if the score is between 4-7 it will accept the answer and give a recommendation, the elif statement is used below the if, it is used when the if statement is not true.
#I have used and to show a range of numbers this is telling the program that between to floats is the desired input to get that particular answer.
#the else statement then congratulates the user on any other number they input because the two other statement already dictated the other scores between 1-10
mood_score = float(input("Please enter your mood as a score from 1-10, we will then advise you what steps you should take!:"))
if mood_score<3:
    print ("Sorry you don't feel good, you should consider speaking to someone whether a friend, loved one or therapist.")
elif mood_score >= 3 and mood_score<=8:
    print ("Your mood is okay, try to remember to look after yourself both physically and mentally")
else:
    print ("Its great to hear that you are feeling so good!!")
