import random
import os
import time
import sys
import argparse

clear = lambda: os.system('clear')

#Nasz wisielec
picture=[
"""
   +---+
   |   |
       |
       |
       |
      / \ """,
"""
   +---+
   |   |
   O   |
       |
       |
       |
      / \ """,
"""
   +---+
   |   |
   O   |
   |   |
       |
       |
      / \ """,
"""
   +---+
   |   |
   O   |
  /|   |
       |
       |
      / \ """,
"""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
      / \ """,
"""
   +---+
   |   |
   O   |
  /|\  |
   |   |
       |
      / \ 
""",
"""
   +---+
   |   |
   O   |
  /|\  |
   |   |
  /    |
      / \ 
""",
"""
   +---+
   |   |
   O   |
  /|\  |
   |   |
  / \  |
      / \ 
"""
]

#lista do trybu easy
easy=['ant', 'mouse', 'dog', 'hornet', 'cobra', 'corry', 'girrafe']

#lista do trybu hard
hard=['ala ma kota', 'co tu sie dzieje', 'lubie placki', 'studenci lubia latwe kolokwia']

secret_word = random.choice(easy)

#operowanie argumentami w celu wlaczenia jednego z 3 trybow gry
parser = argparse.ArgumentParser()
parser.add_argument("--easy", help="Tryb easy")
parser.add_argument("--hard", help="Tryb hard")
parser.add_argument("--custom", help="Tryb custom")
args = parser.parse_args()
if args.easy:
	secret_word = random.choice(easy)
elif args.hard:
	secret_word = random.choice(hard)
elif args.custom:
	try:
		plik=input("Podaj nazwe pliku: ")
		if ".txt" not in plik:
			plik=plik+".txt"
		file_1 = open(plik, "r")
		custom_list= file_1.readlines()
		secret_word = random.choice(custom_list)
		secret_word = secret_word.strip()
	except IOError:
		print("Brak pliku")
		sys.exit(0)

#pozno juz troche, tak bedzie prosciej jezeli
#user sobie jakies duze litery wybierze do listy
secret_word = secret_word.lower()

#zmienne
win_cond = len(secret_word)
global guessed
guessed = 0
wrong = 0
blank='_'*win_cond
typed=[]

#metoda sprawdza czy podana litera jest w zagadce
def check_answer(c):
	if c in secret_word:
		print("Ok")

	elif c not in secret_word:
		print("Zle")
		return 0
	return 1

#metoda wypisuje progress w zagadce
def reveal(c, blank):
	global guessed
	for i in range(len(secret_word)):
		if c in secret_word[i]:
			blank = blank[:i]+blank[i].replace('_', secret_word[i])+blank[(i+1):]
			guessed+=1
		else: continue
	print(blank)
	return blank
			
#metoda sprawdza czy user wygral lub przegral
def check_winOrlost():
	if guessed == win_cond:
		print("Brawo!")
		return 1
	elif wrong == len(picture)-1:
		print("Game over"+"\n"+"Odpowiedz to: "+secret_word)
		return 1
	return


#korekta ze wzgledu na obecnosc spacji w zdaniach
def check_for_space(blank):
	global guessed
	c=' '
	for i in range(len(secret_word)):
		if c in secret_word[i]:
			blank = blank[:i]+blank[i].replace('_', secret_word[i])+blank[(i+1):]
			guessed+=1
		else: continue
	return blank


blank = check_for_space(blank)
clear()
print(blank)
print(picture[wrong])

#glowna petla programu
while 1:
	if check_winOrlost():
		break
	try:
		x=input("Podaj znak: ")
	except:
		print("Blad wprowadzania")
		continue
	else:
		if not x.isalpha():
			clear()
			print("Error - Podaj litere")
			print(blank)
			print(picture[wrong])
			continue

		elif x.lower() in typed:
			clear()
			print("Juz podales ta litere")
			print(blank)
			print(picture[wrong])
			continue
	x=x.lower()

	if check_answer(x):
		clear()
		typed.append(x)
		blank=reveal(x, blank)
		print(picture[wrong])
		continue
	else:
		wrong+=1
		clear()
		print(blank)
		print(picture[wrong])
		continue

