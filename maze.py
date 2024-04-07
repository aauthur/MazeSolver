import time

start_time = time.time()

class Node():
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
    
class StackFrontier():
    def __init__(self):
        self.frontier = []
    def update(self, state):
        self.frontier.append(state)
    def isEmpty(self):
        return len(self.frontier) == 0
    def remove(self):
        if not self.isEmpty():
            x = self.frontier.pop(-1)
            return x
        else:
            print("Can't remove element from empty frontier.")

class QueueFrontier():
    def __init__(self):
        self.frontier = []
    def update(self, state):
        self.frontier.append(state)
    def isEmpty(self):
        return len(self.frontier) == 0
    def remove(self):
        if not self.isEmpty():
            x = self.frontier.pop(0)
            return x
        else:
            print("Can't remove element from empty frontier.")



def load_data(path):
    data = []
    with open(path, mode='r') as f:
        for line in f:
            data.append(line[:-1])
    f.close()
    return data

def get_endpoints(maze):
    for i in range(0, len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "A":
                start = (i,j)
            if maze[i][j] == "B":
                end = (i,j)
    return start, end


def main():
    while True:
        n = input("Type 0 to use Breadth-First-Search, or 1 to use Depth-First-Search to solve the maze: ")
        if n == "0":
            frontier = QueueFrontier()
            break
        elif n == "1":
            frontier = StackFrontier()
            break
        else:
            print("Invalid input. You must input either 0 or 1.")
    frontier = StackFrontier()
    explored = []
    frontier_positions = []
    maze = load_data("maze.txt")
    start, end = get_endpoints(maze)
    initial_state = Node(start)
    goal_state = Node(end)
    frontier.update(initial_state)
    frontier_positions.append(initial_state.state)
    if (input("Type Y to highlight explored portions of the maze in solution: ") == "Y"):
        show_explored = True
    else:
        show_explored = False
    solved = False
    while not frontier.isEmpty():
        pstate = frontier.remove()
        if pstate.state == goal_state.state:
            solution_set = set()
            solution = []
            while pstate.parent is not None:
                pstate = pstate.parent
                solution_set.add(pstate.state)
            for i in range(len(maze)):
                line = ""
                for j in range(len(maze[i])):
                    pos = (i,j)
                    if pos == start:
                        line = line + maze[i][j]
                    elif pos in solution_set:
                        line = line + "\033[92mX\033[0m"
                    elif (pos in explored) and (show_explored == True):
                        line = line + "\033[1;33mO\033[0m"
                    else:
                        line = line + maze[i][j]
                solution.append(line)            
            solved = True
            end_time = time.time()
            print("Solution Found!")
            print(f"Took {end_time-start_time} seconds to find the solution.")
            print()
            for i in range(len(solution)):
                print(solution[i])
            break
        else:
            explored.append(pstate.state)
            frontier_positions.remove(pstate.state)
            try:
                if (maze[pstate.state[0]+1][pstate.state[1]] != "#") and ((pstate.state[0]+1,pstate.state[1]) not in explored) and ((pstate.state[0]+1,pstate.state[1]) not in frontier_positions):
                    newpos = (pstate.state[0] + 1, pstate.state[1])
                    child = Node(state=newpos, parent=pstate)
                    frontier.update(child)
                    frontier_positions.append(child.state)
                if (maze[pstate.state[0]-1][pstate.state[1]] != "#") and ((pstate.state[0]-1,pstate.state[1]) not in explored) and ((pstate.state[0]-1,pstate.state[1]) not in frontier_positions):
                    newpos = (pstate.state[0] - 1, pstate.state[1])
                    child = Node(state=newpos, parent=pstate)
                    frontier.update(child)
                    frontier_positions.append(child.state)
                if (maze[pstate.state[0]][pstate.state[1] - 1] != "#") and ((pstate.state[0],pstate.state[1]-1) not in explored) and ((pstate.state[0],pstate.state[1]-1) not in frontier_positions):
                    newpos = (pstate.state[0], pstate.state[1] -1)
                    child = Node(state=newpos, parent=pstate)
                    frontier.update(child)
                    frontier_positions.append(child.state)
                if (maze[pstate.state[0]][pstate.state[1] + 1] != "#") and ((pstate.state[0],pstate.state[1]+1) not in explored) and ((pstate.state[0],pstate.state[1]+1) not in frontier_positions):
                    newpos = (pstate.state[0], pstate.state[1] +1)
                    child = Node(state=newpos, parent=pstate)
                    frontier.update(child)
                    frontier_positions.append(child.state)
            except IndexError:
                pass
    if solved:
        pass
    else:
        print('No solution exists to the given maze :(')










if __name__ == "__main__":
    main()