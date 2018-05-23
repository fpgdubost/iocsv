import iocsv
import numpy as np

#list of strings single column
list_strings = ["ex1","ex2","ex3"]
iocsv.saveListCsv(list_strings,"list_strings.csv")
list_strings = iocsv.readListCsv("list_strings.csv")

#table of ints
table = np.reshape(range(20),[4,5])
iocsv.saveListCsvMultiCol(table,"table.csv")
table = iocsv.readListCsvMultiCol("table.csv","int")

#table rows of different length
table_diff_len = [[4.55],
                  [5.55,5.63],
                  [4.52]]
iocsv.saveListCsvMultiCol(table_diff_len,"table_diff_len.csv")
table_diff_len = iocsv.readListCsvMultiCol("table_diff_len.csv") 

#list of 2D coordinates (easy to create with loops and list.append())
list_coord2D = [[[4.55,4.63]],
                [[5.55,5.63],[6.55,6.63]],
                [[6.55,6.63],[6.55,6.63],[6.55,6.63]]]
iocsv.saveListCsvMultiCol(list_coord2D,"list_coord2D.csv")
list_coord2D = iocsv.readListCsvMultiCol("list_coord2D.csv","coord")

#list of 3D coordinates (easy to create with loops and list.append())
list_coord3D = [[[4.55,4.63,4.52]],
                [[5.55,5.63,5.52],[6.55,6.63,6.52]],
                [[6.55,6.63,6.52],[6.55,6.63,6.52],[6.55,6.63,6.52]]]
iocsv.saveListCsvMultiCol(list_coord3D,"list_coord3D.csv")
list_coord3D = iocsv.readListCsvMultiCol("list_coord3D.csv","coord")




