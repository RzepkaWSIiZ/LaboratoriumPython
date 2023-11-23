"""
Zadanie 1

type(1+2)      ---> <class 'int'>
type(1+4.5)    ---> <class 'float'>
type(3/2)      ---> <class 'float'>
type(4/2)      ---> <class 'float'>
type(3//2)     ---> <class 'int'>
type(-3//2)    ---> <class 'int'>
type(11%2)     ---> <class 'int'>
type(2**10)    ---> <class 'int'>
type(8**(1/3)) ---> <class 'float'>


Zadanie 2

int(3.0)    ---> 3
float(3.0)  ---> 3.0
float("3")  ---> 3.0
str(12.4)   ---> '12.4'
bool(0)     ---> False

"""
#Zadanie 3

a = int(input('Proszę podać bok a prostokąta: '))
b = int(input('Proszę podać bok b prostokąta: '))

print(f'Pole prostokąta wynosi: {a*b}')
print(f'Obwód prostokąta wynosi: {2*a + 2*b}')
