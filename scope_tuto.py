print('Types de base (booléens, entiers, flottants, chaines de charactères)')



a = 10

b = 11



print("main a=", a)

print("main b=", b)

b = a

b = 15

print("main a=", a)

print("main b=", b)



def func1():

    print(a)

    



def func2():

    a = 25

    print("func2 a=",a)



def func3(a):

    print("func3 a=",a)

    a = 20

    print("func3 a=",a)



def func4(l):

    l[0] = 30

    print("func4 l=", l)

    return l



def func5(l):

    l2 = l.copy()

    l2[0] = 50

    return l2



print("func1()")

func1()

print("func2()")

func2()

print("main a=", a)



print("func3(a)")

func3(a)

print("main a=", a)



print("//")

print("main a=", a)

print("main b=", b)



print("func3(b)")

func3(b)

print("main a=", a)

print("main b=", b)



print('\nObjets (ex : listes)')



my_list = [a,b]

my_new_list = my_list

my_new_list[0] = 0

print("main my_list=", my_list)

print("main my_new_list=", my_new_list)

print("main a=", a)

print("main b=", b)



print('func4')

my_list = [a,b]

print(my_list)

my_new_list = func4(my_list)

print("main my_list=", my_list)

print("main my_new_list=", my_new_list)



print("func5")

my_new_list = func5(my_list)

print("main my_list=", my_list)

print("main my_new_list=", my_new_list)