
import random
import time
start_time = time.time()


def savefile():
    MyFile = open('тиражи1.txt', 'w')
    for element in newlst1:
        MyFile.write(str(element))
        MyFile.write('\n')
    MyFile.close()

def savefile2():
    MyFile = open('совпадения.txt', 'w')
    for element in copylst:
        MyFile.write(str(element))
        MyFile.write('\n')
    MyFile.close()

list = [1,2,3,4,5,6,7,8]
list2 = [1,2,3,4]
newlst = []
newlst1 = []
copylst = []
count = 0
for i in range(200000):
    while len(newlst) != 8:
       x = random.randrange(1,20)
       if x not in newlst:
           newlst.append(x)
    if newlst in newlst1:
        copylst = copylst + [newlst] + ['номер тиража'] + [i] + [count]
        count += 1
    newlst1 = newlst1 + [newlst]
    #print(f'Тираж - {i} комбинация {newlst} , всего поторяющихся {count} ')
    newlst = []


for x in copylst:
    print(x)
print (newlst1)

savefile()
savefile2()


print (time.time() - start_time, "seconds")