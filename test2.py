from itertools import product
import numpy as np

def wartoscowanie_do_mozliwosci(liczba, mozliwosc):
    kombinacje = product([0, 1], repeat=liczba)
    wyniki = ''

    # MASKOWANIE JAKIEŚ
    mozliwosc = np.array(mozliwosc)
    mask = mozliwosc == 0
    for k in list(kombinacje):
        k = np.array(k)
        k[mask] = 0
        wyniki += '1' if np.count_nonzero(k) % 2 else '0'
    return wyniki

def limit_zmienionych(mozliwy_szyfr, znieksztalcona, max_zmienionych):
    czy_niezmienione = np.array(list(mozliwy_szyfr)) == np.array(list(znieksztalcona))
    return np.count_nonzero(czy_niezmienione==0) <= max_zmienionych

def stworz_translator(liczba, sciezka):
    text = ''
    x = product([0, 1], repeat=liczba)
    trans_table = str.maketrans('01', '10')

    while True:
        try:
            y = list(next(x))
            mozliwosc = wartoscowanie_do_mozliwosci(liczba, y)
            mozliwosc_neg = mozliwosc.translate(trans_table)
            print(''.join(str(x) for x in y))
            text += f"{mozliwosc};0{''.join(str(x) for x in y)}\n{mozliwosc_neg};1{''.join(str(x) for x in y)}\n"
        except StopIteration:
            break

    with open(sciezka, 'w') as f:
        f.write(text)


def odkoduj(translator, przyklady):
    with open(translator) as f:
        t = [x.rstrip().split(';') for x in f.readlines()]

    with open(przyklady) as file:
        p = file.read().rstrip().split('\n')
        max_zmienionych_bitow = int(p[2])
        przyklady = p[3:]



    for przyklad in przyklady:
        for kodowanie in t:
            if limit_zmienionych(kodowanie[0], przyklad, max_zmienionych_bitow):
                print(kodowanie[1])
                break
        else:
            print('brak')


if __name__ == '__main__':
    print(stworz_translator(12, 'translator13.txt'))
    odkoduj('translator13.txt', 'messages13.in.txt')

