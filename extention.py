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
        
        #headwear: iron cap (2), leather cap (1), helmet (3)
        #armor: studded leather(9), chainmail(21), scalemail(15), platemail(29)
        #shield: buckler(1), embossed leather shield(2), kite shield(4)

        self.headware = {"leather cap":1,"iron cap":2,"helmet":3}

        #self.armor = {9:{"studded leather"},21:{"chainmail"},15:{"scalemail"},29:{"platemail"}}
        #self.shield = [1,2,4]

        x = list(self.headware.keys())
        randomitem = random.choice(x)

        print(self.headware[randomitem])
        print(random.choice(self.headware))
        #self.equipment[0] = {}

        #self.equipment[0][f"{randomitem}"] = 0

        #print(equipment)
        
        #self.equipment[0][randomitem] = random.choice(self.headware)

        #self.equipment["armor"][randomitem] = random.choice(self.armor)

        #self.equipment["shield"][] = random.choice(self.shield)
        
        
        #armor = self.equipment["head"] + self.equipment["armor"] + self.equipment["shield"] + self.equipment["weapon"]
        
        #print(armor)


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