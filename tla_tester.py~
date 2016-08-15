import random
from math import sqrt

LETTERS = map(chr, range(65, 91)) 
TOTAL_PERMS = len(LETTERS) ** 3

num_tests = 0.0
num_known = 0.0

def generate():
    s = ""
    for i in range(3):
        s += random.choice(LETTERS)
    return s
    
def get_conf_interval():
    global num_known 
    global num_tests
    sample_p = num_known / num_tests
    CRIT_VALUE = 1.96   #could use scipy to create variable to adjust conf level
    std_error = sqrt((sample_p * (1-sample_p)) / num_tests)
    margin_of_error = CRIT_VALUE * std_error
    return (sample_p - margin_of_error, sample_p + margin_of_error)

def check(answer):
    if answer == quit:
        exit(0)
    while answer != 'y' and answer != 'n':
        print "I am sorry, I don't understand. Do you know this TLA? [y/n]"
        answer = raw_input('> ')

def test_knowledge():
    global num_tests
    global num_known
    num_tests += 1
    print "Do you know this TLA? [y/n]"
    print generate()
    answer = raw_input('> ')
    check(answer)
    if answer == 'y':
        num_known += 1

def display_info():
    percentage = num_known/num_tests
    print "\nYou have %s correct answers out of %s." % (num_known, num_tests) 
    print "That is %.2f percent correct (to 2dp)." % (percentage * 100)
    print "You know approximately %s TLAs." % (percentage * TOTAL_PERMS)
    if num_tests > 9:
        bounds = [str(int(round(p_bounds*TOTAL_PERMS))) 
            for p_bounds in get_conf_interval()] 
        print "\nWe are 95% confident that you know "
        print "between " + bounds[0] + " and " + bounds [1] + " TLAs.\n" 

def welcome():
    print "Welcome to TLA test."
    print "Today we will test how many three letter acronyms (TLAs) you know."
    print "You will immediately begin to get live feedback on your current "
    print "correct percentage and the estimated number of TLAs that you know."
    print "Once you have logged 100 answers we will be able to give an"
    print "approximate 95% confidence interval. The more tests you do, the"
    print "the smaller the confidence interval will become as the standard"
    print "error of the mean will become smaller as the sample mean tends"
    print "towards the parametric mean."
    print "\nTo leave the test at any time, type 'quit'."
    print "\nThis is a self-assessment exercise. We hope that it is useful."
    
def reset_totals():
    global num_tests
    global num_known
    num_tests = 0.0
    num_known = 0.0

def start_test():
    welcome()
    reset_totals()
    while True:
        test_knowledge()
        display_info()

start_test()
