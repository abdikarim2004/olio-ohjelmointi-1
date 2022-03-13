import random

class Asiakas:
"""
    :ivar nimi: asiakkaan nimi
    :type nimi: str

    :ivar ika: asiakkaan ikä
    :type ika: int
    
    :ivar asiakasnro: asiakasnumero, arvotaan
    :type asiakasnro: int[]
    
    Yksityiset metodit
        luo_nro()
"""

    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika
        self.luo_nro()
    
    def luo_nro(self):
       asiakasnro = random.randint(0,9)
       return (asiakasnro)

#________getters and setters____
    def get_nimi_ja_ika(self):
        return self.nimi, self.ika
    
    def set_nimi_ja_ika(self):
        if self.nimi == "": raise ValueError("Uusi nimi on annettava")
        else: pass

        if self.ika == "": raise ValueError("uusi ikä on annettava")
        else: pass
    
    def get_asiakasnro(self):
        self.asiakasnro = "{}{}-{}{}{}-{}{}{}".format(*[self.luo_nro for x in range(8)])
    
    


#

class Palvelu(Asiakas):
    """
    :ivar asiakkaat: asiakkaat lista joka alustetaan se tyhjäksi.
    :type nimi: str

    :ivar tuotenimi: Palvelu-luokan konstruktoorin parametri
    :type tuotenimi: str
    
    Julkiset metodit
        lisaa_asiakas(Asiakas)
        poista_asiakas(Asiakas)
        tulosta_asiakkaat()
    
    suojattu metodi
        luo_asiakasrivi(Asiakas): str
"""
    def __init__(self, tuotenimi):
        self.asiakkaat = []

    def luo_asiakasrivi(Asiakas):
        pass

    def lisaa_asiakas(self, Asiakas):
        self.asiakkaat.append(Asiakas)
        if Asiakas == "":
            raise ValueError("Asiakas on annettava.")
        
    def poista_asiakas(self, Asiakas):
        self.asiakkaat.remove(Asiakas)
        if Asiakas not in self.asiakkaat:
            pass

    def luo_asiakasrivi(self):
        print (f"{self.nimi} ({self.asiakasnro}) on {self.ika}-vuotias.")

    def tulosta_asiakkaat(self, Asiakas):
        for len in self.asiakkaat:
            return self.luo_asiakasrivi()




#

class ParempiPalvelu(Palvelu):
    """
    :ivar edut: 
    :type edut: str[]
    
    Julkiset metodit
        lisaa_etu(str)
        poista_etu(str)
        tulosta_edut()
"""

    def __init__(self, tuotenimi):
        self.tuotenimi = Palvelu.__init__(self, tuotenimi)
        self.edut = []
    
    def lisaa_etu(self):
        self.edut.append(Asiakas)
        if self.edut == "":
            raise ValueError("Asiakas on annettava.")

    def poista_etu(self):
        self.edut.remove(Asiakas)
        if Asiakas not in self.asiakkaat:
            pass

    def tulosta_edut(self):
        for len in self.asiakkaat:
            return self.luo_asiakasrivi()
