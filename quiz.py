import openai

questions = [] # ftiaxnw keni lista gia tis erwtiseis
current_question = 0
score = 0
asked_questions = set()

openai.api_key = "insert-api-key-here"

# Question: Is the sky blue? | Answer: yes
def generate_questions():
    for i in range(10):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = [
                {"role": "system",
                 "content": "Generate a simple yes/no question in English about" + quiz_type + ", "
                 "suitable for students up to 18 years old, with a clear correct answer. Return the format: "
                 "'Question: <question> | Answer: <yes/no>'. Ensure the question is unique and not in: " + ", ".join(
                     asked_questions) + "."},
                {"role": "user", "content": "Generate a simple yes/no question."}
            ]
        )

        result = response.choices[0].message["content"].strip() # Question: Is the sky blue? | Answer: yes
        question, answer = result.split(" | ")
        question = question.replace("Question: ", "") # Is the sky blue?
        answer = answer.replace("Answer: ", "").rstrip(".").lower() # yes
        if question not in asked_questions:
            asked_questions.add(question)
            return question, answer
    return "Is this a default question?","yes" # an to chatgpt kollisei, tha mou epistrepsei auti tin erotisi


def start_quiz():
    global current_question, score, quiz_type

    quiz_type = input("Choose category: ")

    for i in range(5):
        questions.append(generate_questions())

    while current_question < len(questions): # einai to megethos tis listas questions
        question, correct_answer = questions[current_question]
        print("Question: ", question)
        current_question += 1
        user_answer = input("Answer (yes/no): ")
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print("You answered "+str(score)+"/"+str(len(questions))+" questions correctly!")
    restart_question = input("Do you want to play again? (yes/no)    ")
    if restart_question.lower() == "yes":
        restart()
    else:
        print("Thanks for playing!")


def restart():
    global current_question, score, questions
    current_question = 0
    score = 0
    questions = []
    start_quiz()


if __name__ == "__main__":
    print("Welcome to my AI Quiz!")
    print("Let's Play!")
    start_quiz()