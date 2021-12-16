import numpy as np
import mw_game

class Mw_cooperative(mw_game.Mw_game):
    def __init__(self, game, eta, init_strategy_x, init_strategy_y, num_iters=800):
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
        y_denom = self.y.T @ np.exp(self.eta * self.game @ self.x)
        self.y = (self.y * np.exp(self.eta * self.game @ self.x)) / y_denom
        self.x = x

    def payoff(self, i):
        x_payoff = self.x.T @ self.game @ self.y
        y_payoff = self.x.T @ self.game @ self.y
        prev_x_payoff = self.x_payoffs[-1] if len(self.x_payoffs) > 0 else 0
        prev_y_payoff = self.y_payoffs[-1] if len(self.y_payoffs) > 0 else 0
        avg_x_payoff = round((prev_x_payoff * i + x_payoff) / (i+1), 10)
        avg_y_payoff = round((prev_y_payoff * i + y_payoff) / (i+1), 10)
        self.x_payoffs = np.append(self.x_payoffs, avg_x_payoff)
        self.y_payoffs = np.append(self.y_payoffs, avg_y_payoff)
            
            