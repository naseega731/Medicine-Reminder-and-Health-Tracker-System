from tkinter import *

root = Tk()
root.title("Dashboard")
root.geometry("500x400")

Label(root, text="Medicine Reminder and Health Tracker",
      font=("Arial", 14, "bold")).pack(pady=20)

Button(root, text="Medicine Management").pack(pady=10)
Button(root, text="Reminder Management").pack(pady=10)
Button(root, text="Health Tracker").pack(pady=10)
Button(root, text="Reports").pack(pady=10)

root.mainloop()
