import numpy as np

class Mw_zero_sum():
    def __init__(self, game, eta, init_strategy_x, init_strategy_y):
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
        self.x_strats = np.array([self.x])
        self.y_strats = np.array([self.y])
        self.x_payoffs = np.array([])
        self.y_payoffs = np.array([])
    
    def update(self):
        x_denom = self.x.T @ np.exp(self.eta * self.game @ self.y)
        x = (self.x * np.exp(self.eta * self.game @ self.y)) / x_denom
        y_denom = self.y.T @ np.exp(self.eta * self.game.T @ self.x)
        self.y = (self.y * np.exp(-self.eta * self.game.T @ self.x)) / y_denom
        self.x = x

    def payoff(self):
        return self.x.T @ self.game @ self.y

    def play_game(self, num_iters):
        for _ in range(num_iters):
            self.update()
            self.x_strats.append(self.x)
            self.y_strats.append(self.y)
            payoff = self.payoff()
            self.x_payoffs.append(payoff)
            self.y_payoffs.append(-payoff)
            
