from tkinter import *
from consts import *
from gui import Gui
from mw_zero_sum import Mw_zero_sum
import numpy as np
import math 

class Gui_3D(Gui):
    def __init__(self, game):
        super().__init__(game)

    def draw_outline(self):
        top = (BOTTOM_LEFT[0] + int(LENGTH/2), BOTTOM_LEFT[1] - int(LENGTH * math.sin(math.radians(60))))
        bottom_right = (BOTTOM_LEFT[0] + LENGTH, BOTTOM_LEFT[1])

        points = [BOTTOM_LEFT[0], BOTTOM_LEFT[1], top[0], top[1], bottom_right[0], bottom_right[1]]
        self.canvas.create_polygon(points, fill="white", outline="black")

        for i in range(0,5):
            self.canvas.create_line(100+100*i, BOTTOM_LEFT[1], 100 + 50*i, BOTTOM_LEFT[1] - (i*100)*math.sin(math.radians(60)), dash=(2, 3))
            self.canvas.create_text(100+100*i+8-20, BOTTOM_LEFT[1]+25, text="Pr=" + str(i*.25), angle=60)
        
            self.canvas.create_line(100+100*i, BOTTOM_LEFT[1], 300 + 50*i, BOTTOM_LEFT[1] - (LENGTH - i*100)*math.sin(math.radians(60)), dash=(2, 3))
            self.canvas.create_text(50 + 50*(i+1)-15, BOTTOM_LEFT[1]-(i)*100*math.sin(math.radians(60))-15, text="Pr=" + str(1-i*.25), angle=300)
            if i!=0:
                self.canvas.create_line(50 + 50*i, BOTTOM_LEFT[1]-(i-1)*100*math.sin(math.radians(60)), 300 + 50*(5-i),  BOTTOM_LEFT[1]-(i-1)*100*math.sin(math.radians(60)), dash=(2, 3))
            self.canvas.create_text(300 + 50*(5-i)-25,  BOTTOM_LEFT[1]-(i)*100*math.sin(math.radians(60)), text="Pr=" + str(i*.25))        

        self.canvas.create_text(BOTTOM_LEFT[0] + int(LENGTH/2), BOTTOM_LEFT[1] + 55, text='Strategy 1 Probability')
        self.canvas.create_text(BOTTOM_LEFT[0] + int(LENGTH/10), BOTTOM_LEFT[1] - int(int(LENGTH/2) * math.sin(math.radians(60))), text='Strategy 2 probability', angle = 60)
        self.canvas.create_text(bottom_right[0] - int(LENGTH/10), bottom_right[1] - int(int(LENGTH/2) * math.sin(math.radians(60))), text='Strategy 3 Probability', angle = 300)
        self.x_payoff = self.canvas.create_text(440, 15, text='Avg x payoff:')
        self.y_payoff = self.canvas.create_text(440, 35, text='Avg y payoff: ')
        self.canvas.create_text(440, 55, text='Payoffs updated every second, not every iteration')
        self.make_key()

    def make_key(self):
        self.canvas.create_text(15, 20, text='Key:')
        self.canvas.create_text(80, 40, text='Player 1 Strategy')
        self.canvas.create_text(80, 60, text='Player 2 Strategy')
        self.canvas.create_text(110, 80, text='Player 1 Time Avg Strategy')
        self.canvas.create_text(110, 100, text='Player 2 Time Avg Strategy')
        self.draw_circle((10, 40), self.get_color(COLORS[-1], True), 6)
        self.draw_circle((10, 60), self.get_color(COLORS_3D[-1], False), 6)
        self.draw_circle((10, 80), COLORS_3D_P1_AVG[-1], 6)
        self.draw_circle((10, 100), COLORS_3D_P2_AVG[-1], 6)
        self.canvas.create_rectangle(1, 1, 200, 120)

    def map_coords(self, strat):
        y = BOTTOM_LEFT[1] - strat[2] * LENGTH * math.sin(math.radians(60))
        b = 460 + (math.tan(math.radians(60)) * (100+400*strat[0]))
        x = (b - y) / math.tan(math.radians(60))
        return (x, y)

    def plot_points(self):
        self.create_circle(self.map_coords(self.game.x_strats[self.i]), POINT_RADIUS, True, COLORS_3D)
        self.create_circle(self.map_coords(self.game.y_strats[self.i]), POINT_RADIUS, False, COLORS_3D)
        self.create_circle(self.map_coords(self.game.avg_x[self.i]), POINT_RADIUS, True, COLORS, True)
        self.create_circle(self.map_coords(self.game.avg_y[self.i]), POINT_RADIUS, False, COLORS, True)
        if self.i % FRAME_RATE == 0:
            self.canvas.itemconfig(self.x_payoff, text='Avg x payoff: ' + str(self.game.x_payoffs[self.i]))
            self.canvas.itemconfig(self.y_payoff, text='Avg y payoff: ' + str(self.game.y_payoffs[self.i]))

if __name__ == "__main__":
    rock_papper_sissors = np.array([[0, 1, -1], [-1, 0, 1], [1, -1, 0]])
    eta = 0.1
    init_strategy_x = np.array([0.25, 0.5, 0.25])
    init_strategy_y = np.array([0.25, 0.25, 0.5])
    game = Mw_zero_sum(rock_papper_sissors, eta, init_strategy_x, init_strategy_y)
    gui = Gui_3D(game)

    