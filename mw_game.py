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
        self.x_payoffs = np.array([])
        self.y_payoffs = np.array([])
        self.play_game(num_iters=num_iters)
    
    @abstractmethod
    def update(self):
        assert False, "update method not implemented"
        
    @abstractmethod
    def payoff(self):
        assert False, "append_payoff method not implemented"

    def play_game(self, num_iters):
        for _ in range(num_iters):
            self.update()
            self.x_strats.append(self.x)
            self.y_strats.append(self.y)
            self.payoff()
            
