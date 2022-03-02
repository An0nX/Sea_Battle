#Импортируем библиотеки
import numpy as np
import os
from random import randrange
import ctypes

#Задаем название окну консоли
ctypes.windll.kernel32.SetConsoleTitleA(b"Sea Battle by httpshotmaker")

#Инициализируем переменные
ships = 7
i = 1
user_ships = 7
bot_ships = 7
first = 0

#Очищаем консоль
try:
	os.system('cls')
except:
	os.system('clear')

#Выводим заставку
print(
	'.▄▄ · ▄▄▄ . ▄▄▄·     ▄▄▄▄·  ▄▄▄· ▄▄▄▄▄▄▄▄▄▄▄▄▌  ▄▄▄ .\n',
	'▐█ ▀. ▀▄.▀·▐█ ▀█     ▐█ ▀█▪▐█ ▀█ •██  •██  ██•  ▀▄.▀·\n',
	'▄▀▀▀█▄▐▀▀▪▄▄█▀▀█     ▐█▀▀█▄▄█▀▀█  ▐█.▪ ▐█.▪██▪  ▐▀▀▪▄\n',
	'▐█▄▪▐█▐█▄▄▌▐█ ▪▐▌    ██▄▪▐█▐█ ▪▐▌ ▐█▌· ▐█▌·▐█▌▐▌▐█▄▄▌\n',
	' ▀▀▀▀  ▀▀▀  ▀  ▀     ·▀▀▀▀  ▀  ▀  ▀▀▀  ▀▀▀ .▀▀▀  ▀▀▀ '
	)

#Создаем пустое поле для юзера
user = np.zeros((10,10), dtype=int)

#Выводим поле
for n1 in range(0, len(user)):
    for n2 in range(0, len(user[n1])):
        print(user[n1][n2], end=' ')
    print()

#Расставляем корабли
while i <= ships:
	point = input("\nВведите место для установки корабля(Формат: 3,3): \n")
	a,b = point.split(',')
	user[int(a)][int(b)] = 1
	print("\n")
	for n1 in range(0, len(user)):
		for n2 in range(0, len(user[n1])):
			print(user[n1][n2], end=' ')
		print()
	i+=1

#Создаем пустое поле для бота
bot = np.zeros((10,10), dtype=int)

#Генерируем корабли
i = 1
while i <= ships:
	a = randrange(10)
	b = randrange(10)
	try:
		if bot[a][b+1] != 1:
			l1 = 1
		else:
			l1 = 0
	except:
		l1 = 1
		pass

	try:
		if bot[a][b-1] != 1:
			l2 = 1
		else:
			l2 = 0
	except:
		l2 = 1
		pass

	try:
		if bot[a+1][b] != 1:
			l3 = 1
		else:
			l3 = 0
	except:
		l3 = 1
		pass

	try:
		if bot[a-1][b] != 1:
			l4 = 1
		else:
			l4 = 0
	except:
		l4 = 1
		pass

	try:
		if bot[a+1][b+1] != 1:
			l5 = 1
		else:
			l5 = 0
	except:
		l5 = 1
		pass

	try:
		if bot[a+1][b-1] != 1:
			l6 = 1
		else:
			l6 = 0
	except:
		l6 = 1
		pass

	try:
		if bot[a-1][b+1] != 1:
			l7 = 1
		else:
			l7 = 0
	except:
		l7 = 1
		pass

	try:
		if bot[a-1][b-1] != 1:
			l2 = 1
		else:
			l2 = 0
	except:
		l2 = 1
		pass

	if l1 == 1 and l2 == 1 and l3 == 1 and l4 == 1 and l5 == 1 and l6 == 1 and l7 == 1 and l2 == 1:
		bot[a][b] = 1
	else:
		continue
	i+=1

#Создаем пустое поле для атак юзера
user_attack = np.zeros((10,10), dtype=int)

#Создаем пустое поле для атак юзера
bot_attack = np.zeros((10,10), dtype=int)

#Первый ход юзеру, землю крестьянам!
while user_ships != 0 or bot_ships != 0:
	print('\n')
	if first == 0:
		for n1 in range(0, len(user_attack)):
			for n2 in range(0, len(user_attack[n1])):
				print(user_attack[n1][n2], end=' ')
			print()
		first = 1
	print('\nВаш ход')
	target = input("\nВведите точку для выстрела(Формат: 3,3): \n")
	a,b = target.split(',')
	a = int(a)
	b = int(b)
	if bot[a][b] == 1:
		user_attack[a][b] = 2
		try:
			user_attack[a+1][b] = 2
		except:
			pass
		try:
			user_attack[a-1][b] = 2
		except:
			pass
		try:
			user_attack[a][b+1] = 2
		except:
			pass
		try:
			user_attack[a][b-1] = 2
		except:
			pass
		try:
			user_attack[a+1][b+1] = 2
		except:
			pass
		try:
			user_attack[a+1][b-1] = 2
		except:
			pass
		try:
			user_attack[a-1][b+1] = 2
		except:
			pass
		try:
			user_attack[a-1][b-1] = 2
		except:
			pass
		for n1 in range(0, len(user_attack)):
			for n2 in range(0, len(user_attack[n1])):
				print(user_attack[n1][n2], end=' ')
			print()
		print('\nУбил!')
		bot_ships-=1
	else:
		user_attack[a][b] = 2
		for n1 in range(0, len(user_attack)):
			for n2 in range(0, len(user_attack[n1])):
				print(user_attack[n1][n2], end=' ')
			print()
		print('\nПромах!')

#Пожалуй и бот заслуживает попробовать свои силы, теперь его очередь
	print('Ход бота')
	a = randrange(10)
	b = randrange(10)
	a = int(a)
	b = int(b)
	if bot_attack[a][b] != 2:
		if user[a][b] == 1:
			try:
				bot_attack[a][b] = 2
			except:
				pass
			try:
				bot_attack[a+1][b] = 2
			except:
				pass
			try:
				bot_attack[a-1][b] = 2
			except:
				pass
			try:
				bot_attack[a][b+1] = 2
			except:
				pass
			try:
				bot_attack[a][b-1] = 2
			except:
				pass
			try:
				bot_attack[a+1][b+1] = 2
			except:
				pass
			try:
				bot_attack[a+1][b-1] = 2
			except:
				pass
			try:
				bot_attack[a-1][b+1] = 2
			except:
				pass
			try:
				bot_attack[a-1][b-1] = 2
			except:
				pass
			for n1 in range(0, len(bot_attack)):
				for n2 in range(0, len(bot_attack[n1])):
					print(bot_attack[n1][n2], end=' ')
				print()
			print('\nУбил!')
			print('\n--------------------------\n')
			user_ships-=1
		else:
			bot_attack[a][b] = 2
			for n1 in range(0, len(bot_attack)):
				for n2 in range(0, len(bot_attack[n1])):
					print(bot_attack[n1][n2], end=' ')
				print()
			print('\nПромах!')
			print('\n--------------------------\n')
	else:
		proba = 1
		while proba != 0:
			if bot_attack != 2:
				if user[a][b] == 1:
					try:
						bot_attack[a][b] = 2
					except:
						pass
					try:
						bot_attack[a+1][b] = 2
					except:
						pass
					try:
						bot_attack[a-1][b] = 2
					except:
						pass
					try:
						bot_attack[a][b+1] = 2
					except:
						pass
					try:
						bot_attack[a][b-1] = 2
					except:
						pass
					try:
						bot_attack[a+1][b+1] = 2
					except:
						pass
					try:
						bot_attack[a+1][b-1] = 2
					except:
						pass
					try:
						bot_attack[a-1][b+1] = 2
					except:
						pass
					try:
						bot_attack[a-1][b-1] = 2
					except:
						pass
					for n1 in range(0, len(bot_attack)):
						for n2 in range(0, len(bot_attack[n1])):
							print(bot_attack[n1][n2], end=' ')
						print()
					print('\nУбил!')
					print('\n--------------------------\n')
					user_ships-=1
				else:
					bot_attack[a][b] = 2
					for n1 in range(0, len(bot_attack)):
						for n2 in range(0, len(bot_attack[n1])):
							print(bot_attack[n1][n2], end=' ')
						print()
					print('\nПромах!')
					print('\n--------------------------\n')
					proba = 0

#Результаты
if user_ships == 0:
	print('Вы проиграли')
if bot_ships == 0:
	print('Вы выиграли')