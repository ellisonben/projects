#!/usr/bin/env python

from Queue import PriorityQueue


class State(object):
    
    def __init__(self, value, parent, start=0, goal=0):
        self.children = [] #list of all possible children from state
        self.parent = parent
        self.value = value
        self.dist = 0 #placeholder - will be set in sublclasses
        if parent:
            self.path = parent.path[:] #copies parent path
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal  = goal
    
    def get_dist(self):
        pass
    
    def create_children(self):
        pass


class StateString(State):
    
    def __init__(self, value, parent, start=0, goal=0):
        super(StateString, self).__init__(value, parent, start, goal)
        self.dist =self.get_dist()
    
    def get_dist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)): ##measures distance of letter from goal
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))
        return dist
    
    def create_children(self):
        if not self.children:
            for i in xrange(len(self.goal) - 1): #swaps letters to create child
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2:] 
                child = StateString(val, self)
                self.children.append(child) #generates children & adds to list


class AStarSolver:

    def __init__(self, start, goal):
        self.path = [] #this will hold solution
        self.visited_queue = [] # holds already viewed children
        self.priority_queue = PriorityQueue()
        self.start = start
        self.goal = goal
    
    def solve(self):
        start_state = StateString(self.start, 0, self.start, self.goal)
        count = 0 #will be used to create an ID for the child created
        self.priority_queue.put((0, count, start_state))
        while (not self.path and self.priority_queue.qsize()):
            closest_child = self.priority_queue.get()[2]
            closest_child.create_children()
            self.visited_queue.append(closest_child.value)
            for child in closest_child.children:
                if child.value not in self.visited_queue:
                    count += 1
                    if not child.dist:
                        self.path = child.path
                        break #triggered when solution is found
                    self.priority_queue.put((child.dist, count, child))
        if not self.path:
            print "Goal of " + self.goal + " is not possible."
            return self.path

if __name__ == "__main__":
    start1 = "cbdae"
    goal1 = "abcde"
    print "starting..."
    a = AStarSolver(start1, goal1)
    a.solve()
    for i in xrange(len(a.path)):
        print "%d) " %i + a.path[i]
