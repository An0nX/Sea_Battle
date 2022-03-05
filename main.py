#Импортируем библиотеки
import numpy as np
import os
from random import randrange
import ctypes
from time import sleep
from colorama import init, Fore, Back, Style
from PIL import Image, ImageDraw, ImageFont
import time

#Запускаем заставку
def extract_gif_frames(gif, fillEmpty=False):
    frames = []
    try:
        while True:
            gif.seek(gif.tell() + 1)
            new_frame = Image.new('RGBA', gif.size)
            new_frame.paste(playgif, (0, 0), playgif.convert('RGBA'))

            if fillEmpty:
                canvas = Image.new('RGBA', new_frame.size, (255, 255, 255, 255))
                canvas.paste(new_frame, mask=new_frame)
                new_frame = canvas

            frames.append(new_frame)
    except EOFError:
        pass
    return frames

def convert_image_to_ascii(image):
    font = ImageFont.load_default()
    (chrx, chry) = font.getsize(chr(32))
    weights = []
    for i in range(32, 127):
        chrImage = font.getmask(chr(i))
        ctr = 0
        for y in range(chry):
            for x in range(chrx):
                if chrImage.getpixel((x, y)) > 0:
                    ctr += 1
        weights.append(float(ctr) / (chrx * chry))

    output = ""
    (imgx, imgy) = image.size
    imgx = int(imgx / chrx)
    imgy = int(imgy / chry)
    image = image.resize((imgx, imgy), Image.BICUBIC)
    image = image.convert("L")
    pixels = image.load()
    for y in range(imgy):
        for x in range(imgx):
            w = float(pixels[x, y]) / 255
            wf = -1.0;
            k = -1
            for i in range(len(weights)):
                if abs(weights[i] - w) <= abs(wf - w):
                    wf = weights[i];
                    k = i
            output += chr(k + 32)
        output += "\n"
    return output

def convert_frames_to_ascii(frames):
    ascii_frames = []
    for frame in frames:
        new_frame = convert_image_to_ascii(frame)
        ascii_frames.append(new_frame)
    return ascii_frames

def animate_ascii(ascii_frames, frame_pause=.001, num_iterations=60, clear_prev_frame=True):
    for i in range(num_iterations):
        for frame in ascii_frames:
            print(frame)
            time.sleep(frame_pause)
            if clear_prev_frame:
                os.system('cls')

playgif = Image.open("start.gif")
frames = extract_gif_frames(playgif, fillEmpty=True)
ascii_frames = convert_frames_to_ascii(frames)
animate_ascii(ascii_frames, num_iterations=2)

#Задаем название окну консоли
ctypes.windll.kernel32.SetConsoleTitleA(b"Sea Battle by httpshotmaker")

#Инициализируем переменные
ships = 7
i = 1
user_ships = 7
bot_ships = 7
first = 0

#Создаем быстрый вызов баннера
def banner():
	#Очищаем консоль
	try:
		os.system('cls')
	except:
		os.system('clear')

	#Выводим заставку
	print(Fore.RED + 
		'.▄▄ · ▄▄▄ . ▄▄▄·     ▄▄▄▄·  ▄▄▄· ▄▄▄▄▄▄▄▄▄▄▄▄▌  ▄▄▄ .\n',
		'▐█ ▀. ▀▄.▀·▐█ ▀█     ▐█ ▀█▪▐█ ▀█ •██  •██  ██•  ▀▄.▀·\n',
		'▄▀▀▀█▄▐▀▀▪▄▄█▀▀█     ▐█▀▀█▄▄█▀▀█  ▐█.▪ ▐█.▪██▪  ▐▀▀▪▄\n',
		'▐█▄▪▐█▐█▄▄▌▐█ ▪▐▌    ██▄▪▐█▐█ ▪▐▌ ▐█▌· ▐█▌·▐█▌▐▌▐█▄▄▌\n',
		' ▀▀▀▀  ▀▀▀  ▀  ▀     ·▀▀▀▀  ▀  ▀  ▀▀▀  ▀▀▀ .▀▀▀  ▀▀▀ '
		)
	print(Fore.WHITE + '')

#Вызываем баннер
banner()

#Создаем пустое поле для юзера
user = np.zeros((10,10), dtype=int)

#Выводим поле
print('\n')
for n1 in range(0, len(user)):
    for n2 in range(0, len(user[n1])):
        print(user[n1][n2], end=' ')
    print()

#Расставляем корабли
while i <= ships:
	pot = 1
	def inputs():
		point = input(Fore.GREEN + "\nВведите место для установки корабля(Формат: 3,3): \n")
		print(Fore.WHITE + '')
		a,b = point.split(',')
		a = int(a)
		b = int(b)
		try:
			if user[a+1][b] != 1:
				u1 = 1
			else:
				u1 = 0
		except:
			u1 = 1
		try:
			if user[a-1][b] != 1:
				u2 = 1
			else:
				u2 = 0
		except:
			u2 = 2
		try:
			if user[a][b+1] != 1:
				u3 = 1
			else:
				u3 = 0
		except:
			u3 = 1
		try:
			if user[a][b-1] != 1:
				u4 = 1
			else:
				u4 = 0
		except:
			u4 = 1
		try:
			if user[a+1][b+1] != 1:
				u5 = 1
			else:
				u5 = 0
		except:
			u5 = 1
		try:
			if user[a+1][b-1] != 1:
				u6 = 1
			else:
				u6 = 0
		except:
			u6 = 1
		try:
			if user[a-1][b+1] != 1:
				u7 = 1
			else:
				u7 = 0
		except:
			u7 = 1
		try:
			if user[a-1][b-1] != 1:
				u8 = 1
			else:
				u8 = 0
		except:
			u8 = 1
		if u1 == 1 and u2 == 1 and u3 == 1 and u4 == 1 and u5 == 1 and u6 == 1 and u7 == 1 and u8 == 1:
			user[a][b] = 1
		else:
			pot = 0
	if pot == 0:
		while pot != 1:
			inputs()
	inputs()
	banner()
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
	double = 1
	def attack():
		first = 0
		if first == 0:
			print(Fore.WHITE + '')
			banner()
			print('\n')
			for n1 in range(0, len(user_attack)):
				for n2 in range(0, len(user_attack[n1])):
					print(user_attack[n1][n2], end=' ')
				print()
			first = 1
		print(Fore.GREEN + '\nВаш ход')
		target = input(Fore.GREEN + "\nВведите точку для выстрела(Формат: 3,3): \n")
		a,b = target.split(',')
		a = int(a)
		b = int(b)
		if user_attack[a][b] != 2:
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
				print(Fore.WHITE + '')
				banner()
				for n1 in range(0, len(user_attack)):
					for n2 in range(0, len(user_attack[n1])):
						print(user_attack[n1][n2], end=' ')
					print()
				print(Fore.CYAN + '\nУбил!')
				bot_ships-=1
			else:
				user_attack[a][b] = 2
				print(Fore.WHITE + '')
				banner()
				for n1 in range(0, len(user_attack)):
					for n2 in range(0, len(user_attack[n1])):
						print(user_attack[n1][n2], end=' ')
					print()
				print(Fore.CYAN + '\nПромах!')
			double = 1
		else:
			double = 0
		if double == 0:
			while double != 1:
				attack()
	attack()

#Пожалуй и бот заслуживает попробовать свои силы, теперь его очередь
	sleep(3)
	print(Fore.RED + '\nХод бота')
	sleep(2)
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
			print(Fore.WHITE + '\n')
			banner()
			for n1 in range(0, len(bot_attack)):
				for n2 in range(0, len(bot_attack[n1])):
					print(bot_attack[n1][n2], end=' ')
				print()
			print(Fore.CYAN + '\nУбил!')
			
			user_ships-=1
		else:
			bot_attack[a][b] = 2
			print(Fore.WHITE + '\n')
			banner()
			for n1 in range(0, len(bot_attack)):
				for n2 in range(0, len(bot_attack[n1])):
					print(bot_attack[n1][n2], end=' ')
				print()
			print(Fore.CYAN + '\nПромах!')
		sleep(3)
			
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
					print(Fore.WHITE + '')
					banner()
					for n1 in range(0, len(bot_attack)):
						for n2 in range(0, len(bot_attack[n1])):
							print(bot_attack[n1][n2], end=' ')
						print()
					print(Fore.CYAN + '\nУбил!')
					
					user_ships-=1
				else:
					bot_attack[a][b] = 2
					print(Fore.WHITE + '')
					banner()
					for n1 in range(0, len(bot_attack)):
						for n2 in range(0, len(bot_attack[n1])):
							print(bot_attack[n1][n2], end=' ')
						print()
					print(Fore.CYAN + '\nПромах!')
					
					proba = 0

#Результаты
if user_ships == 0:
	banner()
	print(Fore.RED + '\nВы проиграли')
if bot_ships == 0:
	banner()
	print(Fore.GREEN + '\nВы выиграли')