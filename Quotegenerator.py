import random

quotes = [
    "Believe in yourself.",
    "Stay consistent, success will follow.",
    "Dream big and work hard.",
    "Small steps every day.",
    "You are capable of amazing things."
]

def generate_quote():
    return random.choice(quotes)

while True:
    print("\n1. Get a Quote")
    print("2. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        print("\n✨", generate_quote())
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
