from tkinter import *
from gui import Gui
from mw_zero_sum import Mw_zero_sum
import numpy as np
import math 

class Gui_3D(Gui):
    def __init__(self, game):
        super().__init__(game)

    def draw_outline(self):
        length = 400
        bottom_left = (100, 460)
        top = (bottom_left[0] + int(length/2), bottom_left[1] - int(length * math.sin(math.radians(60))))
        bottom_right = (bottom_left[0] + length, bottom_left[1])

        points = [bottom_left[0], bottom_left[1], top[0], top[1], bottom_right[0], bottom_right[1]]
        self.canvas.create_polygon(points, fill="white", outline="black")
        

        for i in range(0,5):
            self.canvas.create_line(100+100*i, bottom_left[1], 100 + 50*i, 460 - (i*100)*math.sin(math.radians(60)), dash=(2, 3))
            self.canvas.create_text(100+100*i+8-20, bottom_left[1]+25, text="Pr=" + str(i*.25), angle=60)
        
            self.canvas.create_line(100+100*i, bottom_left[1], 300 + 50*i, 460 - (400 - i*100)*math.sin(math.radians(60)), dash=(2, 3))
            self.canvas.create_text(50 + 50*(i+1)-15, bottom_left[1]-(i)*100*math.sin(math.radians(60))-15, text="Pr=" + str(i*.25), angle=300)
            if i!=0:
                self.canvas.create_line(50 + 50*i, bottom_left[1]-(i-1)*100*math.sin(math.radians(60)), 300 + 50*(5-i),  bottom_left[1]-(i-1)*100*math.sin(math.radians(60)), dash=(2, 3))
            self.canvas.create_text(300 + 50*(5-i)-25,  bottom_left[1]-(i)*100*math.sin(math.radians(60)), text="Pr=" + str(i*.25))
            
        self.canvas.create_text(bottom_left[0] + int(length/2), bottom_left[1] + 55, text='Strategy 1 Probability')
        self.canvas.create_text(bottom_left[0] + int(length/10), bottom_left[1] - int(int(length/2) * math.sin(math.radians(60))), text='Strategy 2 probability', angle = 60)
        self.canvas.create_text(bottom_right[0] - int(length/10), bottom_right[1] - int(int(length/2) * math.sin(math.radians(60))), text='Strategy 3 Probability', angle = 300)
    
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