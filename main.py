import tkinter as tk
from random import randint, choice


WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self):
        self.R = randint(20, 30)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx = choice([dx for dx in range(-4, 5) if dx != 0])
        self.dy = choice([dy for dy in range(-4, 5) if dy != 0])
        self.ball = canvas.create_oval(self.x - self.R, 
                                       self.y - self.R,
                                       self.x + self.R,
                                       self.y + self.R,
                                       fill="green", outline="green")
        
        canvas.tag_bind(self.ball, "<Button-1>", self.click)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R < 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R < 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball, self.dx, self.dy)

    def click(self, event):
        canvas.itemconfig(self.ball, fill="red", outline="red")


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(10, tick)

def main():
    global root, canvas, balls

    root = tk.Tk()
    canvas = tk.Canvas(width=WIDTH, height=HEIGHT, bg="white")
    canvas.pack()
    balls = [Ball() for i in range(15)]
    tick()
    root.mainloop()

if __name__ == "__main__":
    main()
