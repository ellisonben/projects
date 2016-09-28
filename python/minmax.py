from sys import maxsize

##=============================================================================
## TREE BUILDER

class Node(object):

    def __init__(self, i_depth, i_player_num, i_sticks_remaining, i_value=0):
        self.i_depth = i_depth
        self.i_player_num = i_player_num
        self.i_sticks_remaining = i_sticks_remaining
        self.i_value = i_value
        self.children = []
        self.create_children()
    
    def create_children(self):
        if self.i_depth >= 0:
            for i in range(1, 3):
                v = self.i_sticks_remaining - i
                self.children.append(Node(  self.i_depth - 1, 
                                            -self.i_player_num, 
                                            v,
                                            self.real_val(v)))

    def real_val(self, value):
        if value == 0:
            return maxsize * self.i_player_num
        elif value < 0:
            return maxsize * -self.i_player_num
        return 0
         
##=============================================================================
## ALGORITHM

def min_max(node, i_depth, i_player_num):
    if i_depth == 0 or abs(node.i_value) == maxsize:
        return node.i_value
    
    i_best_value = maxsize * -i_player_num
    
    for child in node.children:
        i_val = min_max(child, i_depth - 1, -i_player_num)
        ##it seems like the below if can be simplified
        if (abs(maxsize * i_player_num - i_val) < 
            abs(maxsize * i_player_num - i_best_value)):
            i_best_value = i_val
    
    return i_best_value 
    
##=============================================================================
## IMPLEMENTATION

def win_check(i_sticks, i_player_num):
    if i_sticks <= 0:
        print "*"*30
        if i_player_num > 0:
            if i_sticks == 0:
                print "\tYou WIN!"
            else:
                print "\tTOO MANY! You lose..."
        else:
            if i_sticks == 0:
                print "\tComputer wins... better luck next time."
            else:
                print "\tComputer ERROR!"
        print "*"*30
        return 0
    return 1

if __name__ == "__main__":
    i_stick_total = 11
    i_depth = 7
    i_cur_player = 1
    print "INSTRUCTIONS: Be the player to pick up the last stick"
    print "You can only pick up one (1) or two (2) sticks at a time."
    
    while i_stick_total > 0:
        print ("\n%d sticks remain. How many would you like to pick up?" 
        % i_stick_total)
        i_choice = input("\n1 or 2: ")
        i_stick_total -= int(float(i_choice))
        if win_check(i_stick_total, i_cur_player):
            i_cur_player *= -1
            node = Node(i_depth, i_cur_player, i_stick_total)
            best_choice = -100
            i_best_value = -i_cur_player * maxsize
            for i in range(len(node.children)):
                n_child = node.children[i]
                i_val = min_max(n_child, i_depth, -i_cur_player)
                if (abs(maxsize * i_cur_player - i_val) <=
                    abs(maxsize *  i_cur_player - i_best_value)):
                    i_best_value = i_val
                    best_choice = i
            best_choice += 1
            print "Comp chooses: " + str(best_choice)
            print "Based on value: " + str(i_best_value)
            i_stick_total -= best_choice
            win_check(i_stick_total, i_cur_player)
            i_cur_player *= -1
