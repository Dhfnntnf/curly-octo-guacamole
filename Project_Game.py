import random
Flag = True
class food:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
class weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

#Titles were supposed to give you extra buffs, but I got so depressed making it i gave up        
#class title:
#    def __init__(self, name, dmg, hp):
#        self.name = name
#        self.dmg = dmg
#        self.hp = hp
        
class players():
    def __init__(self, name , hp , damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.hp_edit = hp
        self.dmg_edit = damage
        self.weapon = None
        self.xp  = 0
        self.lvl = 1#(lvl system still wip)
        #self.pp = (50 + 100/hp + 100/damage) #Incomplete idea for durability,
                                              #Either less durable for balancing or more durable for realism
        self.notch = False
        self.spear = False
        self.gdklr = False
        self.shear = False
        self.bgshr = False
        self.Achievements = []
        self.titles = []#Titles that maybe grant extra dmg/hp against specific enemies
        #OH MY DAYS BRUH
        self.killcount = 0
        self.gobslay = 0
        self.gap = 1 #Idea for a (de)buff system
        #self.cur_food = []
        #self.cur_weapon = []#WIP idea for inventory system
        

    def attack(self, target):
        if target.hp < 0:
            print('Target is already dead bro')
        else:
            temp = self.hp
            target.hp -= self.damage
            self.hp -= target.damage
            self.xp += target.xp
            self.lvl = self.xp // 150
            both_dead = target.hp <= 0 and self.hp <= 0 
            print(f"You attacked {target.name}, {target.name}'s health is {target.hp}")
            print(f'{target.name} attacked you, your hp is {self.hp}')
            if target.hp <= 0:
                if self.hp == 1:
                    print("You've obtained the title: Unkillable")
                    self.titles.append('Unkillable')
                Endead = True
                if self.weapon == 'Kindness':
                    if 'Killed with kindness' not in self.Achievements:
                        print("Achievement get!:Kill em with kindness")
                        self.Achievements.append('Killed with kindness')
                if self.weapon == 'Orphan_Obliterator':
                    if 'Dropkicked a child' not in self.Achievements:
                        print('Achievement get!: Officer, I dropkicked that child in SELF DEFENSE')
                        self.Achievements.append('Dropkicked a child')
                if target.name == 'Goblin':
                    self.gobslay += 1
                    if self.gobslay == 100:
                        print("You've obtained the title: Goblin Slayer")
                        self.titles.append('Goblin Slayer')
                if target.name == 'Horror_from_the_hills' or target.name == 'Eater_of_dreams':
                    print('Achievement get!:Winner')
                    self.Achievements.append('Winner')
                    Flag = False
                    print('Sidenote:If this actually happened , take a screenshot and send me, thks :)')
                
                if target.name == 'Dragon':
                    if 'Dragon slayer' not in self.Achievements:
                        print('Achievement get!:One who slew a dragon')
                        self.Achievements.append('Dragon slayer')
                target.dead()
                self.killcount += 1
                if self.killcount == 500:
                    print('Achievement get!:Mosquito ahh killcount')
                    self.Achievements.append('Mosquito ahh killcount')
                    print("You've obtained the title: Baba Yaga")
                    self.titles.append('Baba_Yaga')
            if both_dead == True:
                print("You died but took it down with you, second chances don't come easy")
                if 'Not your time' not in self.Achievements:
                    self.Achievements.append('Not your time')
                    print('Achievement get!:Not your time')
                    print("You've obtained the title:Living legend")
                    self.titles.append('Living_legend')
                self.hp = 150
            if self.hp <= 0:
                Sedead = True
                print('You have died, git gud')
        
            
            
    def eat(self, food):
        if self.hp + food.value < 0:
            print('You have died,git gud')
            print('In theory, you can never lose with perfect play')
            
        if food.name == 'Nectar':
            print('The Nectar has stirred up somthing within you')
            if 'Ambrosia' not in self.Achievements:
                print('Achievement get!:Food of the gods')
                self.Achievements.append('Ambrosia')
            self.notch = True
        if food.name == 'Cursed milk':
            print('You drink the milk. What comes out should never be spoken of again')
        if food.name == 'Cursed pickle':
            print('Why do you eat something labelled cursed?')
        
        self.hp += (food.value)
        
        if self.gdklr == False:
            if self.hp >200:
                self.hp = 200
        
        
    def use_weapon(self, weapon):
        self.damage = weapon.damage
        
        if weapon.name == 'Spear_of_the_non_believer':
            self.spear = True
            if 'Godkilling spear' not in self.Achievements:
                print('Achievement get!: The godless lance')
                self.Achievements.append('Godkilling spear')
        elif weapon.name == 'Kindness':
            print('You feel like donating money to me(Insert shamless plug)')
        elif weapon.name == 'Toothpick':
            print("You are now using Toothpick, legendary pickaxe ")
        elif weapon.name ==  'Bees':
            print("You are now wielding bees. This is fine.")
        elif weapon.name == 'Power_V_Bow':
            print("You are using a Power V Bow, formerly wielded by the skeleton king.")
        elif weapon.name == 'Shears':
            print('You are using some shears?')
            if 'Shears' not in self.Achievements:
                print('Achievement get!:What...')
                self.Achievements.append('Shears')
            self.shear = True
            if self.shear == True and self.bgshr == True:
                if 'Gardener' not in self.Achievements:
                    print('Achievement get!:Gardener')
                    self.Achievements.append('Gardener')
        elif weapon.name == 'Slightly_Bigger_Shears':
            print("You are using Slightly Bigger Shears. Good for... gardening?")
            self.bgshr = True
            if 'Big shears' not in self.Achievements:
                print('Achievement get!:Bigger shears?')
                self.Achievements.append('Big shears')

            if self.bgshr == True and self.shear == True:
                if 'Gardener' not in self.Achievements:
                    print('Achievement get!:Gardener')
                    self.Achievements.append('Gardener')
        elif weapon.name == 'Orphan_Obliterator':
            if 'Post-birth abortion' not in self.Achievements:
                print("Achievement get!:Post-birth abortion") 
                self.Achievements.append('Post-birth abortion')
        else:
            print(f'{weapon.name} equipped')
        self.weapon = weapon.name    
        
    def godkiller(self):
        if self.spear == True and self.notch == True and self.gdklr == False:
            print('Smite the outer gods')
            self.gdklr = True
            if 'Godkiller' not in self.Achievements:
                print('Achievement get!:Godkiller')
                self.Achievements.append('Godkiller')
            self.damage = (10**10)
            self.hp = (10**10)
        elif self.gdklr == True:
            self.gdklr = False
            print('You are no longer a godkiller')
        else:
            print('Fools rush in where angels fear to tread')
class enemy():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.xp = damage + hp
        
    def dead(self):
        lst = [('Forgiveness is between them and god, it is up to you to arrange the meeting' ),
               ('It was at this moment that he knew, he fked up'), ('Hickory dickory dock, the mouse pulled out a glock'),
               ('Kill one man:Murderer, Kill a million:Conqueror, Kill them all:God'),
               ('I identify as a threat, my pronouns are fk around/find out'), ('Kirby has found your sin unforgivable'),
               ('HANS GET ZE FLAMMENWERFER'), ('HANS SCREW ZE FLAMMENWERFER GET SCHWERER GUSTAV'), ('Stay strapped or get clapped'),
               ('You talking some mad sh*t for someone in crusading distance'), ('Your free trial of living has ended'),
               ('Death is no disgrace'), ('Now I am become death, the destroyer of worlds'), ('Skill issue') , ('Lmao bozo')]    
        print('Congratulations, you killed an enemy')
        print(f'Death message:{random.choice(lst)}')  
        
#Still in progress    
def found_enemy():  # Completed for now
    enemies = [
        enemy('Goblin', 10, 10),
        enemy('Mage', 20, 20),
        enemy('Golem', 100, 15),
        enemy('Archmage', 50, 60),
        enemy('Archangel', 150, 100),
        enemy('Dragon', 200, 150),
        enemy('Eater of dreams', 100000, 10000),
        enemy('Horror from the hills', 500000, 500000)
    ]

    weights = [20, 20, 20, 20, 20, 10, 1, 1]
    chosen = random.choices(enemies, weights=weights, k=1)[0]
    if chosen.name == 'Horror from the hills':
        print("Detecting a Lovecraft class entity in the region. Are you certain whatever you're doing is worth it?")
        if 'Lovecraft class sighted!' not in p1.Achievements:
            print('Achievement get!: One who saw a lovecraft class entity')
            p1.Achievements.append('Lovecraft class sighted!')
    elif chosen.name == 'Eater of dreams':
        print('Detecting a pseudo-lovecraft class lifeform. Assessment: Extreme threat - Run and you might just survive')
        if 'Pseudo-Lovecraft class sighted!' not in p1.Achievements:
            print('Achievement get!: One who saw a pseudo-lovecraft class entity')
            p1.Achievements.append('Pseudo-Lovecraft class sighted!')
    elif chosen.name == 'Dragon':
        print("A dragon has appeared. Good luck, you'll need it")
    elif chosen.name == 'Archangel':
        print('An archangel has appeared.')
    elif chosen.name == 'Archmage':
        print('An archmage has appeared')
    elif chosen.name == 'Golem':
        print('A golem has appeared')
    elif chosen.name == 'Mage':
        print('A mage has appeared')
    elif chosen.name == 'Goblin':
        print("A goblin has appeared")

    return chosen
def found_food():
    foods = [
        food('Apple', 5),
        food('Bread', 10),
        food('Cooked_Beef', 20),
        food('Mysterious_Gloop', 50),
        food('Raw_Potato', -5),
        food('Cursed_Pickle', -30),
        food('Emotional_support', 100),
        food('Overcooked_Lasagna', 2),
        food('Under_cooked_Chicken', -20),
        food('Ice_Cream_of_Feelings', 35),
        food('Cursed_Milk', -50),
        food('Grandma’s_Unknown_Stew', 200),
        food('Nectar', 1000)
    ]
    weights = [50, 50, 40, 30, 30, 20, 25, 25, 25, 20, 15, 2, 1]

    result = random.choices(foods, weights=weights, k=1)[0]
    name = result.name
    if name == 'Nectar':
        print("What's this now, Nectar?")
    elif name == 'Grandma’s_Unknown_Stew':
        print("You found Grandma’s Unknown Stew. Smells like memories and mystery.")
    elif name == 'Raw_Potato':
        print("You trip and find a raw potato. Rotton. Cold. Sad. Just like you")
    elif name == 'Cursed_Milk':
        print("You found Cursed Milk. It smells like despair.")
    elif name == 'Under_cooked_Chicken':
        print("Under-cooked Chicken...Salmonella isn't real.")
    elif name == 'Cursed_Pickle':
        print("A Cursed Pickle rolls toward you. You shouldn't eat it.")
    elif name == 'Mysterious_Gloop':
        print("You found Mysterious Gloop. It jiggles ominously.")
    elif name == 'Ice_Cream_of_Feelings':
        print("You found Ice Cream of Feelings. It tastes just like the day your father went to get milk.")
    elif name == 'Emotional_support':
        print("As opposed to emotional damage?")
    elif name == 'Cooked_Beef':
        print("Someone tossed you a cooked beef. Yummy :).")
    elif name == 'Overcooked_Lasagna':
        print("You discovered a slightly overcooked lasagna. It's... fine.")

    print(f"You obtained: {result.name}")
    return result

    
    return result
def found_weapon():
    weapons = [
        weapon('Kindness', 10),
        weapon('Iron_Sword', 30),
        weapon('Diamond_Sword', 40),
        weapon('Iron_Axe', 35),
        weapon('Diamond_Axe', 45),
        weapon('Toothpick', 50),
        weapon('Bees', 60),
        weapon('Shears', 70),
        weapon('Power_V_Bow', 125),
        weapon('Slightly_Bigger_Shears', 300),
        weapon('Orphan_Obliterator', 500),
        weapon('Spear_of_the_non_believer', 10**5)
    ]
    weights = [15, 25, 20, 20, 20, 15, 10, 10, 8, 5, 3, 1]

    result = random.choices(weapons, weights=weights, k=1)[0]

    print(f"You obtained: {result.name} (Damage: {result.damage})")
    return result
#Used for testing purposes
def master_event(event_type, event_name):
    if event_type == 'enemy':
        enemy_map = {
            'Goblin': enemy('Goblin', 10, 10),
            'Mage': enemy('Mage', 20, 20),
            'Golem': enemy('Golem', 100, 15),
            'Archmage': enemy('Archmage', 50, 60),
            'Archangel': enemy('Archangel', 150, 100),
            'Dragon': enemy('Dragon', 200, 150),
            'Eater_of_dreams': enemy('Eater_of_dreams', 100000, 10000),
            'Horror_from_the_hills': enemy('Horror_from_the_hills', 500000, 500000),
        }
        return enemy_map.get(event_name, None)
    elif event_type == 'food':
        food_map = {
            'Apple': food('Apple', 5),
            'Bread': food('Bread', 10),
            'Cooked_Beef': food('Cooked_Beef', 20),
            'Mysterious_Gloop': food('Mysterious_Gloop', 50),
            'Raw_Potato': food('Raw_Potato', -5),
            'Cursed_Pickle': food('Cursed_Pickle', -30),
            'Emotional_Support': food('Emotional_Support', 100),
            'Overcooked_Lasagna': food('Overcooked_Lasagna', 2),
            'Under_cooked_Chicken': food('Under_cooked_Chicken', -20),
            'Ice_Cream_of_Feelings': food('Ice_Cream_of_Feelings', 35),
            'Cursed_Milk': food('Cursed_Milk', -50),
            'Grandmas_Unknown_Stew': food('Grandmas_Unknown_Stew', 200),
            'Nectar': food('Nectar', 1000),
            'Ancient_Yogurt_Sentient': food('Ancient_Yogurt_Sentient', -100),
        }
        return food_map.get(event_name, None)
    elif event_type == 'weapon':
        weapon_map = {
            f"{p1.name}_PP": weapon(f"{p1.name}_PP", 1),
            'Kindness': weapon('Kindness', 10),
            'Iron_Sword': weapon('Iron_Sword', 30),
            'Diamond_Sword': weapon('Diamond_Sword', 40),
            'Iron_Axe': weapon('Iron_Axe', 35),
            'Diamond_Axe': weapon('Diamond_Axe', 45),
            'Toothpick': weapon('Toothpick', 50),
            'Bees': weapon('Bees', 60),
            'Shears': weapon('Shears', 70),
            'Power_V_Bow': weapon('Power_V_Bow', 125),
            'Slightly_Bigger_Shears': weapon('Slightly_Bigger_Shears', 300),
            'Orphan_Obliterator': weapon('Orphan_Obliterator', 500),
            'Spear_of_the_non_believer': weapon('Spear_of_the_non_believer', 100000),
        }
        return weapon_map.get(event_name, None)
    else:
        print("Unknown event")
# Actual game
name = input('Enter your name: ')
p1 = players(name , 100 , 20)
current_enemy = False
current_food = False
current_weapon = False
current_title = None
while p1.hp > 0:
    if 'Winner' in p1.Achievements:
        break
    n = input('''1: Explore, 2: Attack enemy, 3: Eat Food, 
4: Equip weapon 5: Flee from enemy 6: Check status 7:Change title 8:Godkiller mode
9: Quit 10:Run event \n''')
    if n.isdigit() == False or ((1<= int(n) <=10) == False):
        print('Enter a digit from 1 to 10')
        continue
    option = int(n)
    Endead = False
    Sedead = False
    if option == 1 and current_enemy == False:
        event = random.randint(1,3) #you adjust the probability of meeting an enemy vs getting helpful items with these numbers
        if event == 1:
            current_enemy = found_enemy()
        elif event == 2:
            current_food = found_food()
        elif event == 3:
            current_weapon = found_weapon()

    elif option == 1:
        print("The enemy is preventing you from exploring")
    elif option == 2:
        if current_enemy == False:
            print("No enemy around!")
            
            continue
        p1.attack(current_enemy)
        if current_enemy.hp <= 0:
            current_enemy = False
    elif option == 3:
        if current_food == False:
            print("No food on hand!(Go and starve fatty)")
            continue
        print(f"You had some {current_food.name.lower().replace('_',' ')}")
        if current_food.value > 0:
            print('You feel rejuvenated')
        else:
            print('You have a stomachache')
        p1.eat(current_food)
        current_food = False
    elif option == 4:
        if current_weapon == False:
            print("No weapon around!")
            continue
        p1.use_weapon(current_weapon)
        print("You are now using {} with damage: {}".format(current_weapon.name.replace('_',' '), (current_weapon.damage)))
        current_weapon = False
    
    elif option == 5:
        if current_enemy != False:
            print('You successfully escaped from the enemy!')
            current_enemy = False #Run away from your problems
        else:
            print('What are you even running from bro')
#        if random.randint(1,6) >= 5:
#            print("You have successfully escaped from the enemy!")
#            current_enemy = False
#        else:
#            print("You failed to flee and the enemy engaged you!")
#            p1.attack(current_enemy)
    elif option == 6:
        if p1.gdklr == True:
            print(f'{p1.name} the godkiller')
        elif current_title != None:
            print(f'{p1.name} the {current_title},lvl:{p1.lvl}')
        else:
            print(f'Player:{p1.name},lvl:{p1.lvl}')
            
        if p1.gdklr == False:
            
            print("hp: {}/200 damage: {}".format(p1.hp, p1.damage))
        else:
            print("hp: {} damage: {}".format(p1.hp, p1.damage))
        print(f'Your achievements are : {p1.Achievements}')
        print(f'Your titles are :{p1.titles}')
        print(f'You are using {p1.weapon}')
        if current_enemy != False:
            print(f'You are now fighting a {current_enemy.name}')
        
    elif option == 7:
        if p1.titles == [] and p1.lvl > 31:
            print('You have no titles, would you like to create some?')
            s = input('Y/N ')
            if s == 'Y':
                current_title = input('Enter your title: ')
                p1.titles.append(current_title)
            else:
                continue
            
        else:
            print(f'Your titles are {p1.titles}')
            current= input('Which title would you like to use? ')
            if current.lower() == 'none':
                current_title = None
            elif (current not in p1.titles):
                print('Unknown title')
                continue
            else:
                current_title = current

    elif option == 8:
        p1.godkiller()
    elif option == 9:
        break
    elif option == 10:
        n = input('What is the answer to life, the universe, and everything? ')
        if n != '42':
            print('Wrong password')
            continue
        print('Access granted')
        event_type = input('Event type?(Food,Enemy,Weapon,Title):').strip().lower()
        if event_type not in ['food','enemy','weapon','title']:
            print('No such event')
            continue
        event_name = input('Enter the name as seen in the quick ref guide, with underscores and proper capitalisation ')
        if event_type == 'title':
            if event_name not in p1.titles:
                p1.titles.append(event_name)
            continue
            
        
        event = master_event(event_type , event_name)
        if event == None:
            print('No such event')
        elif event_type == 'enemy':
            current_enemy = event
            event_name = event_name.replace('_' , " ")
            print(f"Enemy '{event_name}' has appeared!")
            if event_name =='Horror from the hills':
                print("Detecting a Lovecraft class entity in the region. Are you certain whatever you're doing is worth it?")
                if 'Lovecraft class sighted!' not in p1.Achievements:
                    print('Achievement get!:One who saw a Lovecraft class entity')
                    p1.Achievements.append('Lovecraft class sighted!')
            elif event_name == 'Eater of dreams':
                print('Detecting a pseudo-lovecraft class lifeform.Assessment: Extreme threat - Run and you might just survive')
                if 'Pseudo-Lovecraft class sighted!' not in p1.Achievements:
                    print('Achievement get!:One who saw a Pseudo-Lovecraft class entity')
                    p1.Achievements.append('Pseudo-Lovecraft class sighted!')
        elif event_type == 'food':
            current_food = event
            event_name = event_name.replace('_' , " ")
            print(f"You have received {event_name}")
        elif event_type == 'weapon':
            current_weapon = event
            event_name = event_name.replace('_' , " ")
            print(f"You have received {event_name}")
        
        else:
            print('BRUH')
            continue
    
print("Game over")
        

        
        


