import json


class Kunde():
    def __init__(self, fornavn: str, etternavn: str, tlf: int, epost: str):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.tlf = tlf
        self.epost = epost
    def visInfo(self):
        print(f'Hei {self.fornavn} {self.etternavn}. Vi vil kontakte deg via følgende kontaktinformasjon: tlf:{self.tlf}  epost:{self.epost}')


x=input('x:')
y=input('y:')
z=input('z:')
a=input('a:')
kunde1 = Kunde(x,y,z,a)

objekt = {
str(a) : {
'fornavn': kunde1.fornavn,
'etternavn': kunde1.etternavn,
'tlf': kunde1.tlf,
'epost': kunde1.epost}
}
with open('eposter.json', 'r') as file:
    for line in file:
        try:
            data = json.loads(line)
            if a in data:
                print('Brukeren eksisterer allerede')
            else:
                with open('eposter.json', 'a') as json_file:
                    json.dump(a, json_file)
                    json_file.write('\n')

                with open('brukere.json', 'a') as json_file:
                    json.dump(objekt, json_file)
                    json_file.write('\n')
        except json.JSONDdecodeError as e:
            print(e)
with open('brukere.json', 'a') as json_file:
    json.dump(lagre_kunde, json_file)
    json_file.write('\n')

with open('brukere.json', 'r') as json_file:
    json_data = json.load(json_file)
navn = json_data['fornavn']
print(navn)



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



