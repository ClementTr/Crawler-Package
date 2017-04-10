import pandas as pd
from os.path import split
import mypkg

class MonExceptionRange(Exception):
    def __init__(self,raison):
        self.raison = raison    
    def __str__(self):
        return self.raison

class MonExceptionSort(Exception):
    def __init__(self,raison):
        self.raison = raison    
    def __str__(self):
        return self.raison

    
def exceptionCatcher(mydf, oldcolumn, newcolumnName, tab, value):
    if len(tab) != len(value):
        raise MonExceptionRange("Issue of range")
    elif tab != sorted(tab):
        raise MonExceptionSort("Table not sorted")
    else:
        mydf[newcolumnName] = "test"
        for z in range(len(tab)):
            mydf.loc[((oldcolumn >= tab[z-len(tab)]) & (oldcolumn <= tab[z-len(tab)+1])), newcolumnName] = value[z]
        
        mydf.loc[oldcolumn > tab[-1], newcolumnName] = value[-1]
        return mydf
        


def scalefunc(mydf, oldcolumn, newcolumnName, tab, value):
    '''You have to enter 5 parameters, 
    mydf: your dataframe
    oldcolumn: the mydf.column_you_want_to_scale
    newcolumn: string: colonne name
    tab: value integer of your separations
    value: value returned in the new column
    '''
    try:
        return exceptionCatcher(mydf, oldcolumn, newcolumnName, tab, value)
    except(MonExceptionRange):
        print("len(tab) != len(value) : Out of range")
    except(MonExceptionSort):
        print("tab != sorted(tab) : Table not sorted")




