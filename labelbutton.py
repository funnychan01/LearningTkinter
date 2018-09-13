import tkinter as tk

window = tk.Tk()
window.title("My Second Window")
window.geometry("300x200")
var = tk.StringVar()

l = tk.Label(window, textvariable = var, bg = "pink", font = ("Arial", 10), width = 20, height = 2)
l.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("I Love You!")
    else:
        on_hit = False
        var.set("")

b = tk.Button(window, text = "Hit Me!", width = 20, height = 2, command = hit_me)
b.pack()

window.mainloop()
