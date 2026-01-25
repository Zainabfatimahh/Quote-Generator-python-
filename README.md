
# Random Quote Generator (Python)

A simple Python program that displays a random motivational quote every time it runs.  
Perfect for beginners learning Python and the `random` module.

## Features
- Generates a random quote on each run
- Easy to understand and modify
- Beginner-friendly Python code
- No external libraries required

## Requirements
- Python 3.x

## How to Run
1. Make sure Python is installed:
   ```bash
   python --version

2. Copy the code into a file named:

quote_generator.py


3. Run the program:

python quote_generator.py



Example Output

💬 Quote of the Day:
"Success is the sum of small efforts repeated daily."
- Robert Collier

Sample Code

import random

quotes = [
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("Success is the sum of small efforts repeated daily.", "Robert Collier"),
    ("Dream big and dare to fail.", "Norman Vaughan"),
    ("The future depends on what you do today.", "Mahatma Gandhi")
]

quote, author = random.choice(quotes)

print("💬 Quote of the Day")
print(f'"{quote}"')
print(f"- {author}")

Customization

Add more quotes to the quotes list

Remove authors if not needed

Display quotes in a loop or GUI


Future Improvements

GUI version using Tkinter

Web version using Flask or FastAPI

Fetch quotes from an API


Author

Made by Zainab 💻✨

