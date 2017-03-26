# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
  
    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem 
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state
   
        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state
   
        For a given state, this should return a list of triples, 
        (successor, action, stepCost), where 'successor' is a 
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental 
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take
   
        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def graphSearch(problem, frontier):
    # Initialize
    exploredSet = util.Stack()
    solution = util.Stack()
    try:

        currentPath = [(problem.getStartState(), "Start", 0)]
        currentPoint = currentPath[-1]
        frontier.push(currentPath)
        while (not problem.isGoalState(currentPoint[0])):
            if frontier.isEmpty():
                print "frontier is None, stopping..."
                break
            else:
                currentPath = frontier.pop()
                currentPoint = currentPath[-1]
                if problem.isGoalState(currentPoint[0]):
                    break
                if currentPoint[0] not in exploredSet.list:
                    exploredSet.push(currentPoint[0])
                    leafs = problem.getSuccessors(currentPoint[0])
                    for leaf in leafs:
                        if (leaf[0] not in exploredSet.list):
                            solution.list = currentPath[:]
                            solution.push(leaf)
                            frontier.push(solution.list)
        solution.list = [x[1] for x in currentPath][1:]
        return solution.list
    except Exception as detail:
        print 'Handling run-time error:', detail


def depthFirstSearch(problem):
    frontier = util.Stack()
    return graphSearch(problem, frontier)


def breadthFirstSearch(problem):
    "Search the shallowest nodes in the search tree first. [p 74]"
    # implementing a queue with FIFO will behave for bfs to handle less long nodes first
    frontier = util.Queue()
    return graphSearch(problem, frontier)


def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    pathCost = lambda ufsPath: problem.getCostOfActions([x[1] for x in ufsPath][1:])
    frontier = util.PriorityQueueWithFunction(pathCost)
    return graphSearch(problem, frontier)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    # because my calculated path is in array of paths i use myPath[-1][0], -1 is the last
    # item in the path array and the first node of that which is the point itself (<type 'tuple'>: (35, 1)).
    pathCost = lambda astarPath: problem.getCostOfActions([x[1] for x in astarPath][1:]) + heuristic(astarPath[-1][0],
                                                                                                     problem)
    frontier = util.PriorityQueueWithFunction(pathCost)
    return graphSearch(problem, frontier)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch