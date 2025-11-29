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
		if newchar == 7:
			file_string = file_string + '  '
		if newchar == 15:
			file_string = file_string + '   ' + ascii_string + '\n  '
			ascii_string = '' 
			newchar = 0
	file_string = file_string + (50-3*newchar-int(newchar/7)*2+int(newchar/14)*2)*' ' + ascii_string + '\n'
	text.insert("1.0",file_string)

root = tk.Tk()

root.title("Binary reader")
root.geometry("800x600")

button = tk.Button(root, text='Open', command=choose_file)
button.place(x=50, y=20)

text = tk.Text()
text.place(x=50,y=50, width=700, height=500)

root.mainloop()  