import numpy as np

class Trainer:

    def __init__(self):
        pass

    ## Util to create numpy array of encoded inputs
    def encodeGrid(self, snakeCoordinates, appleCoordinates):
        grid = np.zeros((100, 100))

        for coordinate in snakeCoordinates:
            for x, y in coordinate:
                if coordinate == 0:
                    grid[x, y] = 1 # mark snake's head as 1
                else:
                    grid[x, y] = 2 # mark snake's body as 2

        for x,y in appleCoordinates:
            grid[x, y] = 3 # mark apple as 3
        return grid

    def simulate(self, numberToSimulate):
        pass

    def select(self, numberToSelect):
        pass

    def mutate(self, mutateRate):
        pass
