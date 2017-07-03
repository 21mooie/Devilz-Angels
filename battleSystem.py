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
	options = ["Attack","Defend","Heal","Done", "Press b for back", "Move"]
	vital = ["Attack","Defend","Heal"]

	turn = team2
	opp = team1
	#turnf = "Squad 1"
	#oppf = "Squad 2"
	sturn = "Squad 2"
	sopp = "Squad 1"


	charselect = None
	charinput = None
	brkfromwin = False

	roundnum = 1


	while winner == "":
		#####switch turns#####
		placeholder = turn
		turn = opp
		opp = placeholder
		splaceholder = sturn
		sturn = sopp
		sopp = splaceholder
		######################
		#team gets power to act
		#each character gets the ability to attack, defend, or heal per turn
		#they can also move.
		#once all players have finished their turn, control switches to other team
		print ("\n" +  "Round " + str(roundnum) + "\n")
		roundnum+=1
		methods_4_ease.turn_status(sturn,turn,sopp,opp)
		nameslist = turn.show_teamnames()[:]
		charfinished = True

		while len(nameslist) > 0 and winner == "":
			if (charfinished):
				charselect = choosecar(turn,nameslist)
				charselect = methods_4_ease.string_to_char(charselect,turn)
				charfinished = False

			###options = ["Attack","Defend","Heal","Done", "Press b for back", "Move"]
			print(options)
			charinput = raw_input("Choose one of the above. ")
			while charinput not in options:
				charinput = raw_input("Choose one of the above. ")

			#######   Move  ########
			if(charinput=="Move"):
				if charselect.move(turn,opp):     		  #   MOVE MOVE MOVE							  #
					options.pop()
					methods_4_ease.turn_status(sturn,turn,sopp,opp)

			####### End Move ##########



			elif (charinput in vital):
			####Defend



			####Heal



			####Attack
				if (charinput=="Attack"):
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
				options = ["Attack","Defend","Heal","Done", "Press b to go back" ,"Move"]
				charfinished = True
				print("breaking from attack")


	print(winner + " you have won!")





	'''while winner == None:
		if roundnum > 1:
			print("Switching turns")
	   	print("Round " + str(roundnum) + "\n")
		roundnum+=1
		methods_4_ease.switch_turns(turnf,turn,oppf,opp)
		nameslist = turn.show_teamnames()[:]
		#charselect = None
		#charinput = None
		committedchar = False
		#print(turn)

		### 2 ###
		while len(nameslist) > 0:         #while everyone on team has not gone



			for i in nameslist:
				print(i)

			if not committedchar:
				charselect = raw_input("Choose the character to control: ")             #
				while charselect not in nameslist:                                      #  Allows user to choose char if
					charselect = raw_input("Choose the character to control: ")         #  not committed already

				char = methods_4_ease.string_to_char(charselect,turn)

			chosen = False

			### 3 ###
			while not chosen:               #while char has not chosen

				if not brkfromwin:
					print(options)
					charinput = raw_input("Choose one of the above. ")                    #
					if charinput == "b":												  #  Allows char to choose an
						break															  #  option
					while charinput not in options:                                  	  #
						charinput = raw_input("Choose again. You cannot do that. ")		  #

 				chardone = False
 				donewchar = False
				### 4 ###
				while not chardone:	        #char has not committed to action

					committedchar = False
					if charinput == "Move":                       #
						if not char.move(turn,opp):     		  #   MOVE MOVE MOVE
							print("breaking from move")
							break								  #
						options.pop()
						methods_4_ease.status(turnf,turn,oppf,opp)
						committedchar = True


					elif charinput in vital:                      #
						                     					  # VITAL
											                      #

						if charinput == "Attack":                                #
							print(opp)                       			         #  back from attack
							attackinput = raw_input("Who will you attack? ")     #
							if attackinput == "b":
								print("breaking from attack")                             #
								break

							while attackinput not in opp.show_teamnames():              #
								print("repeat attacking ")
								attackinput = raw_input("Who will you attack? ")        #
							oppchar = methods_4_ease.string_to_char(attackinput,opp)    #  ATTACK ATTACK ATTACK
							char.attack(oppchar) 										#
							if opp.team_loss():											#
								winner = turnf
								brkfromwin = True
								print("breaking to end game")								#
								break

							methods_4_ease.status(turnf,turn,oppf,opp)
							committedchar = True
							options = options[3:]

						elif charinput == "Defend":
							print("defending")                     			#
							char.defend() 											# DEFEND DEFEND DEFEND
							methods_4_ease.status(turnf,turn,oppf,opp)				#
							committedchar = True
							options = options[3:]


						else:                        # will also have back function
							print("healing")
							char.heal()              # will change to include range    #  HEAL HEAL HEAL
							methods_4_ease.status(turnf,turn,oppf,opp)				   #
							committedchar = True
							options = options[3:]

					else:
						print("done")
						chosen = True                            #
						committedchar = False                    #
						donewchar = True                         #  DONE DONE DONE
					chardone = True

				if committedchar:
					print("supposed to have finished either move or vital ")
					chosen = bool(raw_input("Press Enter to continue turn otherwise type then press enter to end " + char.show_name() + " turn."))
					if chosen:
						donewchar = True
						committedchar = False

			if donewchar:
				print("char getting removed")
				nameslist.remove(charselect)
				options = ["Attack","Defend","Heal","Done", "Press b to go back" ,"Move"]

			if winner:
				break

		print("switch")
		placeholder = turn      #
		turn = opp 			   	#  switch turns
		opp = placeholder 		#
		placeholderf = turnf    #
		turnf = oppf
		oppf = placeholderf
	'''
