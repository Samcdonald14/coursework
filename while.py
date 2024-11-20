
while True:
    try:
        memory_usage = float(input("Please enter your memory usage (GB) as an integer:"))
        if memory_usage < 0 or memory_usage > 64:
            print("You have entered an invalid percentage. Please enter a value between 0 and 100.")
        else:
            break  # Exit the loop if the input is valid
    except ValueError:

        memory_usage = float(input("Please enter your memory usage (GB) as an integer:"))
        if memory_usage < 0 or memory_usage > 64: