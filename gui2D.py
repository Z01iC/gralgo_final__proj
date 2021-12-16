from tkinter import *
from consts import POINT_RADIUS
from gui import Gui
from mw_zero_sum import Mw_zero_sum
import numpy as np
from consts import *

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
        self.x_payoff = self.canvas.create_text(400, 20, text='Avg x payoff:')
        self.y_payoff = self.canvas.create_text(400, 40, text='Avg y payoff: ')
        self.canvas.create_text(400, 60, text='Payoffs updated every second, not every iteration')
        self.make_key()

    def make_key(self):
        self.canvas.create_text(15, 20, text='Key:')
        self.canvas.create_text(50, 40, text='Strategy')
        self.canvas.create_text(93, 60, text='Time Average Strategy')
        self.draw_circle((10, 40), self.get_color(COLORS[-1], True), 6)
        self.draw_circle((10, 60), COLORS_3D_P1_AVG[-1], 6)
        self.canvas.create_rectangle(1, 1, 200, 80)

    def map_coords(self, strat):
        return (strat[0]*400+100 , strat[1]*400+100)

    def plot_points(self):
        self.create_circle(self.map_coords([self.game.x_strats[self.i][0], self.game.y_strats[self.i][0]]))
        self.create_circle(self.map_coords([self.game.avg_x[self.i][0], self.game.avg_y[self.i][0]]), POINT_RADIUS*2, True, COLORS, True)
        if self.i % FRAME_RATE == 0:
            self.canvas.itemconfig(self.x_payoff, text='Avg x payoff: ' + str(self.game.x_payoffs[self.i]))
            self.canvas.itemconfig(self.y_payoff, text='Avg y payoff: ' + str(self.game.y_payoffs[self.i]))


if __name__ == "__main__":
    game_mat = np.array([[1, -1], [-1, 1]])
    eta = 0.1
    init_strategy_x = np.array([0.51, 0.49])
    init_strategy_y = np.array([0.51, 0.49])
    game = Mw_zero_sum(game_mat, eta, init_strategy_x, init_strategy_y)
    Gui_2D(game)