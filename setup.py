import os
packages = ['discord.py-self', 'rgbprint', 'sys']
for _ in packages:
    os.system(f'pip install {_}')

print("Everything installed :)")
