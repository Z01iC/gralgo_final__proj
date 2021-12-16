from tkinter import *
from abc import ABC, abstractmethod
import mw_game
from consts import *
import time

class Gui(ABC):
    def __init__(self, game, three_dimensional=False):
        self.master: Tk = Tk()
        self.canvas = Canvas(self.master, width=600, height=600)
        self.canvas.pack()
        self.game: mw_game.Mw_game = game
        self.i = 0
        self.draw_outline()
        self.player_1_dots = []
        self.player_2_dots = []
        self.prev_player_1_average = []
        self.prev_player_2_average = []
    
        self.main_loop()
        self.master.mainloop()

    def re_color_dots(self, player, colors, average=False):
        if not average:
            dots = self.player_1_dots if player else self.player_2_dots
        else:
            dots = self.prev_player_1_average if player else self.prev_player_2_average
        tail_len = min(len(dots), len(colors))
        for color, dot in zip(colors, dots[-tail_len:]):
            fill = color if average else self.get_color(color, player)
            self.canvas.itemconfig(dot, fill=fill)

    def get_color(self, code, player):
        if player:
            return "#" + code + "0000"
        else:
            return "#0000" + code

    def create_circle(self, coords, r=POINT_RADIUS, player=True, colors=COLORS, average=False): #center coordinates, radius
        x0 = coords[0] - r
        y0 = coords[1] - r
        x1 = coords[0] + r
        y1 = coords[1] + r
        if average:
            if player:
                self.re_color_dots(player, COLORS_3D_P1_AVG, average)
                self.prev_player_1_average.append(self.canvas.create_oval(x0, y0, x1, y1, fill="#FF17D8", outline=""))
            else:
                self.re_color_dots(player, COLORS_3D_P2_AVG, average)
                self.prev_player_2_average.append(self.canvas.create_oval(x0, y0, x1, y1, fill="#1AFED1", outline=""))

        else:
            self.re_color_dots(player, colors)
            fill = self.get_color(NEW_COLOR, player)
            if player: 
                self.player_1_dots.append(self.canvas.create_oval(x0, y0, x1, y1, fill=fill, outline=""))
            else:
                self.player_2_dots.append(self.canvas.create_oval(x0, y0, x1, y1, fill=fill, outline=""))

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
            
