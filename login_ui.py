from tkinter import *

root = Tk()
root.title("Login")
root.geometry("400x300")

Label(root, text="Username").pack(pady=10)
Entry(root).pack()

Label(root, text="Password").pack(pady=10)
Entry(root, show="*").pack()

Button(root, text="Login").pack(pady=20)

root.mainloop()
