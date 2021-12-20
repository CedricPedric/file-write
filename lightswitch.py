import tkinter as tk
window = tk.Tk()

button = tk.Button(text='knop', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
BooleanVar = True

def hello(event):
    global BooleanVar
    if BooleanVar:
        window["background"] = 'yellow'
        BooleanVar = False
    else:
        window["background"] = "white"
        BooleanVar = True
    

button.bind('<Button-1>', hello)
# schijf hier tussen je code

window.mainloop()