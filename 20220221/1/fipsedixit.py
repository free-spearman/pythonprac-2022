import sys, ipsedixit
from os.path import exists
SEP = '\n\n'
PARAM_LIST = ('caesar', 'tacitus')
ENCODING = 'utf-8' 

def fipsedixit(paragraphs, p2):
    if not p2:
        prg = ipsedixit.Generator().paragraphs(int(paragraphs))
        print(*prg, sep=SEP)
        return

    if  p2 not in PARAM_LIST:
        if not exists(p2):
            print(f"Такого файла нет {p2}")
            return
        with open(p2, encoding=ENCODING) as f_word:
            p2 = f_word.read()        
    prg = ipsedixit.Generator(p2).paragraphs(int(paragraphs))
    print(*prg, sep=SEP)


if __name__ == '__main__':
    if len(sys.argv)==3:
        fipsedixit(sys.argv[1], sys.argv[2])
    elif len(sys.argv)==2:
        fipsedixit(sys.argv[1])
    else:
        print("Упс, с аргументами что-то не так, попробуйте в другой раз")
