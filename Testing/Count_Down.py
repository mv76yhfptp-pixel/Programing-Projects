import tkinter as tk 

root = tk.Tk()
root.title("CountDown Timer")
root.geometry("300x200")

def countdown(time_left):
    if time_left > 0:
        label.config(text=f"Time left: {time_left}")
        root.after(1000, countdown, time_left - 1)
    else:
        label.config(text="Time's up!")

def start_timer():
    time_left = int(entry.get())
    countdown(time_left)

label = tk.Label(root, text="Example", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

button = tk.Button(root, text="Start", command=start_timer)
button.pack(pady=10)



root.mainloop()