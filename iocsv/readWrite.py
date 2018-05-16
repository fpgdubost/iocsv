import csv
          
def saveListCsv(list_csv, path):
    with open(path, 'wb') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        for val in list_csv:
            wr.writerow([val])
            
def saveListCsvMultiCol(list_csv_MultiCol, path):
    with open(path, 'wb') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        for i in range(len(list_csv_MultiCol)):  
            wr.writerow(list_csv_MultiCol[i]) 
                  
def readListCsv(path):                    
    files = []
    with open(path,'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            files.append(row[0])
    return files   
    
def readListCsvMultiCol(path,isFloat=False):
    list_csv = []
    with open(path,'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            list_csv.append(row)
    #cast to float
    if isFloat:
        list_csv = castTofloat(list_csv)
    return list_csv    
    
def castTofloat(list_csv):
    #cast strings to float
    for i in range(len(list_csv)):
        for j in range(len(list_csv[i])):
            list_csv[i][j] = list_csv[i][j][1:-1].split(',')
            #cast to float
            list_csv[i][j] = [float(coord) for coord in list_csv[i][j]]  
    return list_csv
