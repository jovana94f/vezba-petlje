pocetna_pozicija = 0
cilj = 100
# .               .
trenutna_pozicija = 0
brzina = 20

for x in range(10):
    print(trenutna_pozicija)
    if trenutna_pozicija == cilj:
        print("stigao do cilja.")
    elif trenutna_pozicija > cilj:
        print("prosli ste")
    elif trenutna_pozicija < cilj:
        print("niste jos stigli.")
    trenutna_pozicija += brzina