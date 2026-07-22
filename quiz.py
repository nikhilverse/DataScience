def quiz():
    questions = [
        {"question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "paris"
        },
        {"question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
        },
        {"question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "pacific ocean"
        },
        {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"],
        "answer": "harper lee"  
        },
        {
        "question": "What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "Fe", "Pb"],
        "answer": "au"
        }
    ]
    #enumerate works as a counter for the questions, so we can display the question number to the user
    for index,q in enumerate(questions):
        print(f"Question {index+1}: {q['question']}")
        for i, option in enumerate(q['options']):
            print(f"{i+1}. {option}")

        user_answer = input("Your answer (type the option number): ")

        if user_answer.isdigit() and 1 <= int(user_answer) <= len(q['options']):
            selected_option = q['options'][int(user_answer) - 1].lower()
            if selected_option == q['answer']:
                print("Correct!\n")
            else:
                print(f"Incorrect! The correct answer is: {q['answer'].capitalize()}\n")
quiz()