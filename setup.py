import os
packages = ['discord.py-self', 'rgbprint']
os.system('pip install discord.py')
os.system('pip uninstall discord.py')
for _ in packages:
    os.system(f'pip install {_}')

print("Everything installed :)")
