import os 
import sys



name = sys.argv[1]
n = name[:name.find('.')]

os.system(f'pyinstaller --onefile {name}')
os.system(f'cp ./dist/{n} {n}')
os.system(f'chmod 777 {n}')
os.system(f'rm -rf dist build {n}.spec')
