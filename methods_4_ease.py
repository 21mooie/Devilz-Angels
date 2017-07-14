from classes import *



def string_to_char(charselect,team):
	for i in team.show_team():                           #make function to switch b/w string & object
		if i.show_name() == charselect:
					char = i
	return char


#switch_turns
def turn_status(turnf,turn,oppf,opp):
	print(turnf + " it is your turn")
	for i in turn.show_team():
		print(i.show_name() + " health: " + str(i.show_hp()))
		print(i.show_name() + " position: " + str(i.show_pos()))
	print('\n')
	print("This is " + oppf)
	for j in opp.show_team():
		print(j.show_name() + " health: " + str(j.show_hp()))
		print(j.show_name() + " position: " + str(j.show_pos()))


def back():
	return True

def switch(blist):
	placeholder = blist[0]
	blist[0] = blist[1]
	return blist

def round_status(turn,sturn,opp,sopp,roundnum):
	print ("\n" +  "Round " + str(roundnum) + "\n")  #should be in methods_4_ease.turn_status(...)									    
	turn_status(sturn,turn,sopp,opp)
	nameslist = turn.show_teamnames()[:]
	return nameslist
