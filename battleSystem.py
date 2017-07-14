from classes import *
import methods_4_ease


def choosecar(thisteam,nameslist):
	charselect = raw_input("Choose the character to control: ")             #
	while charselect not in nameslist:                                      #  Allows user to choose char if
		charselect = raw_input("Choose the character to control: ")
	return charselect

	#must improve to be able to check if the turn team has lost

	#must be able to choose char then go back to choose another char
def battleSystem(team1,team2):

	winner = ""
	options = ["Attack","Focus","Heal","Done", "b", "Move"]
	vital = ["Attack","Focus","Heal"]

	turn = team2
	opp = team1
	#turnf = "Squad 1"
	#oppf = "Squad 2"
	sturn = "Squad 2"
	sopp = "Squad 1"
	charinput = "x"

	battlelist = [opp,turn]


	charselect = None
	charinput = None
	brkfromwin = False

	roundnum = 1


	while winner == "":                             ##each team
		#####switch turns#####    should be in methods_4_ease

		######switch teams
		placeholder = turn
		turn = opp
		opp = placeholder
		#####switch teams

		#####switch teamnames
		splaceholder = sturn
		sturn = sopp
		sopp = splaceholder
		#####switch teamnames

		#battlelist = methods_4_ease.switch(battlelist)

		######################
		#team gets power to act
		#each character gets the ability to attack, focus, or heal per turn
		#they can also move.
		#once all players have finished their turn, control switches to other team
		######################

		#print ("\n" +  "Round " + str(roundnum) + "\n")  #should be in methods_4_ease.turn_status(...)
		#roundnum+=1									     #''
		#methods_4_ease.turn_status(sturn,turn,sopp,opp)
		#nameslist = turn.show_teamnames()[:]


		nameslist = methods_4_ease.round_status(turn,sturn,opp,sopp,roundnum)
		charfinished = True
		roundnum+=1

		while len(nameslist) > 0 and winner == "":        #each char
			#charinput = false
			if (charfinished):

				charselect = choosecar(turn,nameslist)
				charselect = methods_4_ease.string_to_char(charselect,turn)
				charfinished = False

			###options = ["Attack","Focus","Heal","Done", "Press b for back", "Move"]
			print(options)
			charinput = raw_input("Choose one of the above. ")
			if (charinput == "b" and len(options)==6):
				charinput = ""
				charfinished = True


			#add a function in methods_4_ease to remove back once a character has made a move

			#######   Move  ########
			elif(charinput=="Move"):
				if charselect.move(turn,opp):     		  #   MOVE MOVE MOVE							  #
					options.pop()
					methods_4_ease.turn_status(sturn,turn,sopp,opp)


			####### End Move ##########



			elif (charinput in vital):
			####Focus     Focus
				if (charinput=="Focus"):
					print("Focus")
					charselect.focus()
					print("Focus activated! " + charselect.show_name() + " is now unstoppable!")
					options = options[3:]
					#charselect.Focus


			####Heal
				elif (charinput=="Heal"):
					print("health")
					healthinput = raw_input("Who would you like to heal?")
					if healthinput == "b":
						print("breaking from attack")
						charinput = ""

					elif healthinput not in turn.show_teamnames():              #
							print("repeat attacking ")

					else:

						turnchar = methods_4_ease.string_to_char(healthinput,turn)    #  ATTACK ATTACK ATTACK
						print("got here")
						charselect.heal(turnchar)
						options = options[3:] ##must repeat


			####Attack
				elif (charinput=="Attack"):
					print(opp)                       			         #  back from attack
					attackinput = raw_input("Who will you attack? ")     #
					if attackinput == "b":
						print("breaking from attack")
						charinput = ""                            #
						#break breaks from character's turn

					elif attackinput not in opp.show_teamnames():              #
							print("repeat attacking ")
							#attackinput = raw_input("Who will you attack? ")        #

					else:
						oppchar = methods_4_ease.string_to_char(attackinput,opp)    #  ATTACK ATTACK ATTACK
						charselect.attack(oppchar)
						options = options[3:] ##must repeat  										#

					if (opp.team_loss()):

						winner = sturn

				methods_4_ease.turn_status(sturn,turn,sopp,opp)
					#committedchar = True
				#options = options[3:]


			elif (charinput == "Done"):
				print("done")
				print("char getting removed")
				nameslist.remove(str(charselect))
				options = ["Attack","Focus","Heal","Done", "b" ,"Move"]
				if (charselect.show_focus>0):
					charselect.focus_reduce()
					if (charselect.show_focus==0):
						print("Oh no focus mode has ended :(")
				charfinished = True
				charinput = ""
			else:
				print("This input " + charinput + " is incorrect")



	print(winner + " you have won!")
