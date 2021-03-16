from ver01.parser import *
from ver01.script import *

x = Parser()
data = x.get_data()

data2 = data_clean(data)

dttir, numtir, numbers, dopnum, num = [] , [], [], [], []


for x in data:
    y = str(x).strip('[]')
    z = y.replace('<div class="elem">', '')
    z = z.replace('<div class="main">','')
    z = z.replace('div class="draw_date" title="','')
    z = z[27:]
    dttir.append([z[0:19]])
    z = z[78:]
    numtir.append([z[0:5]])
    z = z[125:]
    numbers.append(z[0:z.index('span')])
    z = z[120:]
    dopnum.append([z[z.index('tra">')+5:z.index('tra">')+6]])
for s in numbers:
    a = str(s).strip('[]')
    b = a.replace('<b>','')
    b = b.replace('xa0</b>','')
    b = b.replace('n','')
    b = b.replace('\\','!-')
    b = b.replace('</','')
    b = b.split('!-!-')
    b.pop(-1)
    num.append(b)
print(len(dttir), len(numtir), len(num), len(dopnum))

big_data = []
if len(dttir) == len(numtir) == len(num) == len(dopnum):
    for x in range(0,len(numbers)):
        big_data.append([numtir[x],dttir[x],num[x],dopnum[x]])
        print(numtir[x],dttir[x],num[x],dopnum[x])
print(big_data[0])
