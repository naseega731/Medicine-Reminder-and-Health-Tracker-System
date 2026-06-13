from tkinter import *

root = Tk()
root.title("Medicine Form")
root.geometry("400x350")

Label(root, text="Medicine Name").pack()
Entry(root).pack()

Label(root, text="Dosage").pack()
Entry(root).pack()

Label(root, text="Date").pack()
Entry(root).pack()

Label(root, text="Time").pack()
Entry(root).pack()

Button(root, text="Submit").pack(pady=20)

root.mainloop()
