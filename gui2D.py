from tkinter import *
from gui import Gui
from mw_zero_sum import Mw_zero_sum
import numpy as np

class Gui_2D(Gui):
    def __init__(self, game):
        super().__init__(game)

    def draw_outline(self):
        self.canvas.create_rectangle(100, 100, 500, 500, fill="white")
        self.canvas.create_text(300, 520, text='Player 1, Pr(strategy 1)')
        self.canvas.create_text(100, 520, text='0')
        self.canvas.create_text(500, 520, text='1')
        self.canvas.create_text(50, 300, text='Player 2 ')
        self.canvas.create_text(50, 320, text='Pr(strategy 1)')
        self.canvas.create_text(80, 500, text='1')
        self.canvas.create_text(80, 100, text='0')

    def map_coords(self, strat):
        return (strat[0]*400+100 , strat[1]*400+100)

    def plot_points(self):
        self.create_circle(self.map_coords([self.game.x_strats[self.i][0], self.game.y_strats[self.i][0]]))

if __name__ == "__main__":
    game_mat = np.array([[1, -1], [-1, 1]])
    eta = 0.1
    init_strategy_x = np.array([0.51, 0.49])
    init_strategy_y = np.array([0.51, 0.49])
    game = Mw_zero_sum(game_mat, eta, init_strategy_x, init_strategy_y, 1000)

    print(game.x_strats)
    print(game.y_strats)

    Gui_2D(game)