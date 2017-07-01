import random


class Team(object):
    def __init__(self):
        self._team = []
        self._teamnames = []     #so i have a list of the names of evryone on team

    def __str__(self):
        teamstring = ""
        for i in self._team:
            teamstring += i.show_name() + ", "
        teamstring = teamstring[:-2]
        print(len(self._team))
        return teamstring

    def add(self,char):
        self._team.append(char)
        self._teamnames.append(char.show_name())


    def remove(self,char):
        #self._teamnames.remove(self._team.index(char))
        del self._teamnames[self._team.index(char)]
        self._team.remove(char)

    #def remove_names(self,char):
    #    self._teamnames.remove(self._team.index(char))


    def show_team(self):
        return self._team

    def show_teamnames(self):
        return self._teamnames


    def team_pos(self):
        poslist = []
        for i in self._team:
            poslist.append(i.show_pos())
        return poslist


    def team_loss(self):
        return len(self._team) == 0


class Character_Overview(object):     #may need super class that just takes up space
                                        # something for rocks, trees, cars, etc.
    def __init__(self,name,hp,att,defe,ran,mob,team1,team2):
        self._name = name
        self._hp = hp
        self._att = att
        self._defe = defe
        self._pos = None
        self._mob = mob
        self._ran = ran
        self._pos = self.relocate(team1,team2)
        self._myteam = team1

    def __str__(self):
        pass

    def move(self):
        pass

    def attack(self):
        pass

    def is_attack_inrange(self):
        pass

    def defend(self):
        pass

    def recharge(self):
        pass

    def heal(self):
        pass

    def show_pos(self):
        pass

    def show_hp(self):
        pass

    def show_name(self):
        pass
    def relocate(self,team1,team2):    #not necessary
        pass

    def die(self):
        pass

class Character(Character_Overview):
    #put something here if you want all instances to have the same
    #version of this
    def __init__(self,name,hp,att,defe,ran,mob,team1,team2):
        super(Character,self).__init__(name,hp,att,defe,ran,mob,team1,team2)
         #attack and range will be removed bcuz each char's attack will have diff stats

                                                    #teams begin close together

    def __str__(self):
        return self._name

    def move(self,team1,team2):
        moveran = []
        upperran = self._pos + self._mob
        lowerran = self._pos - self._mob
        print(team1)
        print(team2)

        team1pos = team1.team_pos()
        team2pos = team2.team_pos()
        for i in range(lowerran,upperran+1,1):
            if i not in team1pos and i not in team2pos:
                    moveran.append(i)
        print(moveran)
        movechoice = raw_input("Enter the number you want to move to: ")
        if movechoice == "b":
            return False
        movechoice = int(movechoice)
        while movechoice not in moveran:
            movechoice = input("Invalid choice choose again: ")
            movechoice = int(movechoice)
        self._pos = movechoice
        return True


    def relocate(self,team1,team2):
        self._pos = random.randint(-5,5)
        #self._pos = 4
        while self._pos in team1.team_pos() or self._pos in team2.team_pos():
            self._pos = random.randint(-5,5)
            #self._pos = 5
        return self._pos

    def is_attack_inrange(self,other):     #each attack will have different
                                    #accuracy, criticality, and range
        upperran = self._pos + self._ran      #super class does not need explicit attack
        lowerran = self._pos - self._ran     # sub classes will have that.
        if (self._pos < other.show_pos() <= upperran
            or lowerran <= other.show_pos() < self._pos):
            return True
        else:                           #sub class attack will call this func
            return False               #if returned true they will continue with attack
                                        #other wise player can choose diff att or diff command
    def attack(self,other):
        if self.is_attack_inrange(other):    #will soon be turned into virtual function
            print("attack successful")
            other.damage(self._att)


    def defend(self):                       #will improve later
        self._hp += self._defe/2

    def heal(self):
        self._hp += 30

    def show_pos(self):
        return self._pos

    def show_hp(self):
        return self._hp

    def damage(self,other):         #need one for heal
        self._hp-=other
        if self._hp < 0:
            self._hp = 0
            self.die()
                                        #functions for damange
                                        #and heal hp
    def show_name(self):
        return self._name

    def die(self):
        for i in self._myteam.show_team():
            if i.show_name() == self._name:
                self._myteam.remove(i)

'''
def main():
    a = Team()
    b = Team()
    Al = Character("Al",100,120,10,1,5,a,b)
    a.add(Al)
    Bob = Character("Bob",100,10,25,2,1,b,a)
    b.add(Bob)


    #Chris = Character("Chris",100, 20, 20, 1, 1,a,b)
    #a.add(Chris)
    #David = Character("David",100, 15, 25, 3, 6,a,b)
    #b.add(David)



    Al.attack(Bob)

main()
'''
