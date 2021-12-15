from tkinter import *
from gui import Gui
from mw_zero_sum import Mw_zero_sum
import numpy as np

class Gui_3D(Gui):
    def __init__(self, game):
        super().__init__(game)

    def draw_triangle(self):
        self.canvas.create_polygon(points, fill="white")

    def draw_outline(self):
        points = [250,50 , 50,450 , 450,450]
        self.canvas.create_polygon(points, fill="white")
    
    def map_coords(self, strat):
        return (strat[0]*300+100 , strat[1]*300+100)

    def plot_points(self):
        self.create_circle(self.map_coords(self.game.x_strats[self.i]), 5, True)
        self.create_circle(self.map_coords(self.game.y_strats[self.i]), 5, False)

if __name__ == "__main__":
    rock_papper_sissors = np.array([[0, 1, -1], [-1, 0, 1], [1, -1, 0]])
    eta = 0.1
    init_strategy_x = np.array([0.0, 1.0, 0.0])
    init_strategy_y = np.array([1.0, 0.0, 0.0])
    game = Mw_zero_sum(rock_papper_sissors, eta, init_strategy_x, init_strategy_y)

    print(game.x_strats)
    print(game.y_strats)

    Gui_3D(game)