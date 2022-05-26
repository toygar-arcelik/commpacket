from os import listdir
import os
import pandas as pd

def main():
    collist = ['ApolloWdtReset']
    dirs = [name for name in listdir('.') if os.path.isdir(name)]
    for dir in dirs:
        for file in listdir(dir):
            #print(file)
            if not file.endswith('.csv'):
                continue
            with open('./'+dir+'/'+file, 'r+') as csvfile:
                print('<----- '+file+' ----->')
                df = pd.read_csv(csvfile, usecols=collist, dtype=str)
                excel_index = 2 # maalesef bu kötü çözüm :(
                for val in df.values:
                    try:
                        val = int(val)
                        if val != 0:
                            print(excel_index)
                    except:
                        print('exception, val: ' + str(val))
                    excel_index += 1

if __name__ == '__main__':
    main()