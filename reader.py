import tkinter as tk
from tkinter import filedialog

def choose_file(event=None):
	filename = filedialog.askopenfilename()
	text.delete('1.0',tk.END)
	print('Selected: ', filename)
	f = open(filename, 'rb')
	byte = f.read(1)
	file_string = '  '
	ascii_string = ''
	newchar = 0
	while byte:
		file_string = file_string + f'{ord(byte):02x} '
		if ord(byte)>32 and ord(byte)<126:
			ascii_string = ascii_string + chr(ord(byte))
		else:
			ascii_string = ascii_string + '.'
		byte = f.read(1)
		newchar += 1
		if newchar == 8:
			file_string = file_string + '  '
		if newchar == 16:
			file_string = file_string + '   ' + ascii_string + '\n  '
			ascii_string = '' 
			newchar = 0
	file_string = file_string + (53-3*newchar-int(newchar/8)*2+int(newchar/16)*2)*' ' + ascii_string + '\n'
	text.insert("1.0",file_string)

root = tk.Tk()

root.title("Binary reader")
root.geometry("800x600")

button = tk.Button(root, text='Open', command=choose_file)
button.place(x=50, y=20)

scroll = tk.Scrollbar(root)
scroll.place(x=750, y=50, height=500)

text = tk.Text(root, yscrollcommand = scroll.set)
text.place(x=50,y=50, width=700, height=500)

scroll.config(command = text.yview)

root.mainloop()