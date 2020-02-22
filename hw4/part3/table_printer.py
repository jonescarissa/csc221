''' Table Printer practice project
Author: Carissa Jones
'''

tableData = [['I', 'out', 'chair.'],
            ['just', 'of', 'Im'],
            ['fell', 'my', 'fine.']]

    
def printTable(tableData):
    '''Given list of strings, tableData, displays in a well-organized
        table with each column right-justified'''
    colWidths = [0] * len(tableData)

    for x in range(len(tableData[0])):
        for y in range(len(colWidths)):
            print(tableData[y][x].rjust(colWidths[y]), end= ' ')
        print(end='\n')

printTable(tableData)

         

