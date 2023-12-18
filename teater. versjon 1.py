import json

class Billett():
    def __init__(self, forestilling: str, dato: str, honnor: int, student: int, barn: int, standarpris = 300):
        self.forestilling = forestilling
        self.dato = dato
        self.honnor = honnor
        self.student = student
        self.barn = barn
        self.standarpris = standarpris
    def beregn_pris(self):
        totalsum = 0
        pris = self.standarpris
        totalsum += (pris - ((pris/100)*30))*self.honnor
        totalsum += (pris - ((pris/100)*20))*self.student
        totalsum += (pris - ((pris/100)*50))*self.barn
        return totalsum
    def visInfo(self):
        print(f'Du har bestillt følgende privat-billetter: Honnør:{self.honnor}  Student:{self.student}  Barn:{self.barn}. Du la inn datoen:{self.dato} til forestillingen: {self.forestilling}')

class Sal():
    def __init__(self, navn:str, plass: int, forestilling = ''):
        self.plass = plass
        self.forestilling = forestilling
    def visInfo(self):
        print(self.plass, self.forestilling)

class Forestilling():
    def __init__(self, navn: str, sal: str, dato: list, tidspunkt= 19.00):
        self.navn = navn
        self.tidspunkt = tidspunkt
        self.sal = sal
    def visInfo(self):
        print(self.navn, self.tidspunkt, self.sal)

de_elendige = Forestilling('de elendige', 'gull', ['0'])

vildanden = Forestilling('vildanen', 'solv', ['0'])



gull = Sal('gull', 150, 'de elendige')
solv = Sal('sølv', 100, 'vildanden')
bronse = Sal('bronse', 50)

class Kunde():
    def __init__(self, fornavn: str, etternavn: str, tlf: int, epost: str):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.tlf = tlf
        self.epost = epost
    def visInfo(self):
        print(f'Hei {self.fornavn} {self.etternavn}. Vi vil kontakte deg via følgende kontaktinformasjon: tlf:{self.tlf}  epost:{self.epost}')


var=[]
a=input('a:')


with open('eposter.json', 'r') as file:
    for linje in file:
        try:
            data = json.loads(linje)
            if a in data:
                var.append(1)
            else:
                var.append(2)
        except json.JSONDecodeError:
            print()

if not(1 in var):
    x=input('x:')
    y=input('y:')
    z=input('z:')
    kunde1 = Kunde(x,y,z,a)
    objekt = {
    str(a) : {
    'fornavn': kunde1.fornavn,
    'etternavn': kunde1.etternavn,
    'tlf': kunde1.tlf,
    'epost': kunde1.epost}
    }
    with open('eposter.json', 'a') as json_file:
        json_file.write('\n')
        json.dump(a, json_file)
    with open('brukere.json', 'a') as json_file:
        json_file.write('\n')
        json.dump(objekt, json_file)
    var = ''



forestilling = input('Hvilken forestilling vil du plassere en bestilling for?')










