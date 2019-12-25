import tkinter as tk
from random import randint


WIDTH = 800
HEIGHT = 600


class Ball:
    pass


def main():
    global root, canvas

    root = tk.Tk()
    canvas = tk.Canvas(width=WIDTH, height=HEIGHT, bg="white")
    canvas.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
