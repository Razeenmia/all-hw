# Function to ask a question and check the answer
def ask_question(question, correct_answer, options=None):
    print(question)
    
    # If there are options, display them
    if options:
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
    
    # Get the user's answer
    answer = input("Your answer: ").strip().lower()
    
    # If options are provided, check the answer against the option number
    if options:
        try:
            answer_index = int(answer) - 1
            if options[answer_index].lower() == correct_answer.lower():
                return True
            else:
                return False
        except ValueError:
            return False
    # If no options, check the direct answer
    elif answer == correct_answer.lower():
        return True
    else:
        return False

# Function to run the quiz
def run_quiz():
    print("Welcome to the Quiz!\n")
    
    # List of questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "correct_answer": "paris",
            "options": ["Berlin", "Madrid", "Paris", "Rome"]
        },
        {
            "question": "What is the largest planet in our solar system?",
            "correct_answer": "jupiter",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"]
        },
        {
            "question": "Which programming language is known as the language of the web?",
            "correct_answer": "javascript",
            "options": ["Java", "Python", "C++", "JavaScript"]
        },
        {
            "question": "What is the chemical symbol for water?",
            "correct_answer": "h2o",
            "options": ["O2", "H2O", "CO2", "N2"]
        }
    ]
    
    score = 0  # Variable to keep track of the score
    
    # Loop through each question in the list
    for i, question_data in enumerate(questions, 1):
        print(f"Question {i}:")
        question = question_data["question"]
        correct_answer = question_data["correct_answer"]
        options = question_data["options"]
        
        # Ask the question and check the answer
        if ask_question(question, correct_answer, options):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer.capitalize()}.\n")
    
    # Print the final score
    print(f"Quiz finished! You scored {score} out of {len(questions)}.")

# Start the quiz
run_quiz()
