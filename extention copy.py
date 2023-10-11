import random
npcs = []
npchp = []
npcwealth = []


class NPC:
    stats = { 'str' : 0, 'int' : 0, 'pie' : 0, 'agi' : 0, 'stm' : 0, 'cha' : 0 }
    equipment = {}
    level = 0
    hp = 0
    gold = 0
    silver = 0
    copper = 0
    wealth = 0
    armor = 0


    randlist = [1,1,1,1,2,2,2,3,3,4]

    def randItem(self,options):
        x = list(options.keys())
        itemName = random.choice(x)
        number = options[itemName]

        return {itemName:number}
    
    def __init__(self,z):

        for i in self.stats:
            rand1 = random.randint(1,6)
            rand2= random.randint(1,6)
            rand3 = random.randint(1,6)
            self.stats[i] = rand1+rand2+rand3

        self.level = self.randlist[random.randint(0,9)]

        self.hp = (random.randint(1,10)*self.level)
        
        if random.randint(1,100) < 30:
            self.gold = random.randint(0,6)

        if random.randint(1,100) < 50:
            self.silver = random.randint(3,12)

        if self.gold == 0:
            if random.randint(1,100) < 75:
                self.copper = random.randint(4,20)

        self.wealth = ( (self.gold*100)+(self.silver*10)+self.copper )
    

        self.headwear = {"leather cap":1,"iron cap":2,"helmet":3}
        self.armor = {"studded leather":9,"chainmail":21,"scalemail":15,"platemail":29}
        self.shield = {"buckler":1,"embossed leather shield":2,"kite shield":4}


        self.equipment = {}
        self.equipment[0] = self.randItem(self.headwear)
        self.equipment[1] = self.randItem(self.armor)
        self.equipment[2] = self.randItem(self.shield)
       


        print(f"\033[1;47;40m======================= \033[0m")
        print(f"\033[1;47;40mStats: \033[0m")
        print(f"\033[1;31;40mHP \033[0m: {self.hp}")
        print(f"\033[1;35;40mLevel \033[0m: {self.level}")
        print(f"\033[1;33;40mGold \033[0m: {self.gold}")
        print(f"\033[1;47;40mSilver \033[0m: {self.silver}")
        print(f"\033[1;32;40mCopper \033[0m: {self.copper}")
        print(f"\033[1;36;40mWealth \033[0m: {self.wealth}")
        print(f"\033[1;34;40mArmor Value \033[0m: {(list(self.equipment[0].values()))[0]+(list(self.equipment[1].values()))[0]+(list(self.equipment[2].values()))[0]}")

        print(f"\033[1;47;40m\nArmor: \033[0m")
        
        print(f"\033[1;30;40mHeadwear \033[0m: {(list(self.equipment[0].keys()))[0]}")
        print(f"\033[1;30;40mChestplate \033[0m: {(list(self.equipment[1].keys()))[0]}")
        print(f"\033[1;30;40mShield \033[0m: {(list(self.equipment[2].keys()))[0]}")
        print(f"\033[1;47;40m======================= \033[0m")

        

        print("\n")
        return


lvl1 = 0 
lvl2 = 0
lvl3 = 0
lvl4 = 0

for i in range(0,100):
    npcs.append(NPC(i))
    npchp.append(npcs[i].hp)
    npcwealth.append(npcs[i].wealth)
    lvl = npcs[i].level
    
    if lvl == 1:
        lvl1+=1

    if lvl == 2:
        lvl2+=1

    if lvl == 3:
        lvl3+=1

    if lvl == 4:
        lvl4+=1


def mean(dataList):
    total = 0
    
    for i in dataList:
        total += i

    final = total/len(dataList)
    return final

def sd(dL):
    average = mean(dL)
    difference = []
    squares = []
    num = 0

    for i in dL:
        difference.append(i-average)
        
    for i in difference:
        squares.append(i**2)

    for i in squares:
        num += i

    return round(((num/len(dL))**0.5),2)



print(f"The mean is of the hp of the npcs is {mean(npchp)} and the standard deviation is {sd(npchp)}")
print(f"The mean is of the wealth of the npcs is {mean(npcwealth)} and the standard deviation is {sd(npcwealth)}")
print(f"There are {lvl1} level 1's, {lvl2} level 2's, {lvl3} level 3's, {lvl4} level 4's")