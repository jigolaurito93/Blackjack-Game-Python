import random 

# Function to choose a random card (number) from the deck and returns the card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []
is_game_over = False

# Loop through twice to append the random cards to the list(user_cards and computer_cards)
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

print(user_cards)

# Create a function that calculates the sum of the cards in hand and returns the result
def calculate_score(cards):
    # If the sum is already 21 and there are only 2 cards in hand, it's blackjack. You should return 0
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # If the sum of cards in hand is over 21 and you have 11 in hand, remove 11 and add 1 instead. 1 and 11 serves as the Ace card
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

if user_score == 0 or user_score > 21 or computer_score == 0:
    is_game_over = True
