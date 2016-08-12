import random

deck = []

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
names = [["Two", 2], ["Three", 3], ["Four", 4], ["Five", 5],
        ["Six", 6], ["Seven", 7], ["Eight", 8], ["Nine", 9],
        ["Ten", 10], ["Jack", 10], ["Queen", 10], ["King", 10], ["Ace", 11]]

winnings = 0
stake = 10

print "Welcome to Blackjack." 
print "Dealer will hit on soft 17 and blackjack pays 3 for 2."
print "All stakes are 10." 
print "Would you like to play with 6 or 8 decks in this session?"
deck_number = raw_input('> ')
while deck_number != '6' and deck_number != '8':
    print "I am sorry, please select 6 or 8 decks for this session? [6/8]"
    deck_number = raw_input('> ')
deck_number = int(deck_number)

for i in range(deck_number):
    for suit in suits:
        for name in names:
            deck.append([suit, name])

random.shuffle(deck)

dealer_hand = []
player_hand = []

def ace_count(list):
    count = 0
    for i in list:
        if i[1][0] == "Ace":
            count += 1
    return count

def total(list):
    total = 0
    for a in list:
        total += a[1][1]
    if total > 21:
        if total - ace_count(list) * 10 <= 21:
            while total > 21:
                total -= 10
    return total
    
def display(list):
    for i in range(len(list)):
        print list[i][1][0] + " of " + list[i][0]

def endhand():
    if player_total > 21:
        print "\nI am afraid " + str(player_total) + " is greater than 21."
        return 0
    else:
        if player_total == 21 and len(player_hand) == 2:
            print "\nThat is blackjack."
            if dealer_hand[1][1][1] < 10:
                return 2.5
            else: 
                print "The dealer has:"
                display(dealer_hand)
                if total(dealer_hand) == 21:
                    print "Two blackjacks. A draw."
                    return 1
                else:
                    print "You win the hand."
                    return 2.5
        print "\nThe dealer has:"
        display(dealer_hand)
        while (
            total(dealer_hand) < 17 or 
            total(dealer_hand) == 17 and ace_count(dealer_hand) > 0
            ):
            dealer_hand.insert(0, deck.pop())
            print "\nThe dealer hits:"
            print dealer_hand[0][1][0] + " of " + dealer_hand[0][0]
        dealer_total = total(dealer_hand)
        print "The dealer scores " + str(dealer_total) + "."    
        if dealer_total == 21 and len(dealer_hand) == 2:
            print "The dealer has blackjack. You lose the hand."
            return 0
        elif player_total > dealer_total:
            print "Congratulations, you win this round."
            return 2
        elif dealer_total > 21:
            print "The dealer has bust."
            print "Congratulations, you win this round."
            return 2
        elif player_total == dealer_total:
            print "A draw. " + str(player_total) + " apiece."
            return 1
        else:
            print str(dealer_total) + " is greater than " + str(player_total)
            return 0


print "Shall I deal you in? [y/n]"
answer = raw_input('> ')
while answer != 'y' and answer != 'n':
    print "I am sorry, I don't understand. Deal you in? [y/n]"
    answer = raw_input('> ')


while answer == 'y':
    del dealer_hand[:]
    del player_hand[:]
    
    print "You place a bet of " + str(stake) + ".\n"
    winnings -= stake
    
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
        
    print "You have been dealt:"
    display(player_hand)
    
    print "\nYou can see the dealer is holding: " 
    print dealer_hand[1][1][0] + " of " + dealer_hand[1][0]
    
    options = ["[1] Hit", "[2] Stand"] #for future choice here
    
    decision = '1' 
    player_total = total(player_hand)
    
    while player_total < 21 and decision == '1':
        print "\nWould you like to:"
        print options[0] + "\t" + options[1]
        decision = raw_input('> ')
        
        while decision != '2' and decision != '1':
            print "I am sorry, I don't understand. Hit or stand? [1/2]"
            decision = raw_input('> ')
        
        if decision == '1':
            player_hand.insert(0, deck.pop())
            print "You have been dealt:"
            print player_hand[0][1][0] + " of " + player_hand[0][0]
            player_total = total(player_hand)
            print "Your total score is: " + str(player_total)
        
    payout = endhand()
    
    if payout == 0:
         print "Bad luck. You lose this hand."
    elif payout == 1: 
        print "You receive your stake back."
    else:
        print "Well done. You get " + str(stake*payout) + " back."
    
    winnings += stake*payout
    print "\nYour current winnings are " + str(winnings) + "."
    
    print "\nWould you like to play another hand? [y/n]"
    answer = raw_input('> ')
    while answer != 'y' and answer != 'n':
        print "I am sorry, I don't understand. Deal you in again? [y/n]"
        answer = raw_input('> ')

print "Your winnings are " + str(winnings) + "."
print "Have a great day."
exit(0)
