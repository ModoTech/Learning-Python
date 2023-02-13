import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, bg='red', text='Stop', width=125, command=r.destroy)
button.pack()
r.mainloop()