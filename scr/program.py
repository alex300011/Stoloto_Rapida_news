import time
start_time = time.time()
l=[]
text = []

def get_data_from_site(): # тут должен быть парсер в будущем
    pass

def loadfile(): #Загрузка данных из файла.
    l = []
    with open('../from_stoloto_rapido2.0.txt', encoding="utf-8") as f:
        l = f.read().splitlines()
    return l

def savefile2(): #Сохранение верисия 1
    MyFile = open('../совпаденияRapido.txt', 'w')
    for element in text1:
        MyFile.write(str(element))
        MyFile.write('\n')
    MyFile.close()
    print('saveFIle')

def savefile3(): #Сохранение версия 2 --- построчно в файл
    MyFile = open('../совпаденияRapido1.txt', 'a')
    MyFile.write(str(text1))
    MyFile.write('\n')
    MyFile.close()
    print('saveFIle')

def get_lst_from_file(): # Загрузка и обработка комбинаций для дальнейшего анализа
    print('----start----', start_time)
    l = loadfile()
    print('l==', l)
    print('длинна списка = ', len(l))
    i = 0
    while i != len(l): # чистка списка ---- Надо переделать ненравиться
        # for i in range(0,len(l)):

        if 'Суперприз' in l[i]:
            del l[i]
        if 'февраль' in l[i]:
            del l[i]
        if '⚲' in l[i]:
            del l[i]
        i += 1

    print('l==', l)
    for h in range(1, len(l), 3):
        text.append(l[h])

    print('text=', text)

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
    print('lst=', lst)

    for i in range(0, len(lst)):
        del lst[i][-1]

    print(len(lst[0]))

def obrabotka(): # Анализ данных версия 1 --- требуеться доработка
    text1 = []
    num = 0
    lst3 = []
    count = 0
    for x in lst:
        for y in lst:
            if x != y:
                z = (set(x) & set(y))
                print(x, z, len(z))
                if len(z) >= 7:
                    text1.append(['START->', x, '<---->', y, '----->', z, '--->', len(z), '<--END'])
                    count += 1
        text1.append(["SOVPADENIY", count])
        savefile3()
        text1 = []
        count = 0
    print(text1)
