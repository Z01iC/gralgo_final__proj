from tkinter import *
from abc import ABC, abstractmethod
import mw_game
from consts import *

class Gui(ABC):
    def __init__(self, game, three_dimensional=False):
        self.master: Tk = Tk()
        self.canvas = Canvas(self.master, width=600, height=600)
        self.canvas.pack()
        self.game: mw_game.Mw_game = game
        self.i = 0
        self.draw_outline()
        self.dots = []
        self.main_loop()
        self.master.mainloop()

    def re_color_dots(self):
        tail_len = min(len(self.dots), len(COLORS))
        for color, dot in zip(COLORS, self.dots[-tail_len:]):
            self.canvas.itemconfig(dot, fill=color)

    def create_circle(self, coords, r=POINT_RADIUS, player=True): #center coordinates, radius
        x0 = coords[0] - r
        y0 = coords[1] - r
        x1 = coords[0] + r
        y1 = coords[1] + r
        self.re_color_dots()
        self.dots.append(self.canvas.create_oval(x0, y0, x1, y1, fill=NEW_COLOR, outline=""))

    @abstractmethod
    def map_coords(self, strat):
        assert False, "map_coords not implemented"

    @abstractmethod
    def draw_outline(self):
        assert False, "draw_outline not implemented"

    @abstractmethod
    def plot_points(self):
        assert False, "plot_points not implemented"

    def main_loop(self):
        if self.i < self.game.num_iters:
            self.plot_points()
            self.i += 1
            self.canvas.after(int(1000 / FRAME_RATE), self.main_loop)
            
