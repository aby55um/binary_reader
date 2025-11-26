import tkinter as tk
from tkinter import filedialog

def choose_file(event=None):
	filename = filedialog.askopenfilename()
	print('Selected: ', filename)
	f = open(filename)
	print(f.read())

root = tk.Tk()

root.title("Binary reader")
root.geometry("800x600")

button = tk.Button(root, text='Open', command=choose_file)
button.pack()

root.mainloop()