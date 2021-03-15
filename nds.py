chislo = int(input('Число с НДС: '))
nds = chislo / 120 * 20
beznds = chislo - nds
print('НДС: ', round(nds, 2),'\nБез НДС: ', round(beznds, 2))