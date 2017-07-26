from battleSystem import *


def main():
	#cool opening animations
	#logo
	#character choosing screen
	#location screen
	print("Creating Team 1")
	a = Team()                                   #must add chars to teams right after being created
	print("Creating Team 2")
	b = Team()                                   #must put their team name in the before the name of the other team

	               #name,hp,att,focus,ran,mob,team1,team2

	Al = Character("Al",100,70,0,1,10,a,b)    #the stronger the attack the more likely it hits
	a.add(Al)
	Bob = Character("Bob",100,80,0,2,10,b,a)
	b.add(Bob)
	Chris = Character("Chris",100, 50, 0, 1, 10,a,b)
	a.add(Chris)
	David = Character("David",100, 30, 0, 3, 10,b,a)
	b.add(David)



	battleSystem(a,b)


	#end battle shown and victory picture













main()
