import openpyxl


wb = openpyxl.load_workbook('LedigDato.xlsx')
sheet = wb.active



while True:
    forestilling = input('Hvilken forestilling vil du se? ')

    if forestilling.lower() == 'de elendige':
        coloumn_to_print = 'A'
    elif forestilling.lower() == 'vildanden':
        coloumn_to_print = 'D'

    for cell in sheet[coloumn_to_print]:
            print(cell.value)

    antall_billetter = int(input('Hvor mange billetter? '))
    if antall_billetter > 0:
        dato = int(input('Hvilken dag i februar? '))
        if antall_billetter <= sheet['C' + str(dato+1)].value:
            temp_plass = sheet['C' + str(dato+1)].value
            print(temp_plass)
            sheet['C' + str(dato+1)] = temp_plass - antall_billetter
            print(sheet['C' + str(dato+1)].value)
            break
        else:
            svar = input(f'De er ingen ledige forestillinger for {forestilling} for {dato}.februar. Vil du velge et annet tidspunkt? (J/N) ')
            if svar.upper()[0] == 'J':
                True
            else:
                break
    else:
        print('Du må bestille minst 1 billett')

    wb.save('LedigDato.xlsx')
