from battleSystem import *


def main():
	#cool opening animations
	#logo
	#character choosing screen
	#location screen

	a = Team()                                   #must add chars to teams right after being created
	b = Team()                                   #must put their team name in the before the name of the other team

	#name,hp,att,defe,ran,mob,team1,team2

	Al = Character("Al",100,120,10,1,10,a,b)
	a.add(Al)
	Bob = Character("Bob",100,100,25,2,10,b,a)
	b.add(Bob)
	Chris = Character("Chris",100, 120, 20, 1, 10,a,b)
	a.add(Chris)
	David = Character("David",100, 150, 25, 3, 10,b,a)
	b.add(David)



	battleSystem(a,b)


	#end battle shown and victory picture













main()
