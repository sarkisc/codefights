import copy

def allianceHelp(t, allianceSize):

    time = copy.deepcopy(t)
    
    numBoosts = 0
    x = int(0.1*t)
    y = min(10, allianceSize)
    z = max(x,60)

    
    while numBoosts < y:

        if time - x < 0 and time - 60 < 0:
            return 0
        else:
            time -= z
            
        numBoosts += 1
        
    return max(0,time)


# kind of lame
def allianceVersusMonster(healthPoints, attackDamage):
    
    #if there's only one warrior, he attacks every time
    
    if len(healthPoints) == 2:
        if healthPoints[0]//attackDamage[1] <= healthPoints[1]//attackDamage[0]:
            return 1
        return 0
    
    # pick the warrior with the greatest health
    # attack monster for as many turns until one more monster attack will kill warrior
    # switch to warrior of next greatest health and repeat the process
    
    alliance = []
    
    for i in range(1,len(healthPoints)):
        alliance.append([healthPoints[i], attackDamage[i]])
    
    alliance.sort(key = lambda stats: stats[1], reverse = True)
    alliance.sort(key = lambda stats: stats[0], reverse = True)
    
    print(alliance)
    
    monsterHealth = healthPoints[0]
    monsterAttack = attackDamage[0]
    
    allianceHealth = [warrior[0] for warrior in alliance]
    allianceAttack = [warrior[1] for warrior in alliance]
    
    # attack: warrior at index i attacks the monster
    # subtract attackDamage of warrior at index i from monsterHealth
    # if monster is still alive, monster counter-attacks warrior at index i
    # else if monster is killed, no counter attack
    def attack(i):
        nonlocal monsterHealth
        monsterHealth -= allianceAttack[i]
        if monsterHealth > 0:
            allianceHealth[i] -= monsterAttack
            if allianceHealth[i] <= 0:
                allianceHealth.pop(i)
                allianceAttack.pop(i)
    
    
    # returns then index of the chosen warrior
    # if no warrior is chosen, return the index of the first warrior (0)
    def chooseWarrior():
        
        if monsterHealth - allianceAttack[0] <= 0:
                return 0
            
        i = 0
        al = len(allianceHealth)
        while i < al:
            if allianceHealth[i] - monsterAttack > 0:
                return i
            i += 1
        
        return 0
    
    
    # must attack with the warrior that will not die
    # if all will die, go with the one with greatest attack (the first one)
    # if a warrior dies, remove it from the alliance
    
    while monsterHealth > 0 and allianceHealth != []:
        
        warrior = chooseWarrior()
        attack(warrior)  
    
    return len(allianceHealth)