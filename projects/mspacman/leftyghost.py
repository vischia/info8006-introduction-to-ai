from game import Directions
import util
from ghostAgents import GhostAgent


class Leftyghost(GhostAgent):
    "A ghost that prefers to rush Pacman, or flee when scared."

    def __init__(self, index):
        self.index = index

    def getDistribution(self, state):
        # Read variables from state
        legalActions = state.getLegalActions(self.index)
        dist = util.Counter()
        for a in legalActions:
            dist[a] = 0.05
        left = Directions.WEST
        if left in legalActions:
            dist[left] = 1
            dist.normalize()
            return dist
        south = Directions.SOUTH
        if south in legalActions:
            dist[south] = 1
            dist.normalize()
            return dist
        east = Directions.EAST
        if east in legalActions:
            dist[east] = 1
            dist.normalize()
            return dist
        north = Directions.NORTH
        if north in legalActions:
            dist[north] = 1
            dist.normalize()
            return dist