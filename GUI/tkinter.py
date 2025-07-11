import tkinter as tk
window = tk.Tk()
window.title('COUNTING')
button = tk.Button(window, text='START', width=25, command=window.destroy)
button.pack()
window.mainloop()
