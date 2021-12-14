from tkinter import *
import mw_zero_sum
import numpy as np
import mw_game
class Mw_vis_2x2():
    def __init__(self, game):
        self.master: Tk = Tk()
        self.canvas = Canvas(self.master, width=500, height=500)
        self.canvas.create_rectangle(100, 100, 400, 400, fill="white")
        self.canvas.pack()
        self.game: mw_game.Mw_game = game
        self.i = 0
        print("initialized game")
        self.main_loop()
        self.master.mainloop()

    def create_circle(self, coords, r, player): #center coordinates, radius
        x0 = coords[0] - r
        y0 = coords[1] - r
        x1 = coords[0] + r
        y1 = coords[1] + r
        return self.canvas.create_oval(x0, y0, x1, y1, fill="red" if player else "blue")

    # def map_coords(self, strat):
    #     return (strat[0]*300+100 , strat[1]*300+100)

    # def main_loop(self):
    #     if self.i < self.game.num_iters:
    #         self.create_circle(self.map_coords(self.game.x_strats[self.i]), 15, True)
    #         self.create_circle(self.map_coords(self.game.y_strats[self.i]), 15, False)
    #         self.canvas.after(100, self.main_loop)
    #         self.i += 1

    def map_coords(self, x_strat, y_strat):
        return (x_strat[0] * 300 + 100, y_strat[0] * 300 + 100)

    def main_loop(self):
        if self.i < self.game.num_iters:
            self.create_circle(self.map_coords(self.game.x_strats[self.i], self.game.y_strats[self.i]), 5, True)
            self.canvas.after(100, self.main_loop)
            self.i += 1

if __name__ == "__main__":
    game_mat = np.array([[1, -1], [-1, 1]])
    eta = 0.1
    init_strategy_x = np.array([0.51, 0.49])
    init_strategy_y = np.array([0.51, 0.49])
    game = mw_zero_sum.Mw_zero_sum(game_mat, eta, init_strategy_x, init_strategy_y, 1000)

    print(game.x_strats)
    print(game.y_strats)

    Mw_vis_2x2(game)