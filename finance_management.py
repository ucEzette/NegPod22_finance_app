def welcome_message():
    message = (
        "Welcome to Financial Management App 💰💵\n"
        "This Financial Literacy Management App is an educational platform that equips people with essential "
        "financial skills through interactive content, quizzes, and exercises on budgeting, saving, and investing.\n"
        "It also connects users with new business and investment opportunities, promoting informed decision-making "
        "and fostering financial growth.\n"
        "The app empowers users to manage their finances responsibly and explore career or entrepreneurial paths.\n"
        "Fill in the following simple steps and get knowledge on how to manage your finances properly ✅\n"
        "No more wasting money, we got you!!"
    )
    return message
welcome_text = welcome_message()
print(welcome_text)


def interactive_steps():
    name = input("What is your name? ")
    greeting = (
        f"Hello, {name}! Let's get started with learning how to manage your finances better."
    )
    print(greeting)
    action = input("Would you like to take a quiz on budgeting? (yes/no) ").lower()
    if action == 'yes':
        response = (
            "Great! Let's begin with budgeting tips and a quiz to test your knowledge."
        )
    elif action == 'no':
        response = (
            "No worries! You can always come back later to explore budgeting tips."
        )
    else:
        response = "Invalid input. Please enter 'yes' or 'no'."
    print(response)
    
    return greeting, response

# Using the functions without directly printing in the function
welcome_text = welcome_message()
greeting, quiz_response = interactive_steps()

# Displaying the results
# These lines will ultimately display the output if executed in a script or console
welcome_text, greeting, quiz_response