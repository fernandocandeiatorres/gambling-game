import random

money = 100

# Write your game of chance functions here
# INTRO #

print("-> Hello! Welcome to Redrock Cassino, what's your name?")
name = input()

print("-> Hey there, " + str(name) + "! What's your age?")
# forces user to only use numbers as age
while True:
    try:
        age = int(input())
        break
    except ValueError:
        print("Please enter a valid number.")
        continue


# COINFLIP


def coin_flip(bet, guess):
    h_or_t = ["heads", "tails"]
    correct_guess = random.choice(h_or_t)  # pick random str in list

    print("-> The coinflip result is: " + correct_guess.title())

    if guess.lower() == correct_guess:
        global money  # calls global variable
        money += bet_cf*2
        return "-> Congratulations! You won: " + str(int(bet)*2) + "$"

    else:
        return "-> Oops.. maybe next time, you lost: -" + str(bet) + "$"

# DICE SUM


def dice_sum(bet, guess):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_sum = dice_1 + dice_2

    print("-> The dice sum result is: " + str(dice_sum))

    if dice_sum % 2 == 0 and guess.lower() == "even" or dice_sum % 2 != 0 and guess.lower() == "odd":
        global money
        money += bet_cf*2
        return "-> Congratulations! You won: " + str(int(bet)*2) + "$"

    else:
        return "-> Oops.. maybe next time, you lost: -" + str(bet) + "$"


# CARD GAME


def card_game(bet):  # the player bet if he got a higher number
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    player_1 = random.choice(deck)
    # prevents the user and the house to pick the same card, this should not be like this i guess...
    deck.remove(player_1)
    house = random.choice(deck)

    print("-> The house got: " + str(house))
    print("-> You got: " + str(player_1))

    global money

    if player_1 > house:
        money += bet*2
        return "-> Congratulations! You won: " + str(int(bet)*2) + "$"

    elif player_1 == house:
        money += bet
        return "-> That's a tie! You got your money back."

    else:
        return "-> Oops.. maybe next time, you lost: -" + str(bet) + "$"


# Call your game of chance functions here

# # CHECK AGE LATER: SEARCH TO SEE HOW TO ONLY ACCEPT INTEGER
if int(age) < 18:
    print("-> Oh oh, you can't gamble bud. Your below 18 years old!")

if int(age) >= 18:

    while money > 0:

        print(
            "Welcome to the cassino! How much you wanna bet? You got: " + str(money) + "$")

        # forces the user to only use numbers as the money
        while True:
            try:
                bet_cf = int(input())
                break
            except ValueError:
                print("Please enter a valid number.")
                continue

        if bet_cf > money:
            print("You don't have enough money.")
            continue

        else:
            print("-> So, what game do you wanna play?")
            print("-> For coinflip: " + str(1))
            print("-> For dice game: " + str(2))
            print("-> For card game: " + str(3))
            print("-> To stop playing: " + str(4))

            game_choice = int(input())
            print("-> Your current bet is: " + str(bet_cf) + "$")

            if game_choice == 1:  # COIN FLIP
                print("-> Welcome to the coinflip game!")

                money -= bet_cf
                print("-> " + str(bet_cf) +
                      "$ is on the table. What's your guess?")
                guess_cf = str(input())

                if guess_cf.lower() == "heads" or guess_cf.lower() == "tails":
                    print(coin_flip(bet_cf, guess_cf))
                    print("-> Your current balance is: " + str(money) + "$")
                    print("""
                    ###################
                    ###################
                    ###################
                    """)

                else:
                    print("Howdy! You can only guess Heads or Tails.")
                    money += bet_cf
                    continue

            elif game_choice == 2:  # DICE GAME

                print("-> Welcome to the dice game!")
                money -= bet_cf

                print("-> " + str(bet_cf) +
                      "$ is on the table. Will the dice sum be odd or even?")
                guess_cf = str(input())

                if guess_cf.lower() == "odd" or guess_cf.lower() == "even":

                    print(dice_sum(bet_cf, guess_cf))
                    print("-> Your current balance is: " + str(money) + "$")
                    print("""
                    ###################
                    ###################
                    ###################
                    """)

                else:
                    print("Howdy! You can only guess Odd or Even.")
                    money += bet_cf
                    continue

            elif game_choice == 3:  # CARD GAME

                print("-> Welcome to the card game!")
                money -= bet_cf

                print("-> " + str(bet_cf) + "$ is on the table.")
                print(card_game(bet_cf))

                print("-> Your current balance is: " + str(money) + "$")
                print("""
                ###################
                ###################
                ###################
                """)

            elif int(game_choice) == 4:  # user leaves the game
                print("Thank you for playing with us!")
                break
