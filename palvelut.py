from multiprocessing.sharedctypes import Value
import random

class Asiakas:

    def __init__(self, nimi, ika):
        """Asiakas luokan konduktööri

    sijoittaa asiakkaan nimen, iän ja asiakasnumeron omiin muuttujiin

    :param nimi: asiakkaan nimi
    :type nimi: str
    :param ika: asiakkaan ikä
    :type ika: int
    """
        self.__nimi, self.__ika, self.__asiakasnro = nimi, ika, self.__luo_nro()
    
    def __luo_nro(self):
        """tallentaa kokonaisluvun väliltä 0-9 muuttujaan asiakasnumero.
        :return: muuttuja asiakasnumero
        :rtype: int
        """
        asiakasnumero = random.randint(0,9)
        return asiakasnumero

#__________getters_________
    def get_nimi(self):
        """palauttaa asiakkaan nimi"""
        return self.__nimi

    def get_ika(self):
        """palauttaa asiakkaan ikä"""
        return self.__ika

    def get_asiakasnro(self):
        """luo asiakasnro-nimisen muuttujan ja muotoilee sen 8 numeroksi, joista tulee asiakasnumero
        :return: muuttuja asiakasnro
        :rtype: int
        """
        asiakasnro = "{}{}-{}{}{}-{}{}{}".format(*[self.__luo_nro() for x in range(8)])
        return asiakasnro

#__________setters__________
    def set_nimi(self, __nimi):
        """tarkistaa jos nimi on annettu
        :param nimi: sisältää asiakkaan nimi
        :type nimi: variable/string
        """

        if self.__nimi == "": raise ValueError("Uusi nimi on annettava: ")
        else: self.__nimi = __nimi

    
    def set_ika(self):
        """tarkistaa jos ikä on annettu
        :param ika: sisältää asiakkaan ikä
        :type ika: int
        """

        if self.__ika == "": raise ValueError("uusi ikä on annettava: ")
        else: self.__ika = self.__ika
    


class Palvelu(Asiakas):

    def __init__(self, tuotenimi):
        """luo tyhjän listan nimeltä asiakkaat ja muuttujan nimeltä tuotenimi

        :param tuotenimi: muuttuja nimeltä tuotenimi
        :type tuotenimi: string
        """
        self.__asiakkaat, self.tuotenimi = [], tuotenimi

    def lisaa_asiakas(self, asiakas):
        """katsoo jos asiakas on asiakkaat -listassa, ja jos ei ole niin se lisää sen asiakkaat -listaan
        :param asiakas: asiakas
        :type asiakas: string/variable
        """
        if bool(asiakas):
            self.__asiakkaat.append(asiakas)
        else:
            raise ValueError("Asiakas on annettava: ")
        
    def poista_asiakas(self, asiakas):
        """poistaa asiakkaan asiakkaat -listalta, ja jos asiakas ei ole listassa niin se ohittaa
        :param asiakas: asiakas
        :type asiakas: string/variable
        """
        try:
            self.__asiakkaat.remove(asiakas)
        except ValueError:
            pass

    def _luo_asiakasrivi(self, asiakas):
        """luo asiakasrivin käyttämällä asiakkaan nimen, asiakasnumeron ja asiakkaan iän
        :param asiakas: asiakas
        :type asiakas: string/variable
        :return: asiakkaan nimi, asiakasnumero ja ikä
        :rtype: Union[int, string]
        """
        return f'{asiakas.get_nimi()} ({asiakas.get_asiakasnro()}) on {asiakas.get_ika()}-vuotias.'


    def tulosta_asiakkaat(self):
        """Tulostaa rivin jokaiselle asiakaaat -listalla olevalle asiakkaalle"""
        for asiakas in self.__asiakkaat:
            print(self._luo_asiakasrivi(asiakas))



class ParempiPalvelu(Palvelu):

    def __init__(self, tuotenimi):
        Palvelu.__init__(self, tuotenimi)
        self.__edut = []
    
    def lisaa_etu(self, Asiakas):
        """lisää edun edut- nimiseen listaan
        :param etu: etu
        :type etu: string/variable
        """
        self.__edut.append(Asiakas)
        if Asiakas == "":
            raise ValueError("Uusi asiakas on annettava: ")

    def poista_etu(self, etu):
        """poistaa etun edut -listalta, ja jos etu ei ole listassa niin se ohittaa
        :param etu: etu
        :type etu: string/variable
        """
        try:
            self.__edut.remove(etu)
        except ValueError:
            pass

    def tulosta_edut(self):
        """Tulostaa rivin jokaiselle edut -listalla olevalle etun"""
        print("Tuotteen", self.tuotenimi, "edut ovat:")
        for etu in self.__edut:
            print(etu)
