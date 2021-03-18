from ver01.parser import *
from ver01.script import *
import sqlite3
conn = sqlite3.connect('data.db')
cur = conn.cursor()

x = Parser()
data = x.get_data()

data2 = data_clean(data)

dttir, numtir, numbers, dopnum, num, num2 = [] , [], [], [], [], []


for x in data:
    y = str(x).strip('[]')
    z = y.replace('<div class="elem">', '')
    z = z.replace('<div class="main">','')
    z = z.replace('div class="draw_date" title="','')
    z = z[27:]
    dttir.append([z[0:19]])
    z = z[78:]
    numtir.append([int(z[0:5])])
    z = z[125:]
    numbers.append(z[0:z.index('span')])
    z = z[120:]
    dopnum.append([int(z[z.index('tra">')+5:z.index('tra">')+6])])
for s in numbers:
    a = str(s).strip('[]')
    b = a.replace('<b>','')
    b = b.replace('xa0</b>','')
    b = b.replace('n','')
    b = b.replace('\\','!-')
    b = b.replace('</','')
    b = b.split('!-!-')
    b.pop(-1)
    for x in range(0, len(b)):
        num2.append(int(b[x]))
    num.append(num2)
    num2 = []


big_data = []
datas=[]
id = 0
if len(dttir) == len(numtir) == len(num) == len(dopnum):
    for x in range(0,len(numbers)):
        s1 = numtir[x]
        s2 = dopnum[x]
        datas += (int(str(s1)[1:-1]), str(dttir[x])[2:-2], str(num[x])[1:-1], int(str(s2)[1:-1]))
        #cur.execute("INSERT INTO arh_tirag VALUES(?, ?, ?, ?, ?);", datas)
        #conn.commit()
        big_data.append([int(str(s1)[1:-1]), str(dttir[x])[2:-2], num[x], int(str(s2)[1:-1])])
        #print(numtir[x],dttir[x],num[x],dopnum[x])
        #print(datas)
        datas = ()
#print(*big_data)

def analiz_num(data):
    c = []
    count =0
    for x in range(1,21):
        for s in data:
            m = s[2]
            for z in range(0,len(m)):
                if m[z] == x:
                    count += 1
        procent = count / len(data)*100
        c.append([x, procent]) # x - число от 1 до 20, procent - процент совпадений за последнии n  тиражей( чем выше просент тем чаще число выпадает
        count = 0

    return c

print(analiz_num(big_data))
