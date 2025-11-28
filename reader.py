import tkinter as tk
from tkinter import filedialog

def choose_file(event=None):
	filename = filedialog.askopenfilename()
	entry.delete(0,tk.END)
	print('Selected: ', filename)
	f = open(filename, 'rb')
	byte = f.read(1)
	file_string = ''
	while byte:
		print(f'{ord(byte):02x}', end=' ')
		file_string = file_string + f'{ord(byte):02x}'
		byte = f.read(1)
	entry.insert(0,file_string)

root = tk.Tk()

root.title("Binary reader")
root.geometry("800x600")

button = tk.Button(root, text='Open', command=choose_file)
button.place(x=50, y=20)
#button.pack()

#tk.Entry(justify='center').pack()
entry = tk.Entry()
entry.place(x=50,y=50, width=700, height=500)


root.mainloop()