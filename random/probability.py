def blackjack_strategy(player_hand, dealer_upcard):
    # Hard totals strategy
    if isinstance(player_hand, int):
        if player_hand <= 8:
            return "Hit"
        elif player_hand == 9:
            if 3 <= dealer_upcard <= 6:
                return "Double if allowed, otherwise Hit"
            else:
                return "Hit"
        elif player_hand == 10:
            if 2 <= dealer_upcard <= 9:
                return "Double if allowed, otherwise Hit"
            else:
                return "Hit"
        elif player_hand == 11:
            return "Double"
        elif player_hand == 12:
            if 4 <= dealer_upcard <= 6:
                return "Stand"
            else:
                return "Hit"
        elif 13 <= player_hand <= 16:
            if 2 <= dealer_upcard <= 6:
                return "Stand"
            else:
                return "Hit"
        elif player_hand >= 17:
            return "Stand"
    
    # Soft totals strategy (where an Ace counts as 11)
    elif isinstance(player_hand, tuple) and 'A' in player_hand:
        ace_hand_value = sum(11 if card == 'A' else card for card in player_hand)
        if ace_hand_value <= 18:
            if 2 <= dealer_upcard <= 6:
                return "Double if allowed, otherwise Hit"
            elif ace_hand_value == 18 and 7 <= dealer_upcard <= 8:
                return "Stand"
            else:
                return "Hit"
        else:
            return "Stand"

    # Pair splitting strategy
    elif isinstance(player_hand, tuple) and player_hand[0] == player_hand[1]:
        pair_card = player_hand[0]
        if pair_card == 2 or pair_card == 3:
            if 2 <= dealer_upcard <= 7:
                return "Split"
            else:
                return "Hit"
        elif pair_card == 4:
            if 5 <= dealer_upcard <= 6:
                return "Split"
            else:
                return "Hit"
        elif pair_card == 5:
            if 2 <= dealer_upcard <= 9:
                return "Double"
            else:
                return "Hit"
        elif pair_card == 6:
            if 2 <= dealer_upcard <= 6:
                return "Split"
            else:
                return "Hit"
        elif pair_card == 7:
            if 2 <= dealer_upcard <= 7:
                return "Split"
            else:
                return "Hit"
        elif pair_card == 8:
            return "Split"
        elif pair_card == 9:
            if 2 <= dealer_upcard <= 6 or dealer_upcard in [8, 9]:
                return "Split"
            else:
                return "Stand"
        else:  # Pair of 10s
            return "Stand"

# Example usage:
player_hand = (10, 10)  # Example of a pair of 10s
dealer_upcard = 6
action = blackjack_strategy(player_hand, dealer_upcard)
print(f"Player hand: {player_hand}, Dealer's upcard: {dealer_upcard}, Action: {action}")
