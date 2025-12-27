import tkinter as tk
from tkinter import messagebox
import requests

def get_random_word():
    try:
        r = requests.get("https://random-word-api.herokuapp.com/word")
        return r.json()[0].lower()
    except Exception as e:
        return "error"

guessed_letters = []
tries = 6
word_to_guess = get_random_word()

def update_word_display():
    display = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    word_label.config(text=display)

def guess_letter():
    global tries
    letter = entry.get().lower()
    entry.delete(0, tk.END)
    if not letter or len(letter) != 1 or not letter.isalpha():
        messagebox.showwarning("Invalid Input", "Enter a single letter.")
        return
    if letter in guessed_letters:
        messagebox.showinfo("Already Guessed", "You already guessed that letter.")
        return
    guessed_letters.append(letter)
    if letter not in word_to_guess:
        tries -= 1
        tries_label.config(text=f"Tries left: {tries}")
    update_word_display()
    check_game_over()

def check_game_over():
    if all(letter in guessed_letters for letter in word_to_guess):
        messagebox.showinfo("You Win!", f"You guessed the word: {word_to_guess}")
        root.destroy()
    if tries == 0:
        messagebox.showerror("Game Over", f"You lost! The word was: {word_to_guess}")
        root.destroy()

root = tk.Tk()
root.title("Hangman")
root.geometry("350x300")

title_label = tk.Label(root, text="Hangman", font=("Arial", 18))
title_label.pack(pady=10)

word_label = tk.Label(root, text="", font=("Arial", 16))
word_label.pack(pady=10)

tries_label = tk.Label(root, text=f"Tries left: {tries}", font=("Arial", 12))
tries_label.pack()

entry = tk.Entry(root, font=("Arial", 14), width=5, justify="center")
entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack()

update_word_display()

root.mainloop()
