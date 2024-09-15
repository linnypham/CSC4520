def blackjack(player, dealer):

    hand = sum(player)

    if hand == 21:
        return 'Stand'
    
    # Check for surrender conditions
    if hand == 16 and dealer in range(9, 12):
        return 'Surrender'
    if hand == 15 and dealer == 10:
        return 'Surrender'

    # Check for pair splitting
    if player[0] == player[1]:
        if player[0] == 11:  # Always split aces
            return 'Split'
        elif player[0] == 10:  # Never split tens
            return 'Stand'
        elif player[0] == 9 and dealer in range(2,10):  # Split 9s except against 7
            return 'Split'
        elif player[0] == 9 and dealer == 7:  # Stand against 7
            return 'Stand'
        elif player[0] == 8:  # Always split 8s
            return 'Split'
        elif player[0] == 7 and dealer in range(2, 8):  # Split 7s against dealer 2-7, otherwise hit
            return 'Split'
        elif player[0] == 7:  # Hit against dealer 8 and above
            return 'Hit'
        elif player[0] == 6 and dealer in range(2, 7):  # Split 6s against dealer 2-6, otherwise hit
            return 'Split'
        elif player[0] == 6:  # Hit against dealer 7 and above
            return 'Hit'
        elif player[0] == 5 and dealer in range(2, 10):  # Double 5s against dealer 2-9, otherwise hit
            return 'Double'
        elif player[0] == 5:  # Hit against dealer 10 or Ace
            return 'Hit'
        elif player[0] == 4 and dealer in {5, 6}:  # Split 4s against dealer 5 and 6, otherwise hit
            return 'Split'
        elif player[0] == 4:  # Hit against any other dealer cards
            return 'Hit'
        elif player[0] == 3 and dealer in range(2, 8):  # Split 3s against dealer 2-7, otherwise hit
            return 'Split'
        elif player[0] == 3:  # Hit against dealer 8 and above
            return 'Hit'
        elif player[0] == 2 and dealer in range(2, 8):  # Split 2s against dealer 2-7, otherwise hit
            return 'Split'
        else:  # Hit against dealer 8 and above
            return 'Hit'

    # Check for soft totals (Ace as one of the first two cards)
    if 11 in player:
        if hand == 20:  # Soft 20 (A,9) always stands
            return 'Stand'
        elif hand == 19 and dealer == 6:  # Soft 19 (A,8) doubles against dealer 6
            return 'Double'
        elif hand == 19:  # Soft 19 (A,8) otherwise stands
            return 'Stand'
        elif hand == 18 and dealer in range(2, 7):  # Soft 18 (A,7) doubles against dealer 2-6
            return 'Double'
        elif hand == 18 and dealer in range(9, 12):  # Soft 18 (A,7) hits against dealer 9 through Ace
            return 'Hit'
        elif hand == 18:  # Soft 18 (A,7) otherwise stands
            return 'Stand'
        elif hand == 17 and dealer in range(3, 7):  # Soft 17 (A,6) doubles against dealer 3-6
            return 'Double'
        elif hand == 17:  # Soft 17 (A,6) otherwise hits
            return 'Hit'
        elif hand == 16 and dealer in range(4, 7):  # Soft 16 (A,5) doubles against dealer 4-6
            return 'Double'
        elif hand == 16:  # Soft 16 (A,5) otherwise hits
            return 'Hit'
        elif hand == 15 and dealer in range(4, 7):  # Soft 15 (A,4) doubles against dealer 4-6
            return 'Double'
        elif hand == 15:  # Soft 15 (A,4) otherwise hits
            return 'Hit'
        elif hand == 14 and dealer in {5, 6}:  # Soft 14 (A,3) doubles against dealer 5-6
            return 'Double'
        elif hand == 14:  # Soft 14 (A,3) otherwise hits
            return 'Hit'
        elif hand == 13 and dealer in {5, 6}:  # Soft 13 (A,2) doubles against dealer 5-6
            return 'Double'
        else:  # Soft 13 (A,2) otherwise hits
            return 'Hit'

    # Check for hard totals
    if hand >= 17:  # 17 and up always stands
        return 'Stand'
    elif hand == 16 and dealer in range(2, 7):  # 16 stands against dealer 2-6, otherwise hit
        return 'Stand'
    elif hand == 16:  # 16 otherwise hits
        return 'Hit'
    elif hand == 15 and dealer in range(2, 7):  # 15 stands against dealer 2-6, otherwise hit
        return 'Stand'
    elif hand == 15:  # 15 otherwise hits
        return 'Hit'
    elif hand == 14 and dealer in range(2, 7):  # 14 stands against dealer 2-6, otherwise hit
        return 'Stand'
    elif hand == 14:  # 14 otherwise hits
        return 'Hit'
    elif hand == 13 and dealer in range(2, 7):  # 13 stands against dealer 2-6, otherwise hit
        return 'Stand'
    elif hand == 13:  # 13 otherwise hits
        return 'Hit'
    elif hand == 12 and dealer in range(4, 7):  # 12 stands against dealer 4-6, otherwise hit
        return 'Stand'
    elif hand == 12:  # 12 otherwise hits
        return 'Hit'
    elif hand == 11:  # 11 always doubles
        return 'Double'
    elif hand == 10 and dealer in range(2, 10):  # 10 doubles against dealer 2-9, otherwise hit
        return 'Double'
    elif hand == 10:  # 10 otherwise hits
        return 'Hit'
    elif hand == 9 and dealer in range(3, 7):  # 9 doubles against dealer 3-6, otherwise hit
        return 'Double'
    elif hand == 9:  # 9 otherwise hits
        return 'Hit'
    else:  # 8 always hits
        return 'Hit'


dealer = int(input('dealer: '))
a = None
player = []
while len(player)<2:
    a = int(input('Player:'))
    player.append(a)
result = blackjack(player,dealer)
print(result)
while result == 'Hit':
    a = int(input('Player:'))
    player.append(a)
    result = blackjack(player,dealer)
    print(result)
