import xlrd
import collections
data=xlrd.open_workbook(r"C:\Users\之子言归\Desktop\原创.xlsx")
table=data.sheets()[1]
row=table.nrows
class address(object):
    def __init__(self):
        self.s=""
        self.count=0
rs=collections.defaultdict(address)
for i in range(row):
    add=rs[table.cell(i,1).value]
    add.s+=table.cell(i,0).value+":"+table.cell(i,2).value+";"
    add.count+=1
    rs[table.cell(i, 1).value]=add
for i,add in rs.items():
    if add.count>1:
        print(i,"^",add.s[:-1])

