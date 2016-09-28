from sys import exit 

class Scene(object):

    """The Scene class is the parent class for the rooms in the game."""

    def enter(self):
        print "This should not happen as there should be a subclass."
        exit(1)
         
class Engine(object):

    """The Engine class runs the game and calls enter on the instances of 
    the scenes that the Map creates"""

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.start_scene
        final_scene = self.scene_map.next_scene('finish')
        while current_scene != final_scene:
            next_scene = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene)
        current_scene.enter()

class RoomOne(Scene):

    def enter(self):
        print "Welcome challenger. You must use your wits to negotiate your"
        print "way through the rooms of the palace. Good luck.\n"
        print "Ahead lies an open book with pages propped open.\n"
        print "What does man love more than life,"
        print "fear more then death or mortal strife,"
        print "what the poor have the rich require,"
        print "and all contented men desire."
        print "What misers spend and spendthrifts save"
        print "and all men carry to the grave?"
        answer = raw_input('> ')
        while answer!= 'nothing':
            print "Try again, challenger."
            answer = raw_input('> ')
        print "\nVery good. Continue to the next room, challenger.\n"
        return 'room_two'

class RoomTwo(Scene):

    def enter(self):
        print "You enter the second room and an ethereal voice speaks: \n"
        print "One hundred eyes of green and blue" 
        print "Just look like eyes behind me, man."
        print "I shudder, shake and turn to you."
        print "As birds go, I'm your biggest fan.\n"
        print "What am I?"
        i=0
        while i<5:
            answer = raw_input('> ')
            if answer == 'peacock' or answer == 'a peacock':
                print "\nGreat work, challenger. Proceed to the final room.\n"
                return 'room_three'
            else:
                i += 1
                p = 5 - i
                print "Try again, challenger."
                print "You have %s tries remaining" % p
        print "\nNo tries left. Back to the start.\n"
        return 'room_one'

class RoomThree(Scene):

    def enter(self):
        print "This is the final room and now one final puzzle."
        print "A great orb descends from the ceiling."
        print "A voice emanates:\n"
        print "A suit of circling rings I wear;"
        print "Beneath my skin my armour is deep;"
        print "So come and strike me - if you dare!"
        print "For if you wound me, you will weep."
        print "What am I?"
        answer = raw_input('> ')
        if answer == 'onion' or answer == 'an onion':
            return 'finish'
        else:
            print "\nI am afraid your answer has angered the King."
            print "Back to the first room with you.\n\n"
            return 'room_one'

class Finish(Scene):

    def enter(self):
        print "\nCongratulations, challenger."
        print "You have made it out of the court of the Onion King."
        print "Happy riddling!"
        exit(1)

class Map(object):

    """The Map class creates instances of the scenes for the engine to
    call methods on."""
    
    scenes = {
        'room_one': RoomOne(),
        'room_two': RoomTwo(),
        'room_three': RoomThree(),
        'finish': Finish()
        } 
    
    def __init__(self, start_scene):
        self.start_scene = Map.scenes.get(start_scene)
    
    def next_scene(self, next_scene):
        next = Map.scenes.get(next_scene)
        return next
        
