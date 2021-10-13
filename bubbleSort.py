import random
def bubble_sort_vacsie(val):
    run = True
    while run:
        run = False
        for i in range(len(val)-1):
            if val[i] > val[i+1]:
                num1 = val[i]
                val[i] = val[i+1]
                val[i+1] = num1
                run = True
    return val
def bubble_sort_mensie(val):
    run = True
    while run:
        run = False
        for i in range(len(val)-1):
            if val[i] < val[i+1]:
                num1 = val[i]
                val[i] = val[i+1]
                val[i+1] = num1
                run = True
    return val

val = []
dlzka = int(input("Kolko chces cisel: "))
#for i in range(dlzka):
    #num = int(input("Zadaj cislo: ") or 0)
    #val.append(num)
for i in range(dlzka):
    num = random.randint(0,100000)
    val.append(num)
a = bubble_sort_mensie(val)
print(a)
b = bubble_sort_vacsie(val)
print()
print(b)