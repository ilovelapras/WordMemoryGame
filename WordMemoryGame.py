import random
import time
turn_counter = 0
score_counter = 0
card_images = ["apple","lemon","mango","olive","peach"]


def card_shuffling(card_images,cards,cards_list):
    for card_image in card_images:
        first_gen = random.choice(cards_list)
        while cards[first_gen] != 0:
            first_gen = random.choice(cards_list)
        cards[first_gen] = card_image

        second_gen = random.choice(cards_list)
        while cards[second_gen] != 0:
            second_gen = random.choice(cards_list)
        cards[second_gen] = card_image

while True:
    intro = input("Welcome To the Memory Game! Please press the Enter Button to start, or press any other key to exit.")
    if intro != "":
        print("Goodbye!")
        exit()
    else:
        cards = {"Card 1": 0, "Card 2": 0, "Card 3": 0, "Card 4": 0, "Card 5": 0, "Card 6": 0, "Card 7": 0, "Card 8": 0,
                 "Card 9": 0, "Card 10": 0}
        cards_list = list(cards.keys())
        card_shuffling(card_images,cards,cards_list)
        for key,value in cards.items():
            print(f"{key} is {value}.",end="\r")
            time.sleep(2)
        while len(cards)!= 0:
            turn_counter += 1
            print(f"\n--------------------Turn {turn_counter}--------------------")
            print(f"The following cards have yet to be guessed correctly.")
            for key in cards:
                print(key)
            card_guess_1 = input("Please input number of first card guess: ")
            card_guess_1 = "Card " + card_guess_1
            while card_guess_1 not in cards:
                card_guess_1 = input("Number only please/That card has been guessed right: ")
                card_guess_1 = "Card " + card_guess_1
            card_guess_2 = input("Please input number of second card guess: ")
            card_guess_2 = "Card " + card_guess_2
            while card_guess_2 not in cards or card_guess_2 == card_guess_1:
                card_guess_2 = input("Number only/no repeating card number please/That card has been guessed right:  ")
                card_guess_2 = "Card " + card_guess_2
            if cards[card_guess_1] == cards[card_guess_2]:
                print(f"Your guess was right. Cards {card_guess_1} & {card_guess_2} are both {cards[card_guess_1]}s.")
                del cards[card_guess_1]
                del cards[card_guess_2]

            else:
                print(f"Cards {card_guess_1} & {card_guess_2} are different.")
            score_counter += 1
        print(f"Your score is {score_counter}.")
        print("Thank you for playing!\n")











