import json
import openpyxl

# Klasser
class Kunde:
    def __init__(self, fornavn: str, etternavn: str, tlf: int, epost: str):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.tlf = tlf
        self.epost = epost

    def visInfo(self):
        print(
            f"Hei {self.fornavn} {self.etternavn}. Vi vil kontakte deg via følgende kontaktinformasjon; tlf:{self.tlf}  epost:{self.epost}"
        )

    def opprett_bruker(self, filnavn):
        kunde_dict = {
            "bruker": {
                self.epost: {
                    "fornavn": self.fornavn,
                    "etternavn": self.etternavn,
                    "tlf": self.tlf,
                    "epost": self.epost,
                }
            }
        }
        with open(filnavn, "w") as json_file:
            json_file.write(json.dumps(kunde_dict, indent=2))

    def eksporter_bruker(self, filnavn):
        kunde_dict = {
            self.epost: {
                "fornavn": self.fornavn,
                "etternavn": self.etternavn,
                "tlf": self.tlf,
                "epost": self.epost,
            }
        }
        with open(filnavn, "a") as json_file:
            json_file.write(json.dumps(kunde_dict, indent=2))
            json_file.write("\n")

    def eksporter_epost(self, filnavn):
        with open(filnavn, "a") as json_file:
            json_file.write(json.dumps(self.epost, indent=2))
            json_file.write("\n")


class Billett:
    def __init__(
        self,
        forestilling: str,
        dato: str,
        honnor: int,
        voksen: int,
        student: int,
        barn: int,
        standarpris=300,
    ):
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
        totalsum += (pris - ((pris / 100) * 30)) * self.honnor
        totalsum += pris * self.voksen
        totalsum += (pris - ((pris / 100) * 20)) * self.student
        totalsum += (pris - ((pris / 100) * 50)) * self.barn
        return totalsum

    def visInfo(self):
        print(
            f"Du har bestillt følgende privat-billetter: Honnør:{self.honnor}  Student:{self.student}  Barn:{self.barn}. Du la inn datoen:{self.dato} til forestillingen: {self.forestilling}"
        )

    def eksporter_bestilling(self, filnavn):
        bestilling_dict = {
            "bestilling": {
                self.dato: {
                    "forestilling": self.forestilling,
                    "honnørbilletter": self.honnor,
                    "studentbilletter": self.student,
                    "barnebilletter": self.barn,
                    "voksenbilletter": self.voksen,
                    "pris": self.beregn_pris(),
                }
            }
        }
        with open(filnavn, "a") as json_file:
            json_file.write("\n")
            json_file.write(json.dumps(bestilling_dict, indent=2))


# Variabler
var = []

wb = openpyxl.load_workbook("LedigDato.xlsx")
sheet = wb.active


# Registrering av bruker
epost = input("Hvilken email skal brukeren registreres under? ")
fornavn = input("Hvilket fornavn skal brukeren registres under? ")
etternavn = input("Hvilket etternavn skal brukeren registres under? ")
tlf = input("Hvilket telefonnummer skal knyttes oppmot brukeren? ")

ny_kunde = Kunde(fornavn, etternavn, tlf, epost)
ny_kunde.eksporter_bruker("brukere.json")
ny_kunde.opprett_bruker(epost + ".json")
ny_kunde.eksporter_epost("eposter.json")

# Finner ledige datoer
while True:
    forestilling = input("Hvilken forestilling vil du se? ")

    if forestilling.lower() == "de elendige":
        coloumn_to_print = "A"
    elif forestilling.lower() == "vildanden":
        coloumn_to_print = "C"
    print(f"Her er ledige datoer for {forestilling}:")
    for cell in sheet[coloumn_to_print]:
        print(cell.value)
    honnor = int(input("Hvor mange honnørbilletter (over 67 år) skal du ha? "))
    voksen = int(input("Hvor mange voksenbilletter skal du ha? "))
    student = int(input("Hvor mange studentbilletter skal du ha? "))
    barn = int(input("Hvor mange barnebilletter skal du ha? "))
    antall_billetter = honnor + voksen + student + barn
    
    
    if forestilling.lower() == "vildanden":
        if antall_billetter > 0:
            dato = int(input("Hvilken dag i februar? "))
            if antall_billetter <= sheet["D" + str(dato + 1)].value:
                temp_plass = sheet["D" + str(dato + 1)].value
                print(temp_plass)
                sheet["D" + str(dato + 1)] = temp_plass - antall_billetter
                print(sheet["D" + str(dato + 1)].value)
                break
            else:
                svar = input(
                    f"De er ingen ledige forestillinger for {forestilling} for {dato}.februar. Vil du velge et annet tidspunkt? (J/N) "
                )
                if svar.upper()[0] == "J":
                    True
                else:
                    break
                
    if forestilling.lower() == "de elendige":
        if antall_billetter > 0:
            dato = int(input("Hvilken dag i februar? "))
            if antall_billetter <= sheet["B" + str(dato + 1)].value:
                temp_plass = sheet["B" + str(dato + 1)].value
                print(temp_plass)
                sheet["B" + str(dato + 1)] = temp_plass - antall_billetter
                print(sheet["B" + str(dato + 1)].value)
                break
            else:
                svar = input(
                    f"De er ingen ledige forestillinger for {forestilling} for {dato}.februar. Vil du velge et annet tidspunkt? (J/N) "
                )
                if svar.upper()[0] == "J":
                    True
                else:
                    break
    
wb.save("LedigDato.xlsx")


# Lager billetten
antall_billetter = honnor + voksen + student + barn
ny_billett = Billett(forestilling, dato, honnor, voksen, student, barn)
ny_billett.eksporter_bestilling(epost + ".json")
