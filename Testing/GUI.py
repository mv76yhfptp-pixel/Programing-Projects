import tkinter as tk
from tkinter import messagebox

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GUI")
        self.root.geometry("500x500")

        self.label = tk.Label(self.root, text="Welcome to my GUI", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.closing)

        self.root.mainloop()

    def closing(self):

        if messagebox.askyesno(title="Quit?", message="Do you want to close the program?"):         
            self.root.destroy()


GUI()