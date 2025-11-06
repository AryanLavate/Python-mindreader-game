import tkinter as tk
import random

root = tk.Tk()
root.title("Magic Mind Reader")
root.geometry("450x330")
root.config(bg="black")

secret = 0
steps = []
current_step = 0

label = tk.Label(
    root,
    text="Welcome to the Magic Mind Reader!",
    fg="white",
    bg="black",
    font=("Arial", 14),
    wraplength=400,
    justify="center"
)
label.pack(pady=40)

next_button = tk.Button(
    root,
    text="Next",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=12,
    height=1
)
yes_button = tk.Button(
    root,
    text="Yes",
    font=("Arial", 12, "bold"),
    bg="#2196F3",
    fg="white",
    width=10,
    height=1
)
no_button = tk.Button(
    root,
    text="No",
    font=("Arial", 12, "bold"),
    bg="#f44336",
    fg="white",
    width=10,
    height=1
)
restart_button = tk.Button(
    root,
    text="Play Again",
    font=("Arial", 12, "bold"),
    bg="#FFC107",
    fg="black",
    width=12,
    height=1
)

def setup_game():
    global secret, steps, current_step
     
    secret = random.choice([i for i in range(2, 21, 2)])
    current_step = 0
    steps = [
        "Think of any number in your mind... but don't tell me!",
        "Multiply your number by 2.",
        f"Add {secret} to it.",
        "Divide the result by 2.",
        "Subtract the number you first thought of.",
        "Let me read your mind...",
        f"The answer in your mind is {secret // 2}",
        "Did I guess it right?"
    ]
    label.config(text="Welcome to the Magic Mind Reader!")
    next_button.pack(pady=20)
    yes_button.pack_forget()
    no_button.pack_forget()
    restart_button.pack_forget()

def next_step():
    global current_step
    if current_step < len(steps):
        label.config(text=steps[current_step])
        current_step += 1
        if current_step == len(steps):
            next_button.pack_forget()
            yes_button.pack(side="left", padx=40, pady=20)
            no_button.pack(side="right", padx=40, pady=20)

def user_said_yes():
    label.config(text="Haha! I knew it! I'm a real mind reader!")
    yes_button.pack_forget()
    no_button.pack_forget()
    restart_button.pack(pady=20)

def user_said_no():
    label.config(text="Oh no! You are bad at maths")
    yes_button.pack_forget()
    no_button.pack_forget()
    restart_button.pack(pady=20)

def restart_game():
    restart_button.pack_forget()
    setup_game()

next_button.config(command=next_step)
yes_button.config(command=user_said_yes)
no_button.config(command=user_said_no)
restart_button.config(command=restart_game)

setup_game()

root.mainloop()
