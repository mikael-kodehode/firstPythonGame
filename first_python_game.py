import random

class Player:                   #En klasse for player og en for enemies fordi de har different properties. Player class har 6 funksjoner
    def __init__(self, name):
        self.name = name
        self.attack = 1                                 
        self.health = 150                           #Jeg tenkte på mange ting å adde. Jeg ville adde en highscore som samla opp 
        self.defense = 10                           #enemies' health og attack som sum i en liste hvis du defeater de også presentere highscore
        self.wins = 0                               #etter gamet. Men jeg fikk ikke helt taket på hvordan jeg skal lagre informasjonen om enemy 
        self.highscore = []                         #før det endres i fighten. Så jeg droppet ideen for nå.
    
    def stab(self):
        dmg = random.randint(5, 45)
        return dmg
    def slash(self):
        dmg = random.randint(10, 30)
        return dmg
    def punch(self):
        dmg = random.randint(15, 25)
        return dmg
    def take_damage(self, i):
        dmg = (enemies[i-1].attack - self.defense)
        if (dmg < 0):
            dmg = 0
        self.health -= dmg
        if (self.health <= 0):
            input(f"{enemies[i-1].name} punches you for {dmg} damage. You died")
        else:
            input(f"{enemies[i-1].name} punches you for {dmg} damage. You have {self.health} HP left")
    def find_weapon(self):
        #add attack
        weapon = random.choice(weapons)
        self.attack = weapon["attack"]
        print(f"\nYou found a {weapon['name']}.")
        print(f"It gives you additional {weapon['attack']} multiplier to your attack. Attack-multiplier now: {self.attack}")
    def find_shield(self):
        #add defense
        shield = random.choice(shields)
        self.defense = shield["defense"]
        print(f"\nYou found a {shield['name']}.")
        print(f"It gives you additional {shield['defense']} defense. Your current defense: {self.defense}")
    
class Enemy:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.attack = random.randint(15, 60)
        self.health = random.randint(10, 200)
        self.alive = True

arnekurt = Player("Arne Kurt")
bobkaare = Player("Bob Kåre") #This is just the player I made. I would change it to user input if I spend more time. 

                                # I have used dictionaries to store information that I randomly pick out with random.choice
#dicts for weapons

battleaxe = {
"name" : "battleaxe",                                                   
    "attack": 2
}
sword = {
    "name": "sword",
    "attack": 3
}
mace = {
    "name": "mace",
    "attack": 1.5
}
#dicts for shields
wooden_shield = {
    "name": "wooden shield",
    "defense": 15
}
steel_shield = {
    "name": "steel shield",
    "defense": 25
}
carbon_shield = {
    "name": "carbon shield",
    "defense": 35
}
                                                # This is the list of dictionaries that I pick random equipment from
weapons = [battleaxe, sword, mace]
shields = [wooden_shield, steel_shield, carbon_shield]

# This randomizes an enemy and stores it in a list that I can show to the player with a simple loop. The class for enemies is showed above with player class
adjective = ["Smelly", "Dreadful", "Petulant", "Truculent", "Fatuous", "Feckless", "Antiquated", "Mundane", "Dreary", "Dysfunctional", "Dismal"]
insult = ["butt", "douche", "turd", "dingbat", "ass", "lug"]
subject = ["goblin", "gnome", "duck", "rabbit", "monkey", "creeper", "clown", "lickspittle", "chicken", "pig", "troll"]

enemies = []
def spawn():
    i = 0
    print("\nSpawned enemies:")# 0 because it looks better. You will see i+1 and i-1 many times through the code
    while (i < 10): # The reason for "i+1" is that I use index as ID, but show it without the 
        enemy = Enemy(f"{random.choice(adjective)} {random.choice(insult)} {random.choice(subject)}", i+1)
        enemies.append(enemy)
        i += 1
def print_spawn(max):
    i = 0
    while (i < max):
        print("Name", enemies[i].name)                     
        print("ID", enemies[i].id)                      
        print("Attack", enemies[i].attack)
        print("Health", enemies[i].health)
        print("Alive", enemies[i].alive)
        print(" ")
        i += 1

#---------------------------------------------------------------
#functions functions functions
#---------------------------------------------------------------
                                                # I decided to have 3 attack options that the player can choose from 
                                                # to make it seem a bit more interactive and feel less automatic.
                                                # So I stored 3 different attacks as methods, stab, slash, punch and 
                                                # returned damage that this function picks up and multiplies it with 
                                                # the attack of the player which is affected by equipment
def calculating_dmg(self):
    attack_choice = input('\nType "1" for stab (5-45 dmg) \nType "2" for slash (10-30 dmg) \nType "3" for punch (15-25 dmg)\n')
    print("----------------------------------------------------------------------------")
    if (attack_choice == "1"):
        dmg = self.stab() * (self.attack)
        return dmg
    elif ( attack_choice == "2"):
        dmg = self.slash()*(self.attack)
        return dmg
    elif (attack_choice == "3"):
        dmg = self.punch() * (self.attack)
        return dmg
    else:
        print("Invalid value")
        calculating_dmg(self)
                                                # This is used when the player wants to see their stats and when stats are shown 
                                                # for example in a fight. It just picks up player's properties in a string
def current_stats(self):
    print("\nYour stats:\n")
    print(f"Attack-multiplier: {self.attack} \nHealth: {self.health} \nDefense: {self.defense}")
                                                # This shows the enemy's stats in fight
def current_enemy_stats(i):
    print("Attack", enemies[i-1].attack)
    print("Health", enemies[i-1].health)
                                                # This is basically the biggest part of the function fight(). 
                                                # It starts with player and enemy current stats against eachother while the player 
                                                # chooses attack option. It is updated after each turn of attack.
                                                # So this saves the damage from calculate_dmg and applies it to the enemy. If the enemy
                                                # has more than 0 HP it will run again until the enemy is defeated
def player_attacking(self, i):                  # i is enemy id number. -1 because the player identifies which enemy they want to fight through
                                                # ID which is linked with index of the enemies list
    print("----------------------------------------------------------------------------")
    print(f"\n{enemies[i-1].name}:\n")
    current_enemy_stats(i)         
    current_stats(self)
    dmg = calculating_dmg(bobkaare)
    print(dmg)
    if (dmg == None):
        dmg = 0
        enemies[i-1].health -= dmg
        print("You missed")                     # This is a mechanic that I don't actually know why works. Sometimes the dmg
                                                # returns as "None" and I couldn't figure out why, so instead of fixing it I used it as a chance of missing mechanic. Pretty neat.           
    else:
        enemies[i-1].health -= dmg
        if (enemies[i-1].health > 0):
            print(f"You deal {dmg} damage. The monster's HP left: {enemies[i-1].health}")
        elif (enemies[i-1].health <= 0):
            print(f"You deal {dmg} damage which kills the monster. You defeated {enemies[i-1].name}.")
            enemies[i-1].alive = False
        else:
            input("Error player_attacking...")

                                            # Easy function that bundles two player methods, find_weapon and find_shield for easy use.The application of the equipment are done in the method itself. It uses random.choice to pick out one item from the list of weapon and shield dictionaries and extract the bonus defense or bonus attack and adds it to the player properties
def find_equipment(self):
    print("----------------------------------------------------------------------------")
    input("\nPress enter to search...")
    self.find_weapon()
    self.find_shield()
                                            # Quick function that shows stats and attacks. This is only used in the menu.
def check_stats(self):
        print(f"\n\nYour stats: \nAttack-multiplier: {self.attack} \nHealth: {self.health} \nDefense: {self.defense}")
        print(f'\nThis is your attacks: \nStab (5-45 dmg)*{self.attack} \nSlash (10-30 dmg)*{self.attack} \nPunch (15-25 dmg)*{self.attack}\n')

                                            # This function checks the updated enemy list. It will only show the enemies with the value True on self.alive so enemies they have defeated before does not show.
def check_enemies():
    i = 0
    print("\nSpawned enemies: \n")
    while (i < 10):
        if (enemies[i].alive == True):
            print("\nName", enemies[i].name)
            print("ID", enemies[i].id)
            print("Attack", enemies[i].attack)
            print("Health", enemies[i].health)
        i += 1
    print("----------------------------------------------------------------------------\n")
                                            # This function registers which enemy you want to fight. It calls check_enemies() to show them and ask for ID of which enemy to select. After the enemy is defeated the check_enemy() will not show the defeated monster and so this function will stop you from picking a dead enemy. I used try, except to change the string input to an integer. It means that it tries to convert the string to an integer and if the player inputs anything other than a number it doesn't work, so then it checks out except which tells them to try again and with the function continue it will just jump back to the start of the loop. It will finally break when it gets an integer and return that value.
def choose_enemy():
    check_enemies()
    while (True):
        enemy_id = input("Choose which enemy you want to fight by typing in their ID: \n")
        try:
            enemy_id = int(enemy_id)
        except:
            print("Invalid input, please try again: ")
            continue
        if (enemies[enemy_id-1].alive == False):
            print("This enemy is already defeated. Pick another: ")
            continue
        if (type(enemy_id) == int and enemy_id > 0 and enemy_id < 11):
            confirm = input(f"You chose number {enemy_id}. Press enter to confirm or 'n' to choose again: ")
            if (confirm == ""):
                break
            elif (confirm == "n"):
                continue
            else:
                print("Invalid input, please try again: ")
                continue
        else:
            print("Invalid input, please try again: ")
            continue
    return enemy_id
#-------------------------------------------------------
#bigger functions like menu, fight and game
#-------------------------------------------------------
                                                    # Start_menu() is only used before any fight and it's the menu that will send the player to the start_menu if the wins property is 0. Overview over stats by calling check_stats() and asking for an action. Either check_enemies() or start fighting.
def start_menu(self):
    check_stats(bobkaare)
    print("----------------------------------------------------------------------------\n")
    action = input("\nYour goal is to defeat 5 enemies out of 10 spawned. You can choose yourself which order you want to fight, but you don't get any heals between fights so choose carefully. However you can look for better equipment between fights if you wish. \n\n\nPress 'x' to check enemies' stats: \nPress 'f' to fight: \n")

    if (action == "x"):
        print("----------------------------------------------------------------------------\n")
        check_enemies()
        input("Press enter to go back to menu")
        start_menu(self)
    elif (action == "f"):
        fight(self)
    else:
        print("Invalid input, please try again: \n\n")
        start_menu(self)
                                            # This function is called when the player has beaten every monster in the list. It congratulates you and sends you further to the game_over() which I'll cover later
def victory(self):
    print("You won the game! Congratulations and thank you.")
    game_over(self)
                                            # Main menu. The menu shown after the first fight and through. First thing it checks if the player has won. If not, continues to ask what the player wants to do. Calls find_equipment(), check_enemies(), fight() and check_stats(). I usually leave else to print "error" as then I know where it went wrong and it restricts that what happens happens for the right reason. 
def menu(self):
    if (self.wins == 5):
        victory(self)
    elif (self.wins > 0):
        print("----------------------------------------------------------------------------\n")
        action = input("Congratulations on your victory! What do you want to do? \nPress 'e' to find new equipment: \nPress 'x' to check enemies: \nPress 'a' to show your stats: \nPress 'f' to fight: \n\n")
        if (action == "e" ):
            find_equipment(bobkaare)
            input("Press enter to go back to menu")
            menu(self)
        elif (action == "x"):
            print("----------------------------------------------------------------------------\n")
            check_enemies()
            input("Press enter to go back to menu")
            menu(self)
        elif (action == "f"):
            fight(self)
        elif (action == "a"):
            print("----------------------------------------------------------------------------\n")
            check_stats(bobkaare)
            input("Press enter to go back to menu")
            menu(self)
        else:
            print("Invalid input, please try again: ")
            menu(self)
    elif(self.wins == 0):
        start_menu(self)
    else:
        print("Error menu...")
        menu(self)
                                        # This function is the overlord that controls the fights. This calls choose_enemy and stores the returned ID to pick out the enemy. Then it starts a while True loop based on each opponents' health. Both opponents gets to attack before it ends, which means they can die while also killing the enemy. An if statement decides when the loop ends and in which favor. After the loop another if statement either sends you to game_over() or menu().
def fight(self):
    check_enemies()
    id = choose_enemy()
    input(f"\nYou fight {enemies[id-1].name}")
    while (True):
        player_attacking(self, id)
        self.take_damage(id)
        if (self.health <= 0):
            input("Game over")
            break
        elif (enemies[id-1].health <= 0):
            self.wins += 1
            print("Wins: ", self.wins)
            break
        else:
            continue
    if (self.health > 0):
        menu(self)
    elif (self.health <= 0):
        game_over(self)
    else:
        input("Error after fight")

                                    # Game_over() doesn't mean that the player lost, it's the function that is called when either player is dead or after a victory. It asks if they want to play again or exit the game.

def game_over(self):
    print(f"You defeated {self.wins} monsters. Well done!")
    play_again = input("Press 'p' to play again. Press enter to quit: ")
    if (play_again == "p"):
        self.wins = 0
        game(self)
    else:
        input("Thank you for playing!")
                                    # This is the toastbread with all the ingredients in it. Just wraps the game up in one easy function.
def game(self):
    input("Press enter to play...")
    spawn()
    menu(self)

game(bobkaare)
