from blackjack import blackjack

a = int(input('Input your first hand: '))
b = int(input('Input your second hand: '))
c = int(input('Input dealer hand: '))

player = [a,b]
dealer = c
print(blackjack(player,dealer))
