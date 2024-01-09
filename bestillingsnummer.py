import openpyxl
def bestillingsnummer_func(filnavn):
    workbook = openpyxl.load_workbook(filnavn + ".xlsx")
    sheet = workbook.active
    try:
        sheet["H2"] = sheet["H2"].value + 1
    except TypeError:
        sheet["H2"] = 2

    workbook.save(filnavn + ".xlsx")
    return sheet["H2"].value

