import tkinter as tk
import random

# --- Window Setup ---
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#f5f5f5")  # Soft pastel background

# --- Variables ---
choices = ["Rock", "Paper", "Scissors"]
emoji_map = {"Rock": "✊", "Paper": "✋", "Scissors": "✌️"}
score = {"Player": 0, "Computer": 0, "Draws": 0}

# --- Functions ---
def play(player_choice):
    computer_choice = random.choice(choices)
    
    if player_choice == computer_choice:
        result = "It's a Draw!"
        score["Draws"] += 1
        result_color = "#FFA500"  # Orange
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        score["Player"] += 1
        result_color = "#32CD32"  # Lime Green
    else:
        result = "Computer Wins!"
        score["Computer"] += 1
        result_color = "#FF4500"  # Red

    # Update display
    player_label.config(text=emoji_map[player_choice])
    computer_label.config(text=emoji_map[computer_choice])
    result_label.config(text=result, fg=result_color)
    score_label.config(text=f"Player: {score['Player']}  Computer: {score['Computer']}  Draws: {score['Draws']}")

def reset_game():
    score["Player"] = score["Computer"] = score["Draws"] = 0
    player_label.config(text="?")
    computer_label.config(text="?")
    result_label.config(text="", fg="#000")
    score_label.config(text="Player: 0  Computer: 0  Draws: 0")

# --- UI Elements ---
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Comic Sans MS", 28, "bold"), bg="#f5f5f5", fg="#4B0082")
title_label.pack(pady=20)

# Display frame
display_frame = tk.Frame(root, bg="#f5f5f5")
display_frame.pack(pady=20)

player_frame = tk.Frame(display_frame, bg="#dcdcff", bd=2, relief="ridge", padx=20, pady=20)
player_frame.pack(side="left", padx=30)
player_label = tk.Label(player_frame, text="?", font=("Arial", 50))
player_label.pack()
tk.Label(player_frame, text="You", font=("Arial", 14)).pack(pady=5)

computer_frame = tk.Frame(display_frame, bg="#dcdcff", bd=2, relief="ridge", padx=20, pady=20)
computer_frame.pack(side="right", padx=30)
computer_label = tk.Label(computer_frame, text="?", font=("Arial", 50))
computer_label.pack()
tk.Label(computer_frame, text="Computer", font=("Arial", 14)).pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 22, "bold"), bg="#f5f5f5")
result_label.pack(pady=20)

# Scoreboard
score_label = tk.Label(root, text="Player: 0  Computer: 0  Draws: 0", font=("Arial", 16, "italic"), bg="#f5f5f5")
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=30)

def create_button(emoji, choice):
    btn = tk.Button(button_frame, text=emoji, font=("Arial", 40), width=4, height=2, bg="#e6e6fa", fg="#4B0082",
                    activebackground="#cdb5ff", activeforeground="#4B0082",
                    relief="raised", bd=5, command=lambda: play(choice))
    btn.pack(side="left", padx=20)
    return btn

buttons = [create_button(emoji_map[c], c) for c in choices]

# Reset button
reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 16, "bold"), bg="#ffb6c1", fg="#800000",
                      activebackground="#ff69b4", activeforeground="#fff",
                      relief="raised", bd=4, command=reset_game)
reset_btn.pack(pady=20)

# --- Run GUI ---
root.mainloop()
