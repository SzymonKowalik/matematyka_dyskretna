def tablica_prawdy(ile_zmiennych, czy_zanegowane, duplikaty_index):
	wyn = []
	for i in range((2**ile_zmiennych)):
		wartosciowanie = [int(x) for x in ((ile_zmiennych-1)*'0'+format(i, 'b'))[-ile_zmiennych:]]
		if czy_zanegowane:
			wartosciowanie[0] = not wartosciowanie[0]

		xor = 0

		for i, y in zip(wartosciowanie, duplikaty_index):
			if not i or not y:
				continue
			else:
				xor = xor ^ int(y)
		wyn.append(xor)
	return wyn

def porownaj(l1, l2, max_zmienionych):
	counter = 0
	for il1, il2 in zip(l1, l2):
		if il1 != il2:
			if counter >= max_zmienionych:
				return False
			counter += 1
	return True


def mozliwosci(ile_zmiennych, przyklad, max_zmienionych):
	count = 0
	# mozliwosci
	for x in range(2**ile_zmiennych):
		count += 1
		curr = ('0' * ile_zmiennych + format(x, 'b'))[-ile_zmiennych:]
		curr = [int(x) for x in curr]

		# Bez negacji
		mozliwy_szyfr = tablica_prawdy(ile_zmiennych, 0, curr)
		if porownaj(mozliwy_szyfr, przyklad, max_zmienionych):
			return [0]+curr
		# Z negacją
		mozliwy_szyfr = tablica_prawdy(ile_zmiennych, 1, curr)
		if porownaj(mozliwy_szyfr, przyklad, max_zmienionych):
			return [1]+curr

def przyklad_lista(przyklad_tekst):
	return [int(i) for i in przyklad_tekst]

def odkoduj(dlugosc_jednej_wiadomosci, ile_wiadomosci,  max_zmienionych_bitow, przyklady):
	ile_zmiennych = dlugosc_jednej_wiadomosci - 1

	i = 0
	while i < ile_wiadomosci:
		przyklad = przyklad_lista(przyklady[i])
		print(f"{mozliwosci(ile_zmiennych, przyklad, max_zmienionych_bitow)}")
		i += 1

def open_file(path):
	with open(path) as my_file:
		t = my_file.read().rstrip().split('\n')
	t[0] = int(t[0])
	t[1] = int(t[1])
	t[2] = int(t[2])
	return t


def z1():
	t = open_file("messages7.in.txt")
	przyklady = t[3:]

	dlugosc_wiadomosci = t[0]
	ile_przykladow = t[1]
	max_zmienionych_bitow = t[2]

	odkoduj(dlugosc_jednej_wiadomosci=dlugosc_wiadomosci, ile_wiadomosci=ile_przykladow, max_zmienionych_bitow=max_zmienionych_bitow, przyklady=przyklady)


def z2():
	t = open_file("messages13.in.txt")
	przyklady = t[3:]

	dlugosc_wiadomosci = t[0]
	ile_przykladow = t[1]
	max_zmienionych_bitow = t[2]

	odkoduj(dlugosc_jednej_wiadomosci=dlugosc_wiadomosci, ile_wiadomosci=ile_przykladow,
			max_zmienionych_bitow=max_zmienionych_bitow, przyklady=przyklady)

# Lepiej tego nie testowac (chyba ze nienawidzisz swojego kompa):
def z3():
	t = open_file("messages16.in.txt")
	przyklady = t[3:]

	dlugosc_wiadomosci = t[0]
	ile_przykladow = t[1]
	max_zmienionych_bitow = t[2]

	odkoduj(dlugosc_jednej_wiadomosci=dlugosc_wiadomosci, ile_wiadomosci=ile_przykladow,
			max_zmienionych_bitow=max_zmienionych_bitow, przyklady=przyklady)


z1()

