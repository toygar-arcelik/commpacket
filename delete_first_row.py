import os
from os import listdir

def main():
    dirs = [name for name in listdir('.') if os.path.isdir(name)]
    for dir in dirs:
        for file in listdir(dir):
            print(file)
            if not file.endswith('.csv'):
                continue
            with open('./'+dir+'/'+file, 'r+') as f:
                lines = f.readlines()
                f.seek(0)
                f.truncate()
                f.writelines(lines[1:])

if __name__ == '__main__':
    main()