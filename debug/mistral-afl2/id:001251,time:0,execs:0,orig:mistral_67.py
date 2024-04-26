
# This variable is initialized with a False value
should_quit = False

while not should_quit:
    user_answer = input("Do you want to quit? (y/n): ")
    
    # Convert user answer to lowercase and check if it equals 'y'
    if user_answer.lower() == 'y':
        should_quit = True
        
# Program ends here
