# step1: import tkinter
from tkinter import *

# step2: gui interaction
window = Tk()

# step3: adding inputs
window.title("Adarsh")  
window.geometry("500x500")

label1 = Label(window, text="Hello world",bg="lightblue",fg = "black")
label2 = Label(window, text="Welcome to HackerRank",bg="red",fg = "black")
label3 = Label(window, text="Enjoy coding!",bg="purple",fg = "black")
label1.pack(side = TOP,fill = X,expand = False)
label2.pack(side = LEFT,fill = Y,expand = False)
label3.pack(side = RIGHT,fill =Y,expand = False)

# step4: mainloop
window.mainloop()