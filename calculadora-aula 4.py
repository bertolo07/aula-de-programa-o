print("digite um número")
a=float(input())         #float = números decimais 
print ("qual operação voce quer fazer"/n)
print ('''segue algumas instruções;
adição use +
subtração use -
para multiplicação use *
para divisão use /
para elevar ao quadrado use - ao quadrado -
para usar a raíz quadrada use 
 ''')
c=input()
b=float(input())           #int = números inteiros

if c=="+":                 
    print(a+b)              #depois de uma condição, como if no final ":"
elif c=="-": 
    print(a-b)
elif c=="*": 
    print(a*b)
elif c=="/": 
    print(a/b)
if c=="ao quadrado":
    print(a**2)
    quit

