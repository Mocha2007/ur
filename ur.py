import random
def dice():
	return random.randint(0,1)+random.randint(0,1)+random.randint(0,1)+random.randint(0,1)
whitepiece=[0,0,0,0,0,0,0]
blackpiece=[0,0,0,0,0,0,0]
white=0
black=0
skip=0
skipped=0
print("Welcome to Mocha's Ur Simulator!")
open("game.html", "a").write("<ol>\n")
while white<7>black:
	#white's move
	if skip==0:
		roll=dice()
		print("WHITE TO ROLL:",white,"-",black,"\nWhite rolls a",roll)
		if roll!=0:
			playablepiece=[]
			#finding which pieces can be moved
			for i in range(len(whitepiece)):
				if whitepiece[i]+roll not in whitepiece:#can't step on another of your own pieces
					if not ((whitepiece[i]+roll==8) and (8 in blackpiece)):#can't step on opponent, but only on central lotus
						if whitepiece[i]+roll<=15:#can't overgo
							playablepiece+=[i]
			if playablepiece!=[]:
				print("Choose a piece to play:",playablepiece)
				print("Keep in mind, the positions of your pieces are:",whitepiece)
				print("Keep in mind, the positions of black are:",blackpiece)
				choice=-1
				while choice not in playablepiece:
					try:
						choice=int(input("> "))
					except ValueError:
						choice=random.choice(playablepiece)#I gave you the fucking chance and you lost it
				whitepiece[choice]+=roll
				#capture
				if skipped!=1:
					open("game.html", "a").write("\t<li>")
				else:skipped=0
				if (13>whitepiece[choice]>4) and (whitepiece[choice] in blackpiece):
					for i in range(len(blackpiece)):
						if blackpiece[i]==whitepiece[choice]:
							blackpiece[i]=0
					open("game.html", "a").write(str(whitepiece[choice])+"x"+str(whitepiece[choice]+roll))
				else:
					open("game.html", "a").write(str(whitepiece[choice])+">"+str(whitepiece[choice]+roll))
				#forced?
				if len(playablepiece)==1:
					open("game.html", "a").write("f")
				#lotus reroll
				if whitepiece[choice]==4 or whitepiece[choice]==8 or whitepiece[choice]==14:
					skip=1
					open("game.html", "a").write("&amp;")
				#cross the end
				elif whitepiece[choice]==15:
					white+=1
					del whitepiece[choice]
					open("game.html", "a").write("+")
				#print
				try:
					print("White has moved from",whitepiece[choice]-roll,"to",whitepiece[choice],".")
				except IndexError:
					pass
				if skip==0:
					open("game.html", "a").write(",")
			else:
				print("You can't move!")
				open("game.html", "a").write("\t<li>&Oslash;,")
		else:
			print("You rolled a zero!")
			open("game.html", "a").write("\t<li>&Oslash;,")
	else:
		skip-=1
		skipped=1
	#black's move, mirror of white's
	if skip==0:
		roll=dice()
		print("BLACK TO ROLL:",white,"-",black,"\nBlack rolls a",roll)
		if roll!=0:
			playablepiece=[]
			for i in range(len(blackpiece)):
				if blackpiece[i]+roll not in blackpiece:
					if not ((blackpiece[i]+roll==8) and (8 in whitepiece)):
						if blackpiece[i]+roll<=15:
							playablepiece+=[i]
			if playablepiece!=[]:
				print("Choose a piece to play:",playablepiece)
				print("Keep in mind, the positions of your pieces are:",blackpiece)
				print("Keep in mind, the positions of white are:",whitepiece)
				choice=-1
				while choice not in playablepiece:
					try:
						choice=int(input("> "))
					except ValueError:
						choice=random.choice(playablepiece)
				blackpiece[choice]+=roll
				if (13>blackpiece[choice]>4) and (blackpiece[choice] in whitepiece):
					for i in range(len(whitepiece)):
						if whitepiece[i]==blackpiece[choice]:
							whitepiece[i]=0
					open("game.html", "a").write(str(whitepiece[choice])+"x"+str(whitepiece[choice]+roll))
				else:
					open("game.html", "a").write(str(whitepiece[choice])+">"+str(whitepiece[choice]+roll))
				if len(playablepiece)==1:
					open("game.html", "a").write("f")
				if blackpiece[choice]==4 or blackpiece[choice]==8 or blackpiece[choice]==14:
					skip=1
					open("game.html", "a").write("&amp;")
				elif blackpiece[choice]==15:
					black+=1
					del blackpiece[choice]
					open("game.html", "a").write("+")
				try:
					print("Black has moved from",blackpiece[choice]-roll,"to",blackpiece[choice],".")
				except IndexError:
					pass
				if skip==0:
					open("game.html", "a").write("</li>\n")
			else:
				print("You can't move!")
				open("game.html", "a").write("&Oslash;</li>\n")
		else:
			print("You rolled a zero!")
			open("game.html", "a").write("&Oslash;</li>\n")
	else:
		skip-=1
		skipped=1
if white==7:print("White wins!")
else:print("Black wins!")
print(white,"-",black)
open("game.html", "a").write("</ol>\n")