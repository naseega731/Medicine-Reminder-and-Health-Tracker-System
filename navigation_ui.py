from tkinter import *

root = Tk()
root.title("Navigation Menu")
root.geometry("400x300")

Button(root, text="Dashboard").pack(pady=5)
Button(root, text="Medicine Management").pack(pady=5)
Button(root, text="Reminder Management").pack(pady=5)
Button(root, text="Health Tracker").pack(pady=5)
Button(root, text="Reports").pack(pady=5)

root.mainloop()
