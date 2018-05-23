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
    
def readListCsvMultiCol(path,dtype='float',isListCoord=False):
    if not dtype in ['string','int','float','coord']:
	raise ValueError("incorrect type: " + dtype)
    list_csv = []
    with open(path,'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            list_csv.append(row)
    #cast
    if dtype in ['int','float','coord']:
        list_csv = cast(list_csv,dtype)

    return list_csv    

def cast(list_csv,dtype):
    #cast strings to float
    for i in range(len(list_csv)):
        for j in range(len(list_csv[i])):
            #cast to float
	    if dtype == "float":
                list_csv[i][j] = float(list_csv[i][j])
            elif dtype == 'int':
                list_csv[i][j] = int(list_csv[i][j])
	    elif dtype == 'coord':
		list_csv[i][j] = list_csv[i][j][1:-1].split(',')
                #cast to float
                list_csv[i][j] = [float(coord) for coord in list_csv[i][j]]
	    else:
		print "incorrect type: " + dtype
    return list_csv







