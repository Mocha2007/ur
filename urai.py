import random
def dice():
	return random.randint(0,1)+random.randint(0,1)+random.randint(0,1)+random.randint(0,1)
while 1:
	whitepiece=[0,0,0,0,0,0,0]
	blackpiece=[0,0,0,0,0,0,0]
	white=0
	black=0
	skip=0
	skipped=0
	print("Welcome to Mocha's Ur Simulator!")
	open("game.html", "w+").write("<ol>\n")
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
						open("game.html", "a").write(str(whitepiece[choice]-roll)+"x"+str(whitepiece[choice]))
					else:
						open("game.html", "a").write(str(whitepiece[choice]-roll)+">"+str(whitepiece[choice]))
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
					if skipped==0:
						open("game.html", "a").write("\t<li>&Oslash;,")
					else:
						open("game.html", "a").write("&Oslash;,")
						skipped=0
			else:
				print("You rolled a zero!")
				if skipped==0:
					open("game.html", "a").write("\t<li>&Oslash;,")
				else:
					open("game.html", "a").write("&Oslash;,")
					skipped=0
		else:
			skip-=1
			skipped=1
		#black's move, mirror of white's
		if skip==0 and white!=7:
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
					choice=-1
					#AI ALGORITHM BEGIN
					#if can get to safety, do so.
					for i in playablepiece:
						if blackpiece[i]<13 and blackpiece[i]+roll>12:
							choice=i
							break
					#if can capture enemy piece, do so.
					if choice==-1:
						for i in playablepiece:
							if blackpiece[i]+roll in whitepiece:
								choice=i
								break
					#if there is an exposed piece, move it
					if choice==-1:
						for i in playablepiece:
							if 13>blackpiece[i]>4 and blackpiece[i]!=8:
								choice=i
								break
					#if can land on 8, do so.
					if choice==-1:
						for i in playablepiece:
							if blackpiece[i]+roll==8:
								choice=i
								break
					#if can land on 4 or 14, do so.
					if choice==-1:
						for i in playablepiece:
							if blackpiece[i]+roll==4 or blackpiece[i]+roll==14:
								choice=i
								break
					#if can gain point, do so.
					if choice==-1:
						for i in playablepiece:
							if blackpiece[i]+roll==15:
								choice=i
								break
					#if can move a piece in safezone(s) without passing 4, do so.
					if choice==-1:
						for i in playablepiece:
							if blackpiece[i]+roll<5 or blackpiece[i]+roll>12:
								choice=i
								break
					#otherwise, take the first move available
					if choice==-1:
						choice=playablepiece[0]
					#continue as normal
					blackpiece[choice]+=roll
					if skipped==1:skipped=0
					if (13>blackpiece[choice]>4) and (blackpiece[choice] in whitepiece):
						for i in range(len(whitepiece)):
							if whitepiece[i]==blackpiece[choice]:
								whitepiece[i]=0
						open("game.html", "a").write(str(blackpiece[choice]-roll)+"x"+str(blackpiece[choice]))
					else:
						open("game.html", "a").write(str(blackpiece[choice]-roll)+">"+str(blackpiece[choice]))
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
					print("Black can't move!")
					open("game.html", "a").write("&Oslash;</li>\n")
					skipped=0
			else:
				print("Black rolled a zero!")
				open("game.html", "a").write("&Oslash;</li>\n")
				skipped=0
		else:
			skip-=1
			skipped=1
	if white==7:print("White wins!")
	else:print("Black wins!")
	print(white,"-",black)
	print(sum(whitepiece),"-",sum(blackpiece))
	open("game.html", "a").write("</ol>\n")
	input()