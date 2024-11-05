from tkinter import *

if __name__ == "__main__":

    window = Tk()
    window.title("Snake game")
    window.resizable(False,False)

    #display score
    label = Label(window, text = 'Score: ...')
    label.pack()

    #build canvas / game field
    canvas = Canvas(window, bg = "#000000", height = 1000, width = 1000)
    canvas.pack()

    window.update()

    canvas.create_oval(50,50,50 + 25,50+25,fill = "#00FF00")

    window.after()

    window.mainloop()

