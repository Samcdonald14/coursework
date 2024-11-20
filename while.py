
while True:
    try:
        mood_score = float(
            input("Please enter your mood as a score from 1-10, we will then advise you what steps you should take!:"))
        if mood_score < 1 or mood_score > 10:
            print("You have entered an invalid integer Please enter a value between 1 and 10.")
        else:
            break  # Exit the loop if the input is valid
    except ValueError:

        memory_usage = float(input("Please enter your memory usage (GB) as an integer:"))
        if memory_usage < 0 or memory_usage > 64: