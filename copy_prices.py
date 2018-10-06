import xlrd

DieselPricesWorkbook=xlrd.open_workbook('Diesel price in Chennai.xlsx')
WorkSheet=DieselPricesWorkbook.sheet_by_index(0)

DieselPrices=[]

for i in range(3,457):
	DieselPrices.append(WorkSheet.cell(i,6).value)
	
#print(DieselPrices)
del DieselPricesWorkbook

PetrolPricesWorkbook=xlrd.open_workbook('Petrol price in Chennai.xlsx')
WorkSheet=PetrolPricesWorkbook.sheet_by_index(0)

PetrolPrices=[]

for i in range(3,454):
	PetrolPrices.append(WorkSheet.cell(i,5).value)
	
#print (PetrolPrices)

print (len(PetrolPrices)-len(DieselPrices))
	

