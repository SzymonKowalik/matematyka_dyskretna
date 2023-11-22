def tablica_prawdy(ile_zmiennych, czy_zanegowane, duplikaty_index):
	wyn = []
	for i in range((2**ile_zmiennych)):
		wartosciowanie = [int(x) for x in ((ile_zmiennych-1)*'0'+format(i, 'b'))[-ile_zmiennych:]]
		if czy_zanegowane:
			wartosciowanie[0] = not wartosciowanie[0]

		xor = 0

		for i, y in zip(wartosciowanie, duplikaty_index):
			if i and y:
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


def odkoduj(dlugosc_jednej_wiadomosci, ile_wiadomosci,  max_zmienionych_bitow, przyklady):
	ile_zmiennych = dlugosc_jednej_wiadomosci - 1

	i = 0
	while i < ile_wiadomosci:
		przyklad = [int(x) for x in przyklady[i]]
		print(f"{mozliwosci(ile_zmiennych, przyklad, max_zmienionych_bitow)}")
		i += 1


def uruchom(sciezka):
	with open(sciezka) as my_file:
		t = my_file.read().rstrip().split('\n')
	przyklady = t[3:]

	dlugosc_wiadomosci = int(t[0])
	ile_przykladow = int(t[1])
	max_zmienionych_bitow = int(t[2])

	odkoduj(dlugosc_jednej_wiadomosci=dlugosc_wiadomosci, ile_wiadomosci=ile_przykladow,
			max_zmienionych_bitow=max_zmienionych_bitow, przyklady=przyklady)


if __name__ == '__main__':
	path1 = "messages7.in.txt"
	path2 = "messages13.in.txt"
	path3 = "messages16.in.txt"
	uruchom(path1)
	uruchom(path2)
	uruchom(path3)
