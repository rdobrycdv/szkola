class ulamek():
    def __init__(self, licznik=0, mianownik=1):
        self.licznik = licznik
        self.mianownik = mianownik
 
    def dodajUlamek(self, b):
        self.licznik = self.licznik * b.mianownik + b.licznik* self.mianownik
        self.mianownik=self.mianownik*b.mianownik
        
    def odejmijUlamek(self,b):
        self.licznik = self.licznik * b.mianownik - b.licznik* self.mianownik
        self.mianownik=self.mianownik*b.mianownik
        
    def pomnoz(self,x):
        self.licznik=self.licznik*x
        
    def pomnozulamek(self,b):
        self.licznik=self.licznik*b.licznik
        self.mianownik=self.mianownik*b.mianownik 
    
    def odwroc(self):
        kopia_licznik=self.licznik
        kopia_mianownik=self.mianownik
        self.licznik=kopia_mianownik
        self.mianownik=kopia_licznik
        
    def poteguj(self,n):
        self.licznik=int(self.licznik**n)
        self.mianownik=int(self.mianownik**n)
        
        
    def przeciwnosc(self):
        self.licznik=(-1)*self.licznik
    
        
    def wyswietl(self):
        return (self.licznik, self.mianownik)
    
    #b=ulamek(5,4)
    #a=ulamek(2,3)
    #a.wyswietl(x)
    #a.dodajUlamek(b)