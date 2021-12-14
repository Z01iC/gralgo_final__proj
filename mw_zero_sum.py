import numpy as np
import mw_game

class Mw_zero_sum(mw_game.Mw_game):
    def __init__(self, game, eta, init_strategy_x, init_strategy_y, num_iters=100):
        """[summary]

        Args:
            game ([nxn] numpy matrix): matrix representing the game
            eta (float between (0,1)): step size for multiplicative weights
            init_strategy_x ([nx1] numpy matrix ): player x's initial strategy
            init_strategy_y ([nx1] numpy matrix ): player y's initial strategy

        """
        super().__init__(game, eta, init_strategy_x, init_strategy_y, num_iters)
    
    def update(self):
        x_denom = self.x.T @ np.exp(self.eta * self.game @ self.y)
        x = (self.x * np.exp(self.eta * self.game @ self.y)) / x_denom
        y_denom = self.y.T @ np.exp(-self.eta * self.game.T @ self.x)
        self.y = (self.y * np.exp(-self.eta * self.game.T @ self.x)) / y_denom
        self.x = x

    def payoff(self):
        payoff = self.x.T @ self.game @ self.y
        self.x_payoffs = np.append(self.x_payoffs, payoff)
        self.x_payoffs = np.append(self.x_payoffs, -payoff)
            
            
