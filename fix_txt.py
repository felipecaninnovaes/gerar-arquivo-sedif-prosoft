import os

def fix_file(FOLDERPATH):
    NUMBERS_FILES = 0
    CORRECT_FILES = 0
    FIXED_FILES = 0
    CORRECT_LINE_DATA = 'DATALINE\n'
    for filename in os.listdir(FOLDERPATH):
        if filename.endswith('.txt'):
            with open(f'{FOLDERPATH}/{filename}', 'r', encoding='ISO-8859-15') as file:
                NUMBERS_FILES += 1
                text = file.readlines()
                if text[4] != CORRECT_LINE_DATA:
                    print(text)
                    text[4] = CORRECT_LINE_DATA
                    FIXED_FILES += 1
                    with open(f'{FOLDERPATH}/{filename}', 'w', encoding='ISO-8859-15') as file:
                        file.writelines(text)
                else:
                    CORRECT_FILES += 1
            
    print("QUANTIDADE DE ARQUIVOS: " + str(NUMBERS_FILES))
    print("QUANTIDADE DE ARQUIVOS CORRETOS: " + str(CORRECT_FILES))
    print("QUANTIDADE DE ARQUIVOS CORRIGIDOS: " + str(FIXED_FILES))
