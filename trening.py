import random


def select_sportsman():
    sportman = input('Вasdasdaведите имя спортсмена ')
    if sportman == 'bad':
         body_core()
         body_legs()
         body_neck()
         body_arms()
    elif sportman == 'kot':
        print ('Костя выпьет ', random.randint(2 , 15), 'банок пива')
    else:
        print('Таких спортсменов нет')


def body_core():
    #print('упражнения для торс')
    corelist = ['Сгибания', 'Скручивание', 'Жим лежа', 'Развод гантелей']
    print ('Упражнения на вверх тело: ', corelist[random.randint(0, 3)])

def body_legs():
    corelist = ['Сгибания', 'Скручивание', 'Жим лежа', 'Развод гантелей']
    print('упражнения для ног: ', corelist[random.randint(0, 3)])

def body_neck():
    corelist = ['Сгибания', 'Скручивание', 'Жим лежа', 'Развод гантелей']
    print ('упражнение для спины: ', corelist[random.randint(0, 3)])
def body_arms():
    corelist = ['Сгибания', 'Скручивание', 'Жим лежа', 'Развод гантелей']
    print ('упражнеие для рук: ', corelist[random.randint(0, 3)])



select_sportsman()

#print (body_neck(),body_core(),body_arms(),body_legs())





datafile= 'data.data'
f= open(datafile, 'w')
f.write(datafile)
f.close()
f = open (datafile)
