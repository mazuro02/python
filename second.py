import random
order_list = list(range(0, 3))
choose_computer = random.choice(order_list)
hit = False
tryagain = 0
while not hit:
    player = int(input('Seu Palpite: '))
    tryagain += 1
    if player == choose_computer:
        hit = True
print('Você acertou! Com {} tentativas'.format(tryagain))
