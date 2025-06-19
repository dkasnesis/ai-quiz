# AI Quiz Game

A simple Python-based yes/no quiz game that uses OpenAI's API to generate questions dynamically based on a user-selected category. Designed for students up to 18 years old, the game tracks scores and allows users to restart for a new quiz session.

## Features
- Generates unique yes/no questions using OpenAI's GPT-3.5-turbo model.
- Supports custom quiz categories chosen by the user.
- Keeps track of the user's score (1 point per correct answer).
- Includes a default question as a fallback in case of API issues.
- Option to restart the quiz for a new session.
- Simple command-line interface.

## Requirements
- Python 3.x
- OpenAI Python library (`openai`)
- An OpenAI API key (replace `"insert-api-key-here"` in the code with your actual key)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-quiz-game.git
   cd ai-quiz-game
   ```
2. Install the required Python library:
   ```bash
   pip install openai
   ```
3. Set up your OpenAI API key:
   - Replace `"insert-api-key-here"` in the script with your actual OpenAI API key. You can obtain a key from [OpenAI's platform](https://platform.openai.com/).

## Usage
1. Run the script:
   ```bash
   python quiz.py
   ```
2. Follow the prompts:
   - Enter a quiz category (e.g., "science", "history", "geography").
   - Answer each question with "yes" or "no".
   - After answering 5 questions, view your score.
   - Choose to play again or exit.

## Example
```
Welcome to my AI Quiz!
Let's Play!
Choose category: science
Question: Is the sun a star?
Answer (yes/no): yes
Correct!
...
You answered 4/5 questions correctly!
Do you want to play again? (yes/no): no
Thanks for playing!
```

## Code Structure
- `generate_questions()`: Calls OpenAI's API to create a unique yes/no question and answer pair.
- `start_quiz()`: Manages the quiz flow, including category selection, question display, and scoring.
- `restart()`: Resets the quiz state for a new session.
- Main script: Initializes the quiz and handles user interaction.

## Notes
- The script generates 5 questions per quiz session.
- Questions are stored in a set to ensure uniqueness within a session.
- The OpenAI API key must be valid and have sufficient credits to generate questions.
- The default question ("Is this a default question? | Answer: yes") is used if the API fails to generate a question after 10 attempts.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact
For questions or feedback, feel free to open an issue on the GitHub repository.