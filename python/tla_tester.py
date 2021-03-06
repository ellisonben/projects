import random
from math import sqrt

LETTERS = map(chr, range(ord('A'), ord('Z'))) 
TOTAL_PERMS = len(LETTERS) ** 3

def generate():
    s = ""
    for i in range(3):
        s += random.choice(LETTERS)
    return s
    
def get_conf_interval(num_known, num_tests):
    sample_p = num_known / num_tests
    CRIT_VALUE = 1.96   #could use scipy to create variable to adjust conf level
    std_error = sqrt((sample_p * (1-sample_p)) / num_tests)
    margin_of_error = CRIT_VALUE * std_error
    return (sample_p - margin_of_error, sample_p + margin_of_error)

def check(answer):
    while answer != 'y' and answer != 'n':
        if answer == 'quit':
            exit(0)
        print "I am sorry, I don't understand. Do you know this TLA? [y/n]"
        answer = raw_input('> ')

def test_knowledge(num_known, num_tests):
    num_tests += 1
    print "Do you know this TLA? [y/n]"
    print generate()
    answer = raw_input('> ')
    check(answer)
    if answer == 'y':
        num_known += 1
    return num_known, num_tests

def display_info(num_known, num_tests):
    percentage = num_known/num_tests
    print "\nYou have %i correct answers out of %i." % (num_known, num_tests) 
    print "You have got %.2f percent correct (to 2dp)." % (percentage * 100)
    print "You know approximately %i TLAs." % round(percentage * TOTAL_PERMS)
    if num_tests > 100:
        bounds = [str(int(round(p_bounds*TOTAL_PERMS))) 
            for p_bounds in get_conf_interval(num_known, num_tests)] 
        print "\nWe are 95% confident that you know "
        print "between " + bounds[0] + " and " + bounds [1] + " TLAs.\n" 

def welcome():
    print "Welcome to TLA test.\n"
    print "Today we will test how many three letter acronyms (TLAs) you know."
    print "\nYou will immediately begin to get live feedback on your current "
    print "correct percentage and the estimated number of TLAs that you know."
    print "\nOnce you have logged 100 answers we will be able to give an"
    print "approximate 95% confidence interval. The more tests you do, the"
    print "narrower the interval should become."
    print "\nTo leave the test at any time, type 'quit'."
    print "\nThis is a self-assessment exercise. We hope that it is useful."
    
def start_test():
    welcome()
    num_tests = 0.0
    num_known = 0.0
    while True:
        num_known, num_tests = test_knowledge(num_known, num_tests)
        display_info(num_known, num_tests)

if __name__ == '__main__':
    start_test()
