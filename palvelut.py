import random
#_____________________________________________________________#

class Asiakas:
    
    def __init__(self, nimi, ika):
        """Asiakas luokan konduktööri
        sijoittaa asiakkaan nimen, iän ja asiakasnumeron omiin muuttujiin
        :param nimi: asiakkaan nimi
        :type nimi: str
        :param ika: asiakkaan ikä
        :type ika: int
        """

        self.nimi = nimi
        self.ika = ika
        self.asiakasnumero = self.luo_nro()
    
    def luo_nro(self):
        """ tallentaa kokonaisluvun väliltä 0-9 muuttujaan nro.
        :return: muuttuja asiakasnumero
        :rtype: int
        """

        nro = random.randint(0,9)
        return nro
        
    #__________getters_________

    def getnimi(self):
        """ palauttaa asiakkaan nimi"""

        return self.nimi
    
    def getika(self):
        """palauttaa asiakkaan ikä"""

        return self.ika

    def getasiakasnumero(self):
        """luo asiakasnumero-nimisen muuttujan ja muotoilee sen 8 numeroksi, joista tulee asiakasnumero
        :return: muuttuja asiakasnumero
        :rtype: int
        """

        asiakasnumero = "{}{}-{}{}{}-{}{}{}".format(*[Asiakas.luo_nro(self)for x in range(8)])
        return asiakasnumero

#__________setters__________

    def set_nimi(self, nimi):
        """ tarkistaa jos nimi on annettu
        :param nimi: sisältää asiakkaan nimi
        :type nimi: variable/string
        """

        if nimi == True:
            self.nimi = nimi 
        else:
            raise ValueError("Uusi nimi on annettava")
        
    def set_ika(self, ika):
        """ tarkistaa jos ikä on annettu
        :param ika: sisältää asiakkaan ikä
        :type ika: int
        """

        if ika == int:
            self.ika = ika
        else:
            raise ValueError("Uusi ikä on annettava")

#_____________________________________________________________#

class Palvelu:

    def __init__(self, tuotteennimi):
        """luo tyhjän listan nimeltä asiakkaat ja muuttujan nimeltä tuotteennimi
        :param tuotteennimi: muuttuja nimeltä tuotteennimi
        :type tuotteennimi: string
        """

        self.asiakkaat = []
        self.tuotteennimi = tuotteennimi

    def lisaa_asiakas(self, asiakas):
        """ katsoo jos asiakas on asiakkaat -listassa, ja jos ei ole niin se lisää sen asiakkaat -listaan
        :param asiakas: asiakas
        :type asiakas: string/variable
        """

        if bool(asiakas):
            self.asiakkaat.append(asiakas)
        else:
            raise ValueError("Asiakas on annettava.")

    def poista_asiakas(self, asiakas):
        """ poistaa asiakkaan asiakkaat -listalta, ja jos asiakas ei ole listassa niin se ohittaa
        :param asiakas: asiakas
        :type asiakas: string/variable
        """

        try:
            self.asiakkaat.remove(asiakas)
        except ValueError:
            pass

    def luo_asiakasrivi(self, asiakas):
        """ luo asiakasrivin käyttämällä asiakkaan nimen, asiakasnumeron ja asiakkaan iän
        :param asiakas: asiakas
        :type asiakas: string/variable
        :return: asiakkaan nimi, asiakasnumero ja asiakkaan ikä
        :rtype: Union[int, string]
        """

        return f'{Asiakas.getnimi(asiakas)} ({Asiakas.getasiakasnumero(asiakas)}) on {Asiakas.getika(asiakas)}-vuotias.'

    def tulosta_asiakkaat(self):
        """ Tulostaa rivin jokaiselle asiakaaat -listalla olevalle asiakkaalle"""

        print("Tuotteen", self.tuotteennimi, "asiakkaat ovat:")
        for asiakas in self.asiakkaat:
            print(self.luo_asiakasrivi(asiakas))
        print()

#_____________________________________________________________#

class ParempiPalvelu(Palvelu):

    def __init__(self, tuotteennimi):
        self.edut = []
        Palvelu.__init__(self,tuotteennimi)

    def lisaa_etu(self, etu):
        """lisää edun edut- nimiseen listaan
        :param etu: etu
        :type etu: string/variable 
        """
        self.edut.append(etu)

    def poista_etu(self, etu):
        """ poistaa etun edut -listalta, ja jos etu ei ole listassa niin se ohittaa
        :param etu: etu
        :type etu: string/variable
        """
        try:
            self.edut.remove(etu)   
        except ValueError:
            pass

    def tulosta_edut(self):
        """ tulostaa rivin jokaiselle edut -listalla olevalle etun
        """
        print("Tuotteen", self.tuotteennimi, "edut ovat:")
        for etu in self.edut:
            print(etu)
