
def recharge(ammo):
    ammo = ammo + 1
    return ammo


def Shoot(ammo,player_2,player_1,  p2_lives, p1_lives):
    if ammo > 0: 
        ammo = ammo -1
        if player_2 == 'Charge':
            p2_lives = 0
        if player_1 == 'Charge':
            p1_lives = 0
    else:
        print('You have no ammo! Pick again')
    return ammo,p2_lives,p1_lives

def live_check( p2_lives, p1_lives):
    
    if  p2_lives == 0:
        print('Game over!')
        print('P1 wins!')
        return "Stop"
    if  p1_lives == 0:
        print('Game over!')
        print('P2 wins!')
        return 'stop'
def main():
    P1_amo = 0
    P2_amo = 0
    p2_lives = 1
    p1_lives = 1
    print('You will now begin 007')
    while True:

        player_1 = " "
        while player_1 != 'Charge' or player_1 != 'Shoot' or player_1 != 'Shield' or player_1 != 'Mirror':
            player_1 = input('P1 Select one of these orders: Charge, Shoot, Shield, Mirror')
            if player_1 == 'Charge' or player_1 == 'Shoot' or player_1 == 'Shield' or player_1 == 'Mirror':
                break
            else:
                print("That is not in the selection!")
        print('P1 selected',player_1)
        
        player_2 = " "
        while player_2 != 'Charge' or player_2 != 'Shoot' or player_2 != 'Shield' or player_2 != 'Mirror':
            player_2 = input('P2 Select one of these orders: Charge, Shoot, Shield, Mirror')
            if player_2 == 'Charge' or player_2 == 'Shoot' or player_2 == 'Shield' or player_2 == 'Mirror':
                break
            else:
                print("That is not in the selection!")
        print('P2 selected',player_2)

#Charging phaze       
        
        if player_1 == 'Charge':
            P1_amo =  recharge(P1_amo)
            print('Player 1 has', P1_amo, 'ammo!')
        if player_2 == 'Charge':
            P2_amo = recharge(P2_amo)
            print('Player 2 has', P2_amo, 'ammo!')
            
# Shooting phaze
        
        if player_1 == 'Shoot':
            P1_amo, p2_lives, p1_lives = Shoot(P1_amo,player_2,player_1, p2_lives, p1_lives)
            print('Player 1 has', P1_amo, 'ammo!')
        
        if player_2 == 'Shoot':
            P2_amo,p2_lives, p1_lives = Shoot(P2_amo,player_2,player_1,p2_lives, p1_lives)
            print('Player 2 has', P2_amo, 'ammo!')
            
# Check who is dead    
        
        if live_check( p2_lives, p1_lives) == 'stop':
            break
        
main()
