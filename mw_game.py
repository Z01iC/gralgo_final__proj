import numpy as np
from abc import ABC, abstractmethod

class Mw_game(ABC):
    def __init__(self, game, eta, init_strategy_x, init_strategy_y, num_iters):
        """[summary]

        Args:
            game ([nxn] numpy matrix): matrix representing the game
            eta (float between (0,1)): step size for multiplicative weights
            init_strategy_x ([nx1] numpy matrix ): player x's initial strategy
            init_strategy_y ([nx1] numpy matrix ): player y's initial strategy

        """
        self.x = init_strategy_x
        self.y = init_strategy_y
        self.game = game
        self.eta = eta
        self.num_iters = num_iters
        self.x_strats = np.array([self.x])
        self.y_strats = np.array([self.y])
        self.avg_x = np.zeros((num_iters, len(self.x)))
        self.avg_y = np.zeros((num_iters, len(self.x)))
        self.play_game(num_iters=num_iters)
    
    @abstractmethod
    def update(self):
        assert False, "update method not implemented"

    @abstractmethod
    def payoff(self):
        assert False, "append_payoff method not implemented"

    def play_game(self, num_iters):
        for i in range(num_iters):
            self.update()
            self.x_strats = np.append(self.x_strats, [self.x], axis=0)
            self.y_strats = np.append(self.y_strats, [self.y], axis=0)
            self.time = np.append(self.y_strats, [self.y], axis=0)
            self.avg_x[i] = np.mean(self.x_strats, axis=0)
            self.avg_y[i] = np.mean(self.y_strats, axis=0)
            
        print(self.avg_x)
        print(self.avg_y)
        print("finisehd game")
            
