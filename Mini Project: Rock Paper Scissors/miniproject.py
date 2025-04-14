import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Choices
choices = ['rock', 'paper', 'scissors']

# Rules dictionary: what each item beats
rules = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

# Game history storage
history = []

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors or quit): ").lower()
      if choice in choices or choice == 'quit':
            return choice
        else:
            print("Invalid input. Try again.")

def get_computer_choice():
    return np.random.choice(choices)

def decide_winner(user, computer):
    if user == computer:
        return 'draw'
    elif rules[user] == computer:
        return 'win'
    else:
        return 'lose'

def play_game():
    print("\n--- Rock, Paper, Scissors Game ---")
    print("Type 'quit' to end the game.\n")

    while True:
        user = get_user_choice()
        if user == 'quit':
            break
        computer = get_computer_choice()
        result = decide_winner(user, computer)
        print(f"Computer chose: {computer} → You {result.upper()}!")

        # Log result
        history.append({
            'User': user,
            'Computer': computer,
            'Result': result
        })

    print("\nGame Over.")
    if history:
        show_summary()

def show_summary():
    df = pd.DataFrame(history)
    print("\nGame Summary:")
    print(df)

    result_counts = df['Result'].value_counts()

    # Plot the results
    sns.set(style='whitegrid')
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='Result', palette='pastel', order=['win', 'lose', 'draw'])
    plt.title('Game Result Summary')
    plt.ylabel('Count')
    plt.xlabel('Result')
    plt.show()

    print("\nTotal Games:", len(df))
    print("Wins:", result_counts.get('win', 0))
    print("Losses:", result_counts.get('lose', 0))
    print("Draws:", result_counts.get('draw', 0))

if _name_ == '_main_':
    play_game()
