import json

class Billett():
    def __init__(self, forestilling: str, dato: str, honnor: int, voksen:int, student: int, barn: int, standarpris = 300):
        self.forestilling = forestilling
        self.dato = dato
        self.voksen = voksen
        self.honnor = honnor
        self.student = student
        self.barn = barn
        self.standarpris = standarpris
    def beregn_pris(self):
        totalsum = 0
        pris = self.standarpris
        totalsum += (pris - ((pris/100)*30))*self.honnor
        totalsum += pris * self.voksen
        totalsum += (pris - ((pris/100)*20))*self.student
        totalsum += (pris - ((pris/100)*50))*self.barn
        return totalsum
    def visInfo(self):
        print(f'Du har bestillt følgende privat-billetter: Honnør:{self.honnor}  Student:{self.student}  Barn:{self.barn}. Du la inn datoen:{self.dato} til forestillingen: {self.forestilling}')

    def eksporter_bestilling(self, filnavn):
        bestilling_dict = {
            'bestilling' : {
                self.dato : {
                    'forestilling' : self.forestilling,
                    'honnørbilletter' : self.honnor,
                    'studentbilletter' : self.student,
                    'barnebilletter' : self.barn,
                    'voksenbilletter' : self.voksen,
                    'pris' : self.beregn_pris()
                }
            }
        }
        with open(filnavn, 'a') as json_file:
            json_file.write('\n')
            json_file.write(json.dumps(bestilling_dict, indent=2))
    #def importer(self, filnavn):




epost = 'a'
#Print forestillinger
forestilling = input('Hvilken forestilling du bestille for? ')
#Print ledige datoer
dato = input(f'Hvilken dato vil du se {forestilling} på? ')
#Skjekk om datoen er gyldig

honnor = int(input('Hvor mange honnørbilletter skal du ha? '))
voksen = int(input('Hvor mange voksenbilletter skal du ha? '))
student = int(input('Hvor mange studentbilletter skal du ha? '))
barn = int(input('Hvor mange barnebilletter skal du ha? '))

antall_billetter = honnor + voksen + student + barn

ny_billett = Billett(forestilling, dato, honnor, voksen, student, barn)

ny_billett.eksporter_bestilling(epost + '.json')






