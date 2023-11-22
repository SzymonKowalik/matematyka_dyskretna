import itertools
import numpy as np

def tablica_prawdy(ile_zmiennych, czy_zanegowane, duplikaty_index):
	wyn = []
	for i in range((2**ile_zmiennych)):
		wartosciowanie = itertools.product([0, 1], repeat=ile_zmiennych)
		wartosciowanie = [int(x) for x in ((ile_zmiennych-1)*'0'+format(i, 'b'))[-ile_zmiennych:]]

		print(wartosciowanie)
		if czy_zanegowane:
			wartosciowanie[0] = not wartosciowanie[0]
		print(wartosciowanie)
		print('-----')
		xor = 0

		for i, y in zip(wartosciowanie, duplikaty_index):
			if i and y:
				xor = xor ^ int(y)
		wyn.append(xor)
	return wyn


def porownaj(mozliwosc, znieksztalcona, max_zmienionych):
	czy_niezmienione = np.array(mozliwosc) == np.array(znieksztalcona)
	return np.count_nonzero(czy_niezmienione==0) <= max_zmienionych


def mozliwosci(ile_zmiennych, przyklad, max_zmienionych):
	# mozliwosci
	mozliwosci = itertools.product([0, 1], repeat=ile_zmiennych)
	print(list(mozliwosci))

	for x in mozliwosci:
		# Bez negacji
		mozliwy_szyfr = tablica_prawdy(ile_zmiennych, 0, x)
		if porownaj(mozliwy_szyfr, przyklad, max_zmienionych):
			return f"0{x}"
		# Z negacją
		mozliwy_szyfr = tablica_prawdy(ile_zmiennych, 1, x)
		if porownaj(mozliwy_szyfr, przyklad, max_zmienionych):
			return f"1{x}"


def odkoduj(dlugosc_jednej_wiadomosci, 	max_zmienionych_bitow, przyklady):
	for zakodowana in przyklady:
		zakodowana = np.array([int(x) for x in zakodowana])
		print(f"{mozliwosci(dlugosc_jednej_wiadomosci - 1, zakodowana, max_zmienionych_bitow)}")


def uruchom(sciezka):
	with open(sciezka) as my_file:
		t = my_file.read().rstrip().split('\n')
	przyklady = t[3:]

	dlugosc_wiadomosci = int(t[0])
	ile_przykladow = int(t[1])
	max_zmienionych_bitow = int(t[2])

	odkoduj(dlugosc_jednej_wiadomosci=dlugosc_wiadomosci,
			max_zmienionych_bitow=max_zmienionych_bitow, przyklady=przyklady)


# def prawidlowa_mozliwosc(zmieniony, max_zmienionych):
# 	mozliwosci = itertools.product([0, 1], repeat=len(zmieniony))
# 	for mozliwosc in mozliwosci:
# 		if porownaj(mozliwosc, zmieniony, max_zmienionych):
# 			return mozliwosc


if __name__ == '__main__':
	# uruchom("messages7.in.txt")
	# uruchom("messages13.in.txt")
	# uruchom("messages16.in.txt")
	# odkoduj(4, 1, ['01111001'])

	print(prawidlowa_mozliwosc([0, 1, 1, 0, 1, 1, 0, 1], 1))
