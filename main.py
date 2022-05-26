from os import listdir
import os
import pandas as pd

def algo(current: int, next: int):
    if current == 255 and next == 0:
        return True
    if current+1 != next:
        return False
    else:
        return True

def algo2(current: int, next: int):
    if current == 255 and next == 0:
        return True
    if current == next:
        return True
    if current+1 != next:
        return False
    else:
        return True

def algo3(current: int, next: int):
    if current == 255 and next == 0:
        return True
    if current == next:
        return True
    if current+10 > next:
        return True
    else:
        return False

def main():
    collist = ['CommPackageControl']
    dirs = [name for name in listdir('.') if os.path.isdir(name)]
    for dir in dirs:
        for file in listdir(dir):
            #print(file)
            if not file.endswith('.csv'):
                continue
            with open('./'+dir+'/'+file, 'r+') as csvfile:
                print('<----- '+file+' ----->')
                df = pd.read_csv(csvfile, usecols=collist, dtype=str)
                try:
                    current_value = int(df.values[0])
                except:
                    pass
                    #print('Error in file: '+file)
                    #continue
                excel_index = 2 # maalesef bu kötü çözüm :(
                for next_value in df.values[1:]:
                    next_value = int(next_value)
                    result = algo3(current_value, next_value)
                    current_value = next_value
                    if result == False:
                        print(excel_index)
                    excel_index += 1

if __name__ == '__main__':
    main()