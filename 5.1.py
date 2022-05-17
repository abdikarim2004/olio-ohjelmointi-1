class Laskija:
    """Luokka, joka toteuttaa eri laskutoimituksia kahdelle luvulle.

    Julkiset metodit:
        summaa(Union[int, float], Union[int, float])
        kerro(Union[int, float], Union[int, float])
    """

    def summaa(self, a, b):
        """Palauttaa kahden luvun summan.

        :param a: summan ensimmäinen luku
        :type a: Union[int, float]
        :param b: summan toinen luku
        :type b: Union[int, float]
        :return: lukujen a ja b summa
        :rtype: Union[int, float]
        """
        return sum([a, b])

    def kerro(self, a, b):
        """Palauttaa kahden luvun tulon.

        :param a: tulon ensimmäinen luku
        :type a: Union[int, float]
        :param b: tulon toinen luku
        :type b: Union[int, float]
        :return: lukujen a ja b tulo
        :rtype: Union[int, float]
        """
        tulo = 1
        for luku in [a, b]:
            tulo *= luku
        return tulo


### Lisää MonenLaskija ja argumenttien_tulostaja tähän.
class MonenLaskija(Laskija):
    """Luokka, joka toteuttaa eri laskutoimituksia mille tahansa määrälle
       lukuja.

    Julkiset metodit:
        summaa(Union[int, float], ...)
        kerro(Union[int, float], ...)
    """

    def summaa(self, *luvut):
        """Palauttaa annettujen lukujen summan.

        :param luvut: summattavat luvut
        :type luvut: tuple[Union[int, float]]
        :return: lukujen summa
        :rtype: Union[int, float]
        """
        return sum(luvut)

    def kerro(self, *luvut):
        """Palauttaa annettujen lukujen tulon.

        :param luvut: kerrottavat luvut
        :type luvut: tuple[Union[int, float]]
        :return: lukujen tulo
        :rtype: Union[int, float]
        """
        tulo = 1
        for luku in luvut:
            tulo *= luku
        return tulo


def argumenttien_tulostaja(**purettavat):
    """Tulostaa annetut tiedot."""
    for k, v in purettavat.items():
        print(f'Argumentin "{k}" arvo on {v}.')


### Seuraavat rivit tekevät tarkistustulostukset. Älä koske niihin.

l = Laskija()
ml = MonenLaskija()

print(l.summaa(11, 31))
print(l.kerro(3, 12))
print()
print(ml.summaa(1, 2, 3, 4, 5))
print(ml.kerro(1, 2, 3, 4, 5))
print()
print(ml.summaa(1, 2, 3, 4, 5, 6, 7))
print(ml.kerro(1, 2, 3, 4, 5, 6 ,7))
print()
argumenttien_tulostaja(eka=42, toka='foo', kolmas=[0, 1, 2])
print()
argumenttien_tulostaja(nimi='Tero', ika=41, kaupunki='Turku', oppilaitos='TAI')