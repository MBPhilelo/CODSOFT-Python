import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        # Create GUI components
        self.title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.instruction_label = tk.Label(root, text="Choose rock, paper, or scissors:")
        self.instruction_label.pack(pady=5)

        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        self.result_text = tk.Text(root, width=50, height=10)
        self.result_text.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=5)

        self.score_label = tk.Label(root, text=f"User: {self.user_score} - Computer: {self.computer_score}")
        self.score_label.pack(pady=5)

    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        result = self.determine_winner(user_choice, computer_choice)

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"You chose: {user_choice}\n")
        self.result_text.insert(tk.END, f"Computer chose: {computer_choice}\n")
        self.result_text.insert(tk.END, f"Result: {result}\n")

        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1

        self.update_score()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "You win!"
        else:
            return "You lose!"

    def update_score(self):
        self.score_label.config(text=f"User: {self.user_score} - Computer: {self.computer_score}")

    def reset_game(self):
        self.result_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
