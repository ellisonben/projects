from random import randint
from time import clock

##=============================================================================

State = type("State", (object,), {})

class LightOn(State):
    def execute(self):
        print "Light is on!"
    
class LightOff(State):
    def execute(self):
        print "Light is off!"

##=============================================================================

class Transition(object):
    def __init__(self, to_state):
        self.to_state = to_state
        
    def execute(self):
        print "Transitioning ..."

##=============================================================================

class SimpleFSM(object):
    def __init__(self, char):
        self.char = char
        self.states = {}
        self.transitions = {}
        self.cur_state = None
        self.trans = None
    
    def set_state(self, state_name):
        self.cur_state = self.states[state_name]
    
    def transition(self, trans_name):
        self.trans = self.transitions[trans_name]
    
    def execute(self):
        if self.trans:
            self.trans.execute()
            self.set_state(self.trans.to_state)
            self.trans = None
        self.cur_state.execute()
        
##=============================================================================

class Char(object):
    def __init__(self):
        self.FSM = SimpleFSM(self)
        self.light_on = True
        
##=============================================================================

if __name__ == "__main__":
    light = Char()
    
    light.FSM.states["On"] = LightOn()
    light.FSM.states["Off"] = LightOff()
    light.FSM.transitions["toOn"] = Transition("On")
    light.FSM.transitions["toOff"] = Transition("Off")
    
    light.FSM.set_state("On")
    
    for i in range(20):
        start_time = clock()
        time_interval = 1
        while(start_time + time_interval > clock()):
            pass
        if (randint(0, 2)):
            if (light.light_on):
                light.FSM.transition("toOff")
                light.light_on = False
            else:
                light.FSM.transition("toOn")
                light.light_on = True
        light.FSM.execute()
