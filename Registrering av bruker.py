import json

#Klasser
class Kunde():
    def __init__(self, fornavn: str, etternavn: str, tlf: int, epost: str):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.tlf = tlf
        self.epost = epost
    def visInfo(self):
        print(f'Hei {self.fornavn} {self.etternavn}. Vi vil kontakte deg via følgende kontaktinformasjon; tlf:{self.tlf}  epost:{self.epost}')

    def opprett_bruker(self, filnavn):
        kunde_dict = {
            'bruker' : {
                self.epost: {
                    'fornavn': self.fornavn,
                    'etternavn': self.etternavn,
                    'tlf': self.tlf,
                    'epost': self.epost
                }
            }
        }
        with open(filnavn, 'w') as json_file:
            json_file.write(json.dumps(kunde_dict, indent=2))

    def eksporter_bruker(self, filnavn):
        kunde_dict = {
            self.epost: {
                'fornavn': self.fornavn,
                'etternavn': self.etternavn,
                'tlf': self.tlf,
                'epost': self.epost
            }
        }
        with open(filnavn, 'a') as json_file:
            json_file.write(json.dumps(kunde_dict, indent=2))
            json_file.write('\n')


    def eksporter_epost(self, filnavn):
        with open(filnavn, 'a') as json_file:
            json_file.write(json.dumps(self.epost, indent=2))
            json_file.write('\n')



#Variabler
var=[]

#Registrering av bruker
epost = input('Hvilken email skal brukeren registreres under? ')


fornavn = input('Hvilket fornavn skal brukeren registres under? ')
etternavn =input('Hvilket etternavn skal brukeren registres under? ')
tlf = input('Hvilket telefonnummer skal knyttes oppmot brukeren? ')

ny_kunde = Kunde(fornavn, etternavn, tlf, epost)
ny_kunde.eksporter_bruker('brukere.json' )
ny_kunde.opprett_bruker(epost + '.json')
ny_kunde.eksporter_epost('eposter.json')

'''
with open('eposter.json', 'r') as json_file:
    for linje in json_file:
        try:
            data = json.loads(linje)
            if epost in data:
                var.append(1)
            else:
                var.append(2)
        except json.JSONDecodeError:
            print()

if not(1 in var):
'''












