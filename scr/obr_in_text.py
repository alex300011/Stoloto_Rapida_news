import time
start_time = time.time()
l=[]
text = []
def loadfile():
    l = []
    with open('from_stoloto_rapido2.0.txt', encoding="utf-8") as f:
        l = f.read().splitlines()
    return l

def savefile2():
    MyFile = open('совпадения_from_Rapido_Stoloto.txt', 'w')
    for element in text1:
        MyFile.write(str(element))
        MyFile.write('\n')
    MyFile.close()
    print('saveFIle')


print('----start----',start_time)
l = loadfile()
print('l==',l)
print('длинна списка = ',len(l))
i = 0
while i != len(l):
#for i in range(0,len(l)):

    if 'Суперприз' in l[i]:
        del l[i]
    if 'февраль' in l[i]:
        del l[i]
    if '⚲' in l[i]:
        del l[i]
    i += 1

print ('l==',l)
for h in range(1,len(l),3):
    text.append(l[h])

print('text=',text)

lst = []
lst2 = []
z = []
for i in text:
    z.append(i.split('  '))
    for f in z[0]:
        v = int(f)
        lst2.append(v)
    lst = lst + [lst2]
    lst2 = []
    z = []
print('lst=',lst)

for i in range(0,len(lst)):
    del lst[i][-1]

print (len(lst[0]))

while True:
    if input('1.stop-->') == '1':
        break
text1 = []
num = 0
lst3 = []
count = 0
for x in lst:

    #print(x[0])
    for y in lst:
        if x[0] in y:
            lst3 = lst3 + [y]

    #print(lst3)

    #print(x[1])
    lst4=[]
    for y in lst3:
        if x[1] in y:
            lst4 = lst4 + [y]
    #print('lst4',lst4)

    #print(x[2])
    lst5=[]
    for y in lst4:
        if x[2] in y:
            lst5 = lst5 + [y]
    #print('lst5',lst5)

    #print(x[3])
    num = 0
    lst6=[]
    for y in lst5:
        if x[3] in y:
            lst6 = lst6 + [y]
            num += 1
    #print('all',num,'lst6',lst6)

    #print(x[0], x[1], x[2], x[3], x[4])
    num = 0
    lst7=[]
    for y in lst6:
        if x[4] in y:
            lst7 = lst7 + [y]
            num += 1
    #print('all',num,'lst7',lst7)

    #print(x[0], x[1], x[2], x[3], x[4], x[5])
    num = 0
    lst8=[]
    for y in lst7:
        if x[5] in y:
            lst8 = lst8 + [y]
            num += 1
    #print('all',num,'lst8',lst8)

    #print(x[0], x[1], x[2], x[3], x[4], x[5], x[6])
    num = 0
    lst9=[]
    for y in lst8:
        if x[6] in y:
            lst9 = lst9 + [y]
            num += 1
    #print('all',num,'lst9',lst9)

    #print(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7])
    numall = 0
    lst10=[]
    for y in lst9:
        if x[7] in y:
            lst10 = lst10 + [y]
            numall += 1
    #('100% Совпадения',numall,'lst10',lst10)
    count += 1
    print(f"комбинация {count} из {len(lst)} -- Для комбинации {x} всего совпадения {numall} из {len(lst)} возможных комбинаций")
    text1 = text1 +[['для комбинации:'] + [x] + ['Всего совпадений'] + [numall] + ['Список совпадений'] + [lst10]]
    print((time.time() - start_time), "seconds")
print(text1)
savefile2()