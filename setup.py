import os
os.system('pip uninstall discord.py')
os.system('pip uninstall discord.py-self')
packages = ['discord.py-self', 'rgbprint', 'sys']
for _ in packages:
    os.system(f'pip install {_}')

print("Everything installed :)")
