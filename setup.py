import os

print(f"""
	╔═╗┌─┐┌┬┐┬ ┬┌─┐
	╚═╗├┤  │ │ │├─┘
	╚═╝└─┘ ┴ └─┘┴
	""")
try:
	os.system("""
				pip install numpy colorama pillow
				""")
except:
	os.system("""
				pip install numpy colorama pillow
				""")
print('[+] Зависимости установлены! Запустите main.py')