import tkinter as tk

funcao=str()

def inserir_texto(x):
   
    global funcao

    funcao=funcao+x
    texto.delete(1.0,"end")
    texto.insert(1.0,funcao)

janela=tk.Tk()

#janela.geometry("380x400")

texto=tk.Text(janela,height=4, width=27,font=("Arial",24))
texto.grid(columnspan=5)

botao1=tk.Button(janela, text="1",command=lambda:inserir_texto("1"),width=13, height=4,font=("Arial",12))
botao1.grid(column=1,row=2)
botao2=tk.Button(janela, text="2",command=lambda:inserir_texto("2"),width=13, height=4,font=("Arial",12))
botao2.grid(column=2,row=2)
botao3=tk.Button(janela, text="3",command=lambda:inserir_texto("3"),width=13, height=4,font=("Arial",12))
botao3.grid(column=3,row=2)
botao4=tk.Button(janela, text="4",command=lambda:inserir_texto("4"),width=13, height=4,font=("Arial",12))
botao4.grid(column=1,row=3)
botao5=tk.Button(janela, text="5",command=lambda:inserir_texto("5"),width=13, height=4,font=("Arial",12))
botao5.grid(column=2,row=3)
botao6=tk.Button(janela, text="6",command=lambda:inserir_texto("6"),width=13, height=4,font=("Arial",12))
botao6.grid(column=3,row=3)
botao7=tk.Button(janela, text="7",command=lambda:inserir_texto("7"),width=13, height=4,font=("Arial",12))
botao7.grid(column=1,row=4)
botao8=tk.Button(janela, text="8",command=lambda:inserir_texto("8"),width=13, height=4,font=("Arial",12))
botao8.grid(column=2,row=4)
botao9=tk.Button(janela, text="9",command=lambda:inserir_texto("9"),width=13, height=4,font=("Arial",12))
botao9.grid(column=3,row=4)
botao0=tk.Button(janela, text="0",command=lambda:inserir_texto("0"),width=13, height=4,font=("Arial",12))
botao0.grid(column=2,row=5)
botao_abrepar=tk.Button(janela, text="(",command=lambda:inserir_texto("("),width=13, height=4,font=("Arial",12))
botao_abrepar.grid(column=1,row=5)
botao_fechapar=tk.Button(janela, text=")",command=lambda:inserir_texto(")"),width=13, height=4,font=("Arial",12))
botao_fechapar.grid(column=3,row=5)
botao_mais=tk.Button(janela, text="+",command=lambda:inserir_texto("+"),width=13, height=4,font=("Arial",12))
botao_mais.grid(column=4,row=2)
botao_menos=tk.Button(janela, text="-",command=lambda:inserir_texto("-"),width=13, height=4,font=("Arial",12))
botao_menos.grid(column=4,row=3)
botao_mult=tk.Button(janela, text="*",command=lambda:inserir_texto("*"),width=13, height=4,font=("Arial",12))
botao_mult.grid(column=4,row=4)
botao_div=tk.Button(janela, text="/",command=lambda:inserir_texto("/"),width=13, height=4,font=("Arial",12))
botao_div.grid(column=4,row=5)
botao_igual=tk.Button(janela, text="=",command=lambda:inserir_texto("="),width=27, height=4,font=("Arial",12))
botao_igual.grid(column=1,row=6,columnspan=2)
botao_C=tk.Button(janela, text=")",command=lambda:inserir_texto(")"),width=27, height=4,font=("Arial",12))
botao_C.grid(column=3,row=6,columnspan=2)



janela.mainloop()

# aspas diz q a coisa é literal, é o texto, se printar a funçao vai sempre pintar o "x"
#def inserir_texto(x):
#    texto.insert(1.0,x) - quer dizer para o texto aparecer
# % quer dizer "é igual a ..."
#Pesquisar o que significa a função lambda
#O lambda é uma ferramneta que permite a criação de comandos anônimos, muito utilizado para comandos primitivos, que só serão dados uma vez.
#tentando fazer operações com coisas que não combinam (texto com sinais), precisa então transformar caractéries para serem do mesmo tipo
#int=inteiros float=  complex= 
# dado buleano=verdadeiro ou falso
# sequêcia=maneiras de ordenar, vai adicionando letras, palavras, conteúdo, interligando as informações
# exitem 3 maneiras: String(sequencia uma do lado da outra)
# List (cada funcao terá seu lugar)
# calculo = a função
#str = tipo de dado


lista_de_funções=[imprimir(4), somar(5,6), diminuir(5,6)]
