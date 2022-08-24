from tkinter import *
import tkinter.font as tkfont
from tkinter import messagebox
from tkinter import ttk
import time,random,string
import os
import sys
import mysql.connector

b1OV = ' '
b1XV = ' '
b2OV = ' '
b2XV = ' '
b3OV = ' '
b3XV = ' '
b4OV = ' '
b4XV = ' '
b5OV = ' '
b5XV = ' '
b6OV = ' '
b6XV = ' '
b7OV = ' '
b7XV = ' '
b8OV = ' '
b8XV = ' '
b9OV = ' '
b9XV = ' '

lista_numeros_tictac_X = []
lista_numeros_tictac_O = []

valor_inicial=1

def botao0():
    
    for i0 in range(len(mostrar_calculo.get())):
        continue
    mostrar_calculo.insert(i0, '0')
    if i0==0:
        mostrar_calculo.delete(0)
        mostrar_calculo.insert(i0, '0')
    return 0
def botao1():
    for i in range(len(mostrar_calculo.get())):
        continue
    mostrar_calculo.insert(i, '1')
    if i==0:
        mostrar_calculo.delete(0)
        mostrar_calculo.insert(i, '1')
    return 1
def botao2():
    for i2 in range(len(mostrar_calculo.get())):
        continue
    mostrar_calculo.insert(i2, '2')
    if i2==0:
        mostrar_calculo.delete(0)
        mostrar_calculo.insert(i2, '2')
    return 2
def botao3():
    for i3 in range(len(mostrar_calculo.get())):
        continue
    mostrar_calculo.insert(i3, '3')
    if i3==0:
        mostrar_calculo.delete(0)
        mostrar_calculo.insert(i3, '3')
    return 3
def botao4():
    for i4 in range(len(mostrar_calculo.get())):
        continue
    mostrar_calculo.insert(i4, '4')
    if i4==0:
        mostrar_calculo.delete(0)
        mostrar_calculo.insert(i4, '4')
    return 4
def botao5():
    for i5 in range(len(mostrar_calculo.get())):
        continue
    mostrar_calculo.insert(i5, '5')
    if i5==0:
        mostrar_calculo.delete(0)
        mostrar_calculo.insert(i5, '5')
    return 5
def botao6():
    for i6 in range(len(mostrar_calculo.get())):
        continue
    mostrar_calculo.insert(i6, '6')
    if i6==0:
        mostrar_calculo.delete(0)
        mostrar_calculo.insert(i6, '6')
    return 6
def botao7():
    for i7 in range(len(mostrar_calculo.get())):
        continue
    mostrar_calculo.insert(i7, '7')
    if i7==0:
        mostrar_calculo.delete(0)
        mostrar_calculo.insert(i7, '7')
    return 7
def botao8():
    for i8 in range(len(mostrar_calculo.get())):
        continue
    mostrar_calculo.insert(i8, '8')
    if i8==0:
        mostrar_calculo.delete(0)
        mostrar_calculo.insert(i8, '8')
    return 8
def botao9():
    for i9 in range(len(mostrar_calculo.get())):
        continue
    mostrar_calculo.insert(i9, '9')
    if i9==0:
        mostrar_calculo.delete(0)
        mostrar_calculo.insert(i9, '9')
    return 9

def botaomenos():
    for imenos in range(len(mostrar_calculo.get())):
        continue
    mostrar_calculo.insert(imenos, '-')
def botaomais():
    for imais in range(len(mostrar_calculo.get())):
        continue
    mostrar_calculo.insert(imais, '+')
def botaodivide():
    for idivide in range(len(mostrar_calculo.get())):
        continue
    mostrar_calculo.insert(idivide, '/')
def botaomultiplica():
    for imultiplica in range(len(mostrar_calculo.get())):
        continue
    mostrar_calculo.insert(imultiplica, '*')
def botaoporcento():
    numero_porcentagem = float(mostrar_calculo.get())
    input_porcentagem = (numero_porcentagem/100)

    mostrar_calculo.delete(0,'end')
    mostrar_calculo.insert(0, str(input_porcentagem))
def botaoponto():
    for iponto in range(len(mostrar_calculo.get())):
        continue
    mostrar_calculo.insert(iponto,'.')
def Calculadora():
    calculo_input = eval(mostrar_calculo.get())  
    calculo_input_str = str(calculo_input)

    mostrar_calculo.delete(0,'end')
    mostrar_calculo.insert(0,calculo_input_str)
    mostrar_calculo.insert(len(mostrar_calculo.get()),' ')

def vitoriatictac():
    
    if b1OV=='O' and b2OV=='O' and b3OV=='O':
        messagebox.showinfo(' ','PLAY ER 2 VENCEU')
        ReiniciarTicTac()
    elif b1XV=='X' and b2XV=='X' and b3XV=='X':
        messagebox.showinfo(' ','PLAYER 1 VENCEU')
        ReiniciarTicTac()

    elif b4XV=='X' and b5XV=='X' and b6XV=='X':
        messagebox.showinfo(' ','PLAYER 1 VENCEU')
        ReiniciarTicTac()
    elif b4OV=='O' and b5OV=='O' and b6OV=='O':
        messagebox.showinfo(' ','PLAYER 2 VENCEU')
        ReiniciarTicTac()

    elif b7XV=='X' and b8XV=='X' and b9XV=='X':
        messagebox.showinfo(' ','PLAYER 1 VENCEU')
        ReiniciarTicTac()
    elif b7OV=='O' and b8OV=='O' and b9OV=='O':
        messagebox.showinfo(' ','PLAYER 2 VENCEU')
        ReiniciarTicTac()

    elif b1XV=='X' and b5XV=='X' and b9XV=='X':
        messagebox.showinfo(' ','PLAYER 1 VENCEU')
        ReiniciarTicTac()
    elif b1OV=='O' and b5OV=='O' and b9OV=='O':
        messagebox.showinfo(' ','PLAYER 2 VENCEU')
        ReiniciarTicTac()

    elif b7XV=='X' and b5XV=='X' and b3XV=='X':
        messagebox.showinfo(' ','PLAYER 1 VENCEU')
        ReiniciarTicTac()
    elif b7OV=='O' and b5OV=='O' and b3OV=='O':
        messagebox.showinfo(' ','PLAYER 2 VENCEU')
        ReiniciarTicTac()

    elif b1XV=='X' and b4XV=='X' and b7XV=='X':
        messagebox.showinfo(' ','PLAYER 1 VENCEU')
        ReiniciarTicTac()
    elif b1OV=='O' and b4OV=='O' and b7OV=='O':
        messagebox.showinfo(' ','PLAYER 2 VENCEU')
        ReiniciarTicTac()

    elif b2XV=='X' and b5XV=='X' and b8XV=='X':
        messagebox.showinfo(' ','PLAYER 2 VENCEU')
        ReiniciarTicTac()
    elif b2OV=='O' and b5OV=='O' and b8OV=='O':
        messagebox.showinfo(' ','PLAYER 2 VENCEU')
        ReiniciarTicTac()

    elif b3XV=='X' and b6XV=='X' and b9XV=='X':
        messagebox.showinfo(' ','PLAYER 2 VENCEU')
        ReiniciarTicTac()
    elif b3OV=='O' and b6OV=='O' and b9OV=='O':
        messagebox.showinfo(' ','PLAYER 2 VENCEU')
        ReiniciarTicTac()

def TicTacToe_b1():
    global valor_inicial
    global player1_cor,player2_cor
    global b1XV,b1OV
    if valor_inicial==1:

       botao_circulo_PLAYER_x1.place(x=3000,y=3000)
       label_o1.place(x=3000,y=3000)
       valor_inicial+=1
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b1XV = 'X'
       vitoriatictac()

    else:
        botao_circulo_PLAYER_x1.place(x=3000,y=3000)
        label_x1.place(x=3000,y=3000)
        valor_inicial-=1
        player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='black',background='white')
        player2_tictac.place(x=370,y=50)

        player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='blue',background='white')
        player1_tictac.place(x=1,y=50)
        b1OV = 'O'
        vitoriatictac()
def TicTacToe_b2():
    global valor_inicial
    global player1_cor,player2_cor
    global b2XV,b2OV
    if valor_inicial==1:
       botao_circulo_PLAYER_x2.place(x=3000,y=3000)
       label_o2.place(x=3000,y=3000)
       valor_inicial+=1
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b2XV = 'X'
       vitoriatictac() 
    else:
        botao_circulo_PLAYER_x2.place(x=3000,y=3000)
        label_x2.place(x=3000,y=3000)
        valor_inicial-=1
        player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='black',background='white')
        player2_tictac.place(x=370,y=50)

        player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='blue',background='white')
        player1_tictac.place(x=1,y=50)
        b2OV = 'O'
        vitoriatictac()
def TicTacToe_b3():
    global valor_inicial
    global player1_cor,player2_cor
    global b3XV,b3OV
    if valor_inicial==1:
       botao_circulo_PLAYER_x3.place(x=3000,y=3000)
       label_o3.place(x=3000,y=3000)
       valor_inicial+=1 
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b3XV = 'X'
       vitoriatictac() 
    else:
        botao_circulo_PLAYER_x3.place(x=3000,y=3000)
        label_x3.place(x=3000,y=3000)
        valor_inicial-=1
        player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='black',background='white')
        player2_tictac.place(x=370,y=50)

        player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='blue',background='white')
        player1_tictac.place(x=1,y=50)
        b3OV = 'O'
        vitoriatictac()
def TicTacToe_b4():
    global valor_inicial
    global player1_cor,player2_cor
    global b4XV,b4OV
    if valor_inicial==1:
       botao_circulo_PLAYER_x4.place(x=3000,y=3000)
       label_o4.place(x=3000,y=3000)
       valor_inicial+=1
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b4XV = 'X'
       vitoriatictac()
    else:
        botao_circulo_PLAYER_x4.place(x=3000,y=3000)
        label_x4.place(x=3000,y=3000)
        valor_inicial-=1
        player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='black',background='white')
        player2_tictac.place(x=370,y=50)

        player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='blue',background='white')
        player1_tictac.place(x=1,y=50)
        b4OV = 'O'
        vitoriatictac()
def TicTacToe_b5():
    global valor_inicial
    global player1_cor,player2_cor
    global b5XV,b5OV
    if valor_inicial==1:
       botao_circulo_PLAYER_x5.place(x=3000,y=3000)
       label_o5.place(x=3000,y=3000)
       valor_inicial+=1
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b5XV = 'X'
       vitoriatictac() 
    else:
        botao_circulo_PLAYER_x5.place(x=3000,y=3000)
        label_x5.place(x=3000,y=3000)
        valor_inicial-=1
        player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='black',background='white')
        player2_tictac.place(x=370,y=50)

        player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='blue',background='white')
        player1_tictac.place(x=1,y=50)
        b5OV = 'O'
        vitoriatictac()
def TicTacToe_b6():
    global valor_inicial
    global player1_cor,player2_cor
    global b6XV,b6OV
    if valor_inicial==1:
       botao_circulo_PLAYER_x6.place(x=3000,y=3000)
       label_o6.place(x=3000,y=3000)
       valor_inicial+=1
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b6XV = 'X'
       vitoriatictac() 
    else:
        botao_circulo_PLAYER_x6.place(x=3000,y=3000)
        label_x6.place(x=3000,y=3000)
        valor_inicial-=1
        player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='black',background='white')
        player2_tictac.place(x=370,y=50)

        player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='blue',background='white')
        player1_tictac.place(x=1,y=50)
        b6OV = 'O'
        vitoriatictac()
def TicTacToe_b7():
    global valor_inicial
    global player1_cor,player2_cor
    global b7XV,b7OV
    if valor_inicial==1:
       botao_circulo_PLAYER_x7.place(x=3000,y=3000)
       label_o7.place(x=3000,y=3000)
       valor_inicial+=1 
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b7XV = 'X'
       vitoriatictac() 
    else:
        botao_circulo_PLAYER_x7.place(x=3000,y=3000)
        label_x7.place(x=3000,y=3000)
        valor_inicial-=1
        player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='black',background='white')
        player2_tictac.place(x=370,y=50)

        player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='blue',background='white')
        player1_tictac.place(x=1,y=50)
        b7OV = 'O'
        vitoriatictac()
def TicTacToe_b8():
    global valor_inicial
    global player1_cor,player2_cor
    global b8XV,b8OV
    if valor_inicial==1:
       botao_circulo_PLAYER_x8.place(x=3000,y=3000)
       label_o8.place(x=3000,y=3000)
       valor_inicial+=1
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b8XV = 'X'
       vitoriatictac() 
    else:
        botao_circulo_PLAYER_x8.place(x=3000,y=3000)
        label_x8.place(x=3000,y=3000)
        valor_inicial-=1
        player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='black',background='white')
        player2_tictac.place(x=370,y=50)

        player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='blue',background='white')
        player1_tictac.place(x=1,y=50)
        b8OV = 'O'
        vitoriatictac()
def TicTacToe_b9():
    global valor_inicial
    global player1_cor,player2_cor
    global b9XV,b9OV
    if valor_inicial==1:
       botao_circulo_PLAYER_x9.place(x=3000,y=3000)
       label_o9.place(x=3000,y=3000)
       valor_inicial+=1
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b9XV = 'X'
       vitoriatictac() 
    else:
        botao_circulo_PLAYER_x9.place(x=3000,y=3000)
        label_x9.place(x=3000,y=3000)
        valor_inicial-=1
        player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='black',background='white')
        player2_tictac.place(x=370,y=50)

        player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='blue',background='white')
        player1_tictac.place(x=1,y=50)
        b9OV = 'O'
        vitoriatictac()

def TicTacToe_b1_COM():
    global valor_inicial
    global player1_cor,player2_cor,lista_numeros_tictac_X
    global b1XV,b1OV
    if valor_inicial==1:
       botao_circulo_x1.place(x=3000,y=3000)
       label_o1.place(x=3000,y=3000)
       valor_inicial+=1
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b1XV = 'X'
       lista_numeros_tictac_X.append(1)
       vitoriatictac()
       IAjogada_tictac()
       
def TicTacToe_b2_COM():
    global valor_inicial
    global player1_cor,player2_cor
    global b2XV,b2OV
    if valor_inicial==1:
       botao_circulo_x2.place(x=3000,y=3000)
       label_o2.place(x=3000,y=3000)
       valor_inicial+=1
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b2XV = 'X'
       lista_numeros_tictac_X.append(2)
       vitoriatictac()
       IAjogada_tictac()
       
def TicTacToe_b3_COM():
    global valor_inicial
    global player1_cor,player2_cor
    global b3XV,b3OV
    if valor_inicial==1:
       botao_circulo_x3.place(x=3000,y=3000)
       label_o3.place(x=3000,y=3000)
       valor_inicial+=1 
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b3XV = 'X'
       lista_numeros_tictac_X.append(3) 
       vitoriatictac()
       IAjogada_tictac()
       
def TicTacToe_b4_COM():
    global valor_inicial
    global player1_cor,player2_cor
    global b4XV,b4OV
    if valor_inicial==1:
       botao_circulo_x4.place(x=3000,y=3000)
       label_o4.place(x=3000,y=3000)
       valor_inicial+=1
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b4XV = 'X'
       lista_numeros_tictac_X.append(4)
       vitoriatictac()
       IAjogada_tictac()

def TicTacToe_b5_COM():
    global valor_inicial
    global player1_cor,player2_cor
    global b5XV,b5OV
    if valor_inicial==1:
       botao_circulo_x5.place(x=3000,y=3000)
       label_o5.place(x=3000,y=3000)
       valor_inicial+=1
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b5XV = 'X'
       lista_numeros_tictac_X.append(5)
       vitoriatictac()
       IAjogada_tictac()

def TicTacToe_b6_COM():
    global valor_inicial
    global player1_cor,player2_cor
    global b6XV,b6OV
    if valor_inicial==1:
       botao_circulo_x6.place(x=3000,y=3000)
       label_o6.place(x=3000,y=3000)
       valor_inicial+=1
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b6XV = 'X'
       lista_numeros_tictac_X.append(6)
       vitoriatictac()
       IAjogada_tictac()  

def TicTacToe_b7_COM():
    global valor_inicial
    global player1_cor,player2_cor
    global b7XV,b7OV
    if valor_inicial==1:
       botao_circulo_x7.place(x=3000,y=3000)
       label_o7.place(x=3000,y=3000)
       valor_inicial+=1 
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b7XV = 'X'
       lista_numeros_tictac_X.append(7)
       vitoriatictac()
       IAjogada_tictac()

def TicTacToe_b8_COM():
    global valor_inicial
    global player1_cor,player2_cor
    global b8XV,b8OV
    if valor_inicial==1:
       botao_circulo_x8.place(x=3000,y=3000)
       label_o8.place(x=3000,y=3000)
       valor_inicial+=1
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b8XV = 'X'
       lista_numeros_tictac_X.append(8)
       vitoriatictac()
       IAjogada_tictac()

def TicTacToe_b9_COM():
    global valor_inicial
    global player1_cor,player2_cor
    global b9XV,b9OV
    if valor_inicial==1:
       botao_circulo_x9.place(x=3000,y=3000)
       label_o9.place(x=3000,y=3000)
       valor_inicial+=1
       player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
       player1_tictac.place(x=1,y=50)

       player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='red',background='white')
       player2_tictac.place(x=370,y=50)
       b9XV = 'X'
       lista_numeros_tictac_X.append(9)
       vitoriatictac()
       IAjogada_tictac()

def COM_tictac():

    global jogada_COM_tictac
    global b1OV,b2OV,b3OV,b4OV,b5OV,b6OV,b7OV,b8OV,b9OV,valor_inicial,lista_numeros_tictac_O
    
    for tictac_cont in range(1,30,1):
        com_tictac_numero = random.randrange(1,10,1)

        if com_tictac_numero not in lista_numeros_tictac_O and com_tictac_numero not in lista_numeros_tictac_X:

            jogada_COM_tictac = com_tictac_numero
            lista_numeros_tictac_O.append(com_tictac_numero)
            
            break
    if jogada_COM_tictac==1 and b1XV!='X':
        botao_circulo_x1.place(x=3000,y=3000)
        label_x1.place(x=3000,y=3000)
        valor_inicial-=1
        b1OV = 'O'
        vitoriatictac()
    if jogada_COM_tictac==2 and b2XV!='X':
        botao_circulo_x2.place(x=3000,y=3000)
        label_x2.place(x=3000,y=3000)
        valor_inicial-=1
        b2OV = 'O'
        vitoriatictac()
    if jogada_COM_tictac==3 and b3XV!='X':
        botao_circulo_x3.place(x=3000,y=3000)
        label_x3.place(x=3000,y=3000)
        valor_inicial-=1
        b3OV = 'O'
        vitoriatictac()
    if jogada_COM_tictac==4 and b4XV!='X':
        botao_circulo_x4.place(x=3000,y=3000)
        label_x4.place(x=3000,y=3000)
        valor_inicial-=1
        b4OV = 'O'
        vitoriatictac()
    if jogada_COM_tictac==5 and b5XV!='X':
        botao_circulo_x5.place(x=3000,y=3000)
        label_x5.place(x=3000,y=3000)
        valor_inicial-=1
        b5OV = 'O'
        vitoriatictac()
    if jogada_COM_tictac==6 and b6XV!='X':
        botao_circulo_x6.place(x=3000,y=3000)
        label_x6.place(x=3000,y=3000)
        valor_inicial-=1
        b6OV = 'O'
        vitoriatictac()
    if jogada_COM_tictac==7 and b7XV!='X':
        botao_circulo_x7.place(x=3000,y=3000)
        label_x7.place(x=3000,y=3000)
        valor_inicial-=1
        b7OV = 'O'
        vitoriatictac()
    if jogada_COM_tictac==8 and b8XV!='X':
        botao_circulo_x8.place(x=3000,y=3000)
        label_x8.place(x=3000,y=3000)
        valor_inicial-=1
        b8OV = 'O'
        vitoriatictac()
    if jogada_COM_tictac==9 and b9XV!='X':
        botao_circulo_x9.place(x=3000,y=3000)
        label_x9.place(x=3000,y=3000)
        valor_inicial-=1
        b9OV = 'O'
        vitoriatictac()

def IAjogada_tictac():
    global valor_inicial,lista_numeros_tictac_O
    global b1OV,b2OV,b3OV,b4OV,b5OV,b6OV,b7OV,b8OV,b9OV
    n1_tictac = 1
    n2_tictac = 2
    n3_tictac = 3
    n4_tictac = 4
    n5_tictac = 5
    n6_tictac = 6
    n7_tictac = 7
    n8_tictac = 8
    n9_tictac = 9

    if b1OV=='O' and b2OV=='O' and n3_tictac not in lista_numeros_tictac_O and n3_tictac not in lista_numeros_tictac_X:
        botao_circulo_x3.place(x=3000,y=3000)
        label_x3.place(x=3000,y=3000)
        valor_inicial-=1
        b3OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(3)
    
    elif b2OV=='O' and b3OV=='O' and n1_tictac not in lista_numeros_tictac_O and n1_tictac not in lista_numeros_tictac_X:
        botao_circulo_x1.place(x=3000,y=3000)
        label_x1.place(x=3000,y=3000)
        valor_inicial-=1
        b1OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(1)

    elif b3OV=='O' and b1OV=='O' and n2_tictac not in lista_numeros_tictac_O and n2_tictac not in lista_numeros_tictac_X:
        botao_circulo_x2.place(x=3000,y=3000)
        label_x2.place(x=3000,y=3000)
        valor_inicial-=1
        b2OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(2)


    elif b4OV=='O' and b5OV=='O' and n6_tictac not in lista_numeros_tictac_O and n6_tictac not in lista_numeros_tictac_X:
        botao_circulo_x6.place(x=3000,y=3000)
        label_x6.place(x=3000,y=3000)
        valor_inicial-=1
        b6OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(6)

    elif b6OV=='O' and b5OV=='O' and n4_tictac not in lista_numeros_tictac_O and n4_tictac not in lista_numeros_tictac_X:
        botao_circulo_x4.place(x=3000,y=3000)
        label_x4.place(x=3000,y=3000)
        valor_inicial-=1
        b4OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(4)
    
    elif b6OV=='O' and b4OV=='O' and n5_tictac not in lista_numeros_tictac_O and n5_tictac not in lista_numeros_tictac_X:
        botao_circulo_x5.place(x=3000,y=3000)
        label_x5.place(x=3000,y=3000)
        valor_inicial-=1
        b5OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(5)


    elif b7OV=='O' and b8OV=='O' and n9_tictac not in lista_numeros_tictac_O and n9_tictac not in lista_numeros_tictac_X:
        botao_circulo_x9.place(x=3000,y=3000)
        label_x9.place(x=3000,y=3000)
        valor_inicial-=1
        b9OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(9)
    
    elif b9OV=='O' and b8OV=='O' and n7_tictac not in lista_numeros_tictac_O and n7_tictac not in lista_numeros_tictac_X:
        botao_circulo_x7.place(x=3000,y=3000)
        label_x7.place(x=3000,y=3000)
        valor_inicial-=1
        b7OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(7)

    elif b9OV=='O' and b7OV=='O' and n8_tictac not in lista_numeros_tictac_O and n8_tictac not in lista_numeros_tictac_X:
        botao_circulo_x8.place(x=3000,y=3000)
        label_x8.place(x=3000,y=3000)
        valor_inicial-=1
        b8OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(8)


    elif b1OV=='O' and b5OV=='O' and n9_tictac not in lista_numeros_tictac_O and n9_tictac not in lista_numeros_tictac_X:
        botao_circulo_x9.place(x=3000,y=3000)
        label_x9.place(x=3000,y=3000)
        valor_inicial-=1
        b9OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(9)

    elif b9OV=='O' and b5OV=='O' and n1_tictac not in lista_numeros_tictac_O and n1_tictac not in lista_numeros_tictac_X:
        botao_circulo_x1.place(x=3000,y=3000)
        label_x1.place(x=3000,y=3000)
        valor_inicial-=1
        b1OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(1)

    elif b9OV=='O' and b1OV=='O' and n5_tictac not in lista_numeros_tictac_O and n5_tictac not in lista_numeros_tictac_X:
        botao_circulo_x5.place(x=3000,y=3000)
        label_x5.place(x=3000,y=3000)
        valor_inicial-=1
        b5OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(5)


    elif b7OV=='O' and b5OV=='O' and n3_tictac not in lista_numeros_tictac_O and n3_tictac not in lista_numeros_tictac_X:
        botao_circulo_x3.place(x=3000,y=3000)
        label_x3.place(x=3000,y=3000)
        valor_inicial-=1
        b3OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(3)

    elif b3OV=='O' and b5OV=='O' and n7_tictac not in lista_numeros_tictac_O and n7_tictac not in lista_numeros_tictac_X:
        botao_circulo_x7.place(x=3000,y=3000)
        label_x7.place(x=3000,y=3000)
        valor_inicial-=1
        b7OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(7)

    elif b3OV=='O' and b7OV=='O' and n5_tictac not in lista_numeros_tictac_O and n5_tictac not in lista_numeros_tictac_X:
        botao_circulo_x5.place(x=3000,y=3000)
        label_x5.place(x=3000,y=3000)
        valor_inicial-=1
        b5OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(5)


    elif b1OV=='O' and b4OV=='O' and n7_tictac not in lista_numeros_tictac_O and n7_tictac not in lista_numeros_tictac_X:
        botao_circulo_x7.place(x=3000,y=3000)
        label_x7.place(x=3000,y=3000)
        valor_inicial-=1
        b7OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(7)
    
    elif b7OV=='O' and b4OV=='O' and n1_tictac not in lista_numeros_tictac_O and n1_tictac not in lista_numeros_tictac_X:
        botao_circulo_x1.place(x=3000,y=3000)
        label_x1.place(x=3000,y=3000)
        valor_inicial-=1
        b1OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(1)

    elif b7OV=='O' and b1OV=='O' and n4_tictac not in lista_numeros_tictac_O and n4_tictac not in lista_numeros_tictac_X:
        botao_circulo_x4.place(x=3000,y=3000)
        label_x4.place(x=3000,y=3000)
        valor_inicial-=1
        b4OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(4)


    elif b2OV=='O' and b5OV=='O' and n8_tictac not in lista_numeros_tictac_O and n8_tictac not in lista_numeros_tictac_X:
        botao_circulo_x8.place(x=3000,y=3000)
        label_x8.place(x=3000,y=3000)
        valor_inicial-=1
        b8OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(8)

    elif b8OV=='O' and b5OV=='O' and n2_tictac not in lista_numeros_tictac_O and n2_tictac not in lista_numeros_tictac_X:
        botao_circulo_x2.place(x=3000,y=3000)
        label_x2.place(x=3000,y=3000)
        valor_inicial-=1
        b2OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(2)

    elif b8OV=='O' and b2OV=='O' and n5_tictac not in lista_numeros_tictac_O and n5_tictac not in lista_numeros_tictac_X:
        botao_circulo_x5.place(x=3000,y=3000)
        label_x5.place(x=3000,y=3000)
        valor_inicial-=1
        b5OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(5)


    elif b3OV=='O' and b6OV=='O' and n9_tictac not in lista_numeros_tictac_O and n9_tictac not in lista_numeros_tictac_X:
        botao_circulo_x9.place(x=3000,y=3000)
        label_x9.place(x=3000,y=3000)
        valor_inicial-=1
        b9OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(9)

    elif b9OV=='O' and b6OV=='O' and n3_tictac not in lista_numeros_tictac_O and n3_tictac not in lista_numeros_tictac_X:
        botao_circulo_x3.place(x=3000,y=3000)
        label_x3.place(x=3000,y=3000)
        valor_inicial-=1
        b3OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(3)

    elif b9OV=='O' and b3OV=='O' and n6_tictac not in lista_numeros_tictac_O and n6_tictac not in lista_numeros_tictac_X:
        botao_circulo_x6.place(x=3000,y=3000)
        label_x6.place(x=3000,y=3000)
        valor_inicial-=1
        b6OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(6)

    elif b1XV=='X' and b2XV=='X' and n3_tictac not in lista_numeros_tictac_O:
        botao_circulo_x3.place(x=3000,y=3000)
        label_x3.place(x=3000,y=3000)
        valor_inicial-=1
        b3OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(3)
    
    elif b2XV=='X' and b3XV=='X' and n1_tictac not in lista_numeros_tictac_O:
        botao_circulo_x1.place(x=3000,y=3000)
        label_x1.place(x=3000,y=3000)
        valor_inicial-=1
        b1OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(1)

    elif b3XV=='X' and b1XV=='X' and n2_tictac not in lista_numeros_tictac_O:
        botao_circulo_x2.place(x=3000,y=3000)
        label_x2.place(x=3000,y=3000)
        valor_inicial-=1
        b2OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(2)


    elif b4XV=='X' and b5XV=='X' and n6_tictac not in lista_numeros_tictac_O:
        botao_circulo_x6.place(x=3000,y=3000)
        label_x6.place(x=3000,y=3000)
        valor_inicial-=1
        b6OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(6)

    elif b6XV=='X' and b5XV=='X' and n4_tictac not in lista_numeros_tictac_O:
        botao_circulo_x4.place(x=3000,y=3000)
        label_x4.place(x=3000,y=3000)
        valor_inicial-=1
        b4OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(4)
    
    elif b6XV=='X' and b4XV=='X' and n5_tictac not in lista_numeros_tictac_O:
        botao_circulo_x5.place(x=3000,y=3000)
        label_x5.place(x=3000,y=3000)
        valor_inicial-=1
        b5OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(5)


    elif b7XV=='X' and b8XV=='X' and n9_tictac not in lista_numeros_tictac_O:
        botao_circulo_x9.place(x=3000,y=3000)
        label_x9.place(x=3000,y=3000)
        valor_inicial-=1
        b9OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(9)
    
    elif b9XV=='X' and b8XV=='X' and n7_tictac not in lista_numeros_tictac_O:
        botao_circulo_x7.place(x=3000,y=3000)
        label_x7.place(x=3000,y=3000)
        valor_inicial-=1
        b7OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(7)

    elif b9XV=='X' and b7XV=='X' and n8_tictac not in lista_numeros_tictac_O:
        botao_circulo_x8.place(x=3000,y=3000)
        label_x8.place(x=3000,y=3000)
        valor_inicial-=1
        b8OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(8)


    elif b1XV=='X' and b5XV=='X' and n9_tictac not in lista_numeros_tictac_O:
        botao_circulo_x9.place(x=3000,y=3000)
        label_x9.place(x=3000,y=3000)
        valor_inicial-=1
        b9OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(9)

    elif b9XV=='X' and b5XV=='X' and n1_tictac not in lista_numeros_tictac_O:
        botao_circulo_x1.place(x=3000,y=3000)
        label_x1.place(x=3000,y=3000)
        valor_inicial-=1
        b1OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(1)

    elif b9XV=='X' and b1XV=='X' and n5_tictac not in lista_numeros_tictac_O:
        botao_circulo_x5.place(x=3000,y=3000)
        label_x5.place(x=3000,y=3000)
        valor_inicial-=1
        b5OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(5)


    elif b7XV=='X' and b5XV=='X' and n3_tictac not in lista_numeros_tictac_O:
        botao_circulo_x3.place(x=3000,y=3000)
        label_x3.place(x=3000,y=3000)
        valor_inicial-=1
        b3OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(3)

    elif b3XV=='X' and b5XV=='X' and n7_tictac not in lista_numeros_tictac_O:
        botao_circulo_x7.place(x=3000,y=3000)
        label_x7.place(x=3000,y=3000)
        valor_inicial-=1
        b7OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(7)

    elif b3XV=='X' and b7XV=='X' and n5_tictac not in lista_numeros_tictac_O:
        botao_circulo_x5.place(x=3000,y=3000)
        label_x5.place(x=3000,y=3000)
        valor_inicial-=1
        b5OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(5)


    elif b1XV=='X' and b4XV=='X' and n7_tictac not in lista_numeros_tictac_O:
        botao_circulo_x7.place(x=3000,y=3000)
        label_x7.place(x=3000,y=3000)
        valor_inicial-=1
        b7OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(7)
    
    elif b7XV=='X' and b4XV=='X' and n1_tictac not in lista_numeros_tictac_O:
        botao_circulo_x1.place(x=3000,y=3000)
        label_x1.place(x=3000,y=3000)
        valor_inicial-=1
        b1OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(1)

    elif b7XV=='X' and b1XV=='X' and n4_tictac not in lista_numeros_tictac_O:
        botao_circulo_x4.place(x=3000,y=3000)
        label_x4.place(x=3000,y=3000)
        valor_inicial-=1
        b4OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(4)


    elif b2XV=='X' and b5XV=='X' and n8_tictac not in lista_numeros_tictac_O:
        botao_circulo_x8.place(x=3000,y=3000)
        label_x8.place(x=3000,y=3000)
        valor_inicial-=1
        b8OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(8)

    elif b8XV=='X' and b5XV=='X' and n2_tictac not in lista_numeros_tictac_O:
        botao_circulo_x2.place(x=3000,y=3000)
        label_x2.place(x=3000,y=3000)
        valor_inicial-=1
        b2OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(2)

    elif b8XV=='X' and b2XV=='X' and n5_tictac not in lista_numeros_tictac_O:
        botao_circulo_x5.place(x=3000,y=3000)
        label_x5.place(x=3000,y=3000)
        valor_inicial-=1
        b5OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(5)


    elif b3XV=='X' and b6XV=='X' and n9_tictac not in lista_numeros_tictac_O:
        botao_circulo_x9.place(x=3000,y=3000)
        label_x9.place(x=3000,y=3000)
        valor_inicial-=1
        b9OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(9)

    elif b9XV=='X' and b6XV=='X' and n3_tictac not in lista_numeros_tictac_O:
        botao_circulo_x3.place(x=3000,y=3000)
        label_x3.place(x=3000,y=3000)
        valor_inicial-=1
        b3OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(3)

    elif b9XV=='X' and b3XV=='X' and n6_tictac not in lista_numeros_tictac_O:
        botao_circulo_x6.place(x=3000,y=3000)
        label_x6.place(x=3000,y=3000)
        valor_inicial-=1
        b6OV = 'O'
        vitoriatictac()
        lista_numeros_tictac_O.append(6)

    else:
        COM_tictac()

def IniciarTICTAC():
    global Ticb1,Ticb2,Ticb3,Ticb4,Ticb5,Ticb6,Ticb7,Ticb8,Ticb9
    if caixa_combo_tictac.get()=='PLAYER 2':
        botao_inicial_x1.place(x=3000,y=3000)
        botao_inicial_x2.place(x=3000,y=3000)
        botao_inicial_x3.place(x=3000,y=3000)
        botao_inicial_x4.place(x=3000,y=3000)
        botao_inicial_x5.place(x=3000,y=3000)
        botao_inicial_x6.place(x=3000,y=3000)
        botao_inicial_x7.place(x=3000,y=3000)
        botao_inicial_x8.place(x=3000,y=3000)
        botao_inicial_x9.place(x=3000,y=3000)

        botao_circulo_PLAYER_x1.place(x=113,y=80)
        botao_circulo_PLAYER_x2.place(x=113,y=160)
        botao_circulo_PLAYER_x3.place(x=113,y=240)
        botao_circulo_PLAYER_x4.place(x=200,y=80)
        botao_circulo_PLAYER_x5.place(x=200,y=160)
        botao_circulo_PLAYER_x6.place(x=200,y=240)
        botao_circulo_PLAYER_x7.place(x=287,y=80)
        botao_circulo_PLAYER_x8.place(x=287,y=160)
        botao_circulo_PLAYER_x9.place(x=287,y=240)

    elif caixa_combo_tictac.get()=='COM':
        botao_inicial_x1.place(x=3000,y=3000)
        botao_inicial_x2.place(x=3000,y=3000)
        botao_inicial_x3.place(x=3000,y=3000)
        botao_inicial_x4.place(x=3000,y=3000)
        botao_inicial_x5.place(x=3000,y=3000)
        botao_inicial_x6.place(x=3000,y=3000)
        botao_inicial_x7.place(x=3000,y=3000)
        botao_inicial_x8.place(x=3000,y=3000)
        botao_inicial_x9.place(x=3000,y=3000)
        

        botao_circulo_x1.place(x=113,y=80)
        botao_circulo_x2.place(x=113,y=160)
        botao_circulo_x3.place(x=113,y=240)
        botao_circulo_x4.place(x=200,y=80)
        botao_circulo_x5.place(x=200,y=160)
        botao_circulo_x6.place(x=200,y=240)
        botao_circulo_x7.place(x=287,y=80)
        botao_circulo_x8.place(x=287,y=160)
        botao_circulo_x9.place(x=287,y=240)

def ReiniciarTicTac():
    global b1OV,b1XV,b2OV,b2XV,b3OV,b3XV,b4OV,b4XV,b5OV,b5XV,b6OV,b6XV,b7OV,b7XV,b8OV,b8XV,b9OV,b9XV
    label_x1.place(x=123,y=78)
    label_x2.place(x=123,y=158)
    label_x3.place(x=123,y=241)
    label_x4.place(x=216,y=78)
    label_x5.place(x=216,y=158)
    label_x6.place(x=216,y=241)
    label_x7.place(x=304,y=78)
    label_x8.place(x=304,y=158)
    label_x9.place(x=304,y=241)

    label_o1.place(x=123,y=78)
    label_o2.place(x=123,y=158)
    label_o3.place(x=123,y=241)
    label_o4.place(x=216,y=78)
    label_o5.place(x=216,y=158)
    label_o6.place(x=216,y=241)
    label_o7.place(x=304,y=78)
    label_o8.place(x=304,y=158)
    label_o9.place(x=304,y=241)

    botao_circulo_x1.place(x=3000,y=3000)
    botao_circulo_x2.place(x=3000,y=3000)
    botao_circulo_x3.place(x=3000,y=3000)
    botao_circulo_x4.place(x=3000,y=3000)
    botao_circulo_x5.place(x=3000,y=3000)
    botao_circulo_x6.place(x=3000,y=3000)
    botao_circulo_x7.place(x=3000,y=3000)
    botao_circulo_x8.place(x=3000,y=3000)
    botao_circulo_x9.place(x=3000,y=3000)

    botao_circulo_PLAYER_x1.place(x=3000,y=3000)
    botao_circulo_PLAYER_x2.place(x=3000,y=3000)
    botao_circulo_PLAYER_x3.place(x=3000,y=3000)
    botao_circulo_PLAYER_x4.place(x=3000,y=3000)
    botao_circulo_PLAYER_x5.place(x=3000,y=3000)
    botao_circulo_PLAYER_x6.place(x=3000,y=3000)
    botao_circulo_PLAYER_x7.place(x=3000,y=3000)
    botao_circulo_PLAYER_x8.place(x=3000,y=3000)
    botao_circulo_PLAYER_x9.place(x=3000,y=3000)

    botao_inicial_x1.place(x=113,y=80)
    botao_inicial_x2.place(x=113,y=160)
    botao_inicial_x3.place(x=113,y=240)
    botao_inicial_x4.place(x=200,y=80)
    botao_inicial_x5.place(x=200,y=160)
    botao_inicial_x6.place(x=200,y=240)
    botao_inicial_x7.place(x=287,y=80)
    botao_inicial_x8.place(x=287,y=160)
    botao_inicial_x9.place(x=287,y=240)

    player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
    player1_tictac.place(x=1,y=50)

    player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='black',background='white')
    player2_tictac.place(x=370,y=50)

    b1OV = ' '
    b1XV = ' '
    b2OV = ' '
    b2XV = ' '
    b3OV = ' '
    b3XV = ' '
    b4OV = ' '
    b4XV = ' '
    b5OV = ' '
    b5XV = ' '
    b6OV = ' '
    b6XV = ' '
    b7OV = ' '
    b7XV = ' '
    b8OV = ' '
    b8XV = ' '
    b9OV = ' '
    b9XV = ' '

    lista_numeros_tictac_O.clear()

    lista_numeros_tictac_X.clear()

def apagarTudo():
    mostrar_calculo.delete(0,'end')
    mostrar_calculo.insert(0,' ')

def apagarUltimo():
    for apagaultimo in range(len(mostrar_calculo.get())):
        continue
    apagaultimo -=1
    mostrar_calculo.delete(apagaultimo)
    
    if len(mostrar_calculo.get())==0:
        mostrar_calculo.insert(0,' ')

def LogaUsuario():
    con = mysql.connector.connect(host='localhost',database='login',user='root',password='acesso123')
    try:
        if con.is_connected():
                
            cursor = con.cursor()
            comando_sql = "SELECT user_name,user_senha FROM usuario WHERE user_name=%s AND user_senha=%s;"
            dados = (str(input_user.get()),str(input_senha.get()))
            cursor.execute(comando_sql,dados)
            sql_login = cursor.fetchall()
            print(sql_login)
            if sql_login[0][0]==input_user.get() and sql_login[0][1]==input_senha.get():
                messagebox.showinfo('','LOGADO COM SUCESSO!')
                if con.is_connected():
                    cursor.close()
                    con.close()
                janela_principal()
            elif sql_login[0][0]!=input_user.get() or sql_login[0][1]!=input_senha.get():
                messagebox.showerror('','USUÁRIO OU SENHA INVÁLIDOS')
            
    except IndexError:
        messagebox.showerror('','USUÁRIO OU SENHA INVÁLIDOS')
        
    except:
        messagebox.showerror('','USUÁRIO OU SENHA INVÁLIDOS')
        
def CadastraUsuario():
    con = mysql.connector.connect(host='localhost',database='login',user='root',password='acesso123')
    try:
        if con.is_connected():
            if input_user.get()=='' or input_senha.get()=='':
                messagebox.showerror('','CADASTRO INVÁLIDO')
            else:
                cursor = con.cursor()
                comando_sql = "INSERT INTO usuario(user_name,user_senha) VALUES(%s,%s);"
                dados = (str(input_user.get()),str(input_senha.get()))
                cursor.execute(comando_sql,dados)
                con.commit()
                messagebox.showinfo(' ','CADASTRADO COM SUCESSO!!')
                
                if con.is_connected():
                    cursor.close()
                    con.close()
        
    except mysql.connector.errors.IntegrityError:
        messagebox.showerror('','USUÁRIO JÁ CADASTRADO')
    
    except:
        messagebox.showerror('','CADASTRO INVÁLIDO')
    
def janela_principal():
    global imagem
    global janela_depoislogin
    global botao_voltar,janela,label_adivinhacao,botao_adivinhacao,label_tictac,botao_tictac,label_calculadora,botao_calculadora,imagem,label_imagem,botao_sair

    janela.withdraw()
    janela_depoislogin = Toplevel()
    janela_depoislogin.title(' ')
    janela_depoislogin.geometry('410x485+730+250')
    janela_depoislogin.configure(background='white')
    janela_depoislogin.resizable(width=FALSE,height=FALSE)
    janela_depoislogin.iconbitmap('./imgs/cubo.ico')

    estilo_da_fonte_titulo = tkfont.Font(family='Bahnschrift', size=23)

    estilo_da_fonte_widgets = tkfont.Font(family='Bahnschrift', size=11)

    setilo_da_fonte_label_principal = tkfont.Font(family='Bahnschrift',size=15)

    label_nome_user = Label(janela_depoislogin, text=input_user.get(), font=estilo_da_fonte_titulo,background='white',anchor=NE)
    label_nome_user.place(x=150,y=50)

    label_espaco_principal = Label(janela_depoislogin, text= '',width=375, anchor=NW, background='black',font=('Ivy 1'), fg='black')
    label_espaco_principal.place(x=15,y=160)


    label_gera_senha = Label(janela_depoislogin, text='GERADOR DE SENHAS', font=setilo_da_fonte_label_principal,background='white')
    label_gera_senha.place(x=9,y=190)

    botao_gera_senha = Button(janela_depoislogin, text='⇨',relief='flat',command=janela_gerador_senha,bg='black',fg='white',width=15,font=estilo_da_fonte_widgets)
    botao_gera_senha.place(x=260,y=190)


    label_jokenpo = Label(janela_depoislogin, text='JO KEN PO', font=setilo_da_fonte_label_principal,background='white')
    label_jokenpo.place(x=9,y=240)

    botao_jokenpo = Button(janela_depoislogin, text='⇨',relief='flat',command=janela_jokenpo,bg='black',fg='white',width=15,font=estilo_da_fonte_widgets)
    botao_jokenpo.place(x=260,y=240)


    label_adivinhacao = Label(janela_depoislogin, text='JOGO DA ADIVINHAÇÃO',font=setilo_da_fonte_label_principal,background='white')
    label_adivinhacao.place(x=9,y=290)

    botao_adivinhacao = Button(janela_depoislogin, text='⇨',relief='flat',command=janela_adivinhacao,bg='black',fg='white',width=15,font=estilo_da_fonte_widgets)
    botao_adivinhacao.place(x=260,y=290)


    label_tictac = Label(janela_depoislogin, text='TIC TAC TOE', font=setilo_da_fonte_label_principal,background='white')
    label_tictac.place(x=9,y=340)

    botao_tictac = Button(janela_depoislogin, text='⇨',relief='flat',command=janela_jogodavelha,bg='black',fg='white',width=15,font=estilo_da_fonte_widgets)
    botao_tictac.place(x=260,y=340)

    label_calculadora = Label(janela_depoislogin, text='CALCULADORA', font=setilo_da_fonte_label_principal,background='white')
    label_calculadora.place(x=9,y=390)

    botao_calculadora = Button(janela_depoislogin, text='⇨',relief='flat',command=janela_Calculadora,bg='black',fg='white',width=15,font=estilo_da_fonte_widgets)
    botao_calculadora.place(x=260,y=390)

    imagem = PhotoImage(file="./imgs/user_login_certo.png")
    label_imagem = Label(janela_depoislogin, image=imagem,background='white')
    label_imagem.place(x=9,y=1)

    botao_sair = Button(janela_depoislogin, text='Sair',command=volta_janela_login_principal,relief='solid',bg='black',fg='white',width=11,font=estilo_da_fonte_widgets)
    botao_sair.place(x=150,y=440)

def volta_janela_login_principal():
    janela_depoislogin.withdraw()
    janela.deiconify()

def volta_janela_principal_jokenpo():
    janela_do_jokenpo.withdraw()
    janela_depoislogin.deiconify()

def volta_janela_principal_adivinhacao():
    janela_da_adivinhacao.withdraw()
    janela_depoislogin.deiconify()

def volta_janela_principal_gerador():
    janela_gera_senha.withdraw()
    janela_depoislogin.deiconify()

def volta_janela_principal_calculadora():
    janela_da_calculadora.withdraw()
    janela_depoislogin.deiconify()

def volta_janela_principal_tictactoe():
    janela_TICTACTOE.withdraw()
    janela_depoislogin.deiconify()

def janela_jokenpo():
    global janela_do_jokenpo
    global label_nome_user_jokenpo,label_espaco_principal_jokenpo,escolher_jokenpo,caixa_combo,label_COM_texto,imagem_tesoura_direita,imagem_papel_direita,imagem_pedra_direita,imagem_versus,imagem_pedra,imagem_papel,imagem_tesoura,label_player_texto,label_vs,botao_jogar,botao_retornar,imagem_dnv,botao_jogar_dnv


    janela_depoislogin.withdraw()
    janela_do_jokenpo = Toplevel()
    janela_do_jokenpo.title(' ')
    janela_do_jokenpo.geometry('630x310+700+390')
    janela_do_jokenpo.configure(background='white')
    janela_do_jokenpo.resizable(width=FALSE,height=FALSE)
    janela_do_jokenpo.iconbitmap('./imgs/cubo.ico')
    estilo_da_fonte_titulo = tkfont.Font(family='Bahnschrift', size=23)

    estilo_da_fonte_widgets = tkfont.Font(family='Bahnschrift', size=11)

    setilo_da_fonte_label_principal = tkfont.Font(family='Bahnschrift',size=15)

    label_nome_user_jokenpo = Label(janela_do_jokenpo, text='JO KEN PO!!', font=estilo_da_fonte_titulo,background='white',anchor=NE)
    label_nome_user_jokenpo.place(x=242,y=1)

    label_espaco_principal_jokenpo = Label(janela_do_jokenpo, text= '',width=210, anchor=NW, background='black',font=('Ivy 1'), fg='black')
    label_espaco_principal_jokenpo.place(x=218,y=40)

    escolher_jokenpo = StringVar()
    caixa_combo = ttk.Combobox(janela_do_jokenpo,textvariable=escolher_jokenpo,)
    caixa_combo['values']= ['Pedra','Papel','Tesoura']
    caixa_combo.place(x=250,y=240)



    label_COM_texto = Label(janela_do_jokenpo,text='COM',font=setilo_da_fonte_label_principal,background='white')
    label_COM_texto.place(x=560,y=58)

    imagem_pedra = PhotoImage(file='./imgs/PEDRA.png')
    imagem_papel = PhotoImage(file='./imgs/PAPEL.png')
    imagem_tesoura= PhotoImage(file='./imgs/TESOURA.png')
    imagem_versus = PhotoImage(file='./imgs/versus preto e branco certo.png')

    imagem_pedra_direita = PhotoImage(file='./imgs/PEDRA_direita.png')
    imagem_papel_direita = PhotoImage(file='./imgs/PAPEL_direita.png')
    imagem_tesoura_direita = PhotoImage(file='./imgs/TESOURA_papel.png')


    label_player_texto = Label(janela_do_jokenpo, text='PLAYER', font=setilo_da_fonte_label_principal,background='white')
    label_player_texto.place(x=9,y=58)

    label_vs = Label(janela_do_jokenpo,image=imagem_versus,background='white')
    label_vs.place(x=284,y=130)


    imagem_dnv = PhotoImage(file='./imgs/pngegg.png')
    botao_jogar = Button(janela_do_jokenpo,command=jogo_jokenpo, text='JOGAR',relief='sunken',bg='black',fg='white',width=12,font=estilo_da_fonte_widgets)
    botao_jogar.place(x=288,y=270)

    botao_jogar_dnv = Button(janela_do_jokenpo,command=esconder, image=imagem_dnv,compound=CENTER,width=25,height=26,relief='solid',background='black',foreground='black')
    botao_jogar_dnv.place(x=250,y=270)


    botao_retornar = Button(janela_do_jokenpo, text='<<',relief='sunken',command=volta_janela_principal_jokenpo,width=6,height=1,background='black',font=estilo_da_fonte_widgets,foreground='white')
    botao_retornar.place(x=2,y=2)

def janela_adivinhacao():
    global janela_da_adivinhacao
    global label_nome_user_adivinhacao,label_espaco_principal_adivinhacao,escolher_adivinhacao,caixa_combo_adivinhacao,label_COM_texto_adivinhacao,imagem_versus_adivinhacao,label_player_texto_adivinhacao,label_vs_adivinhacao,botao_jogar_adivinhacao,botao_retornar_adivinhacao

    janela_depoislogin.withdraw()
    janela_da_adivinhacao = Toplevel()
    janela_da_adivinhacao.title(' ')
    janela_da_adivinhacao.geometry('630x310+700+390')
    janela_da_adivinhacao.configure(background='white')
    janela_da_adivinhacao.resizable(width=FALSE,height=FALSE)
    janela_da_adivinhacao.iconbitmap('./imgs/cubo.ico')
    estilo_da_fonte_titulo = tkfont.Font(family='Bahnschrift', size=23)

    estilo_da_fonte_widgets = tkfont.Font(family='Bahnschrift', size=11)

    setilo_da_fonte_label_principal = tkfont.Font(family='Bahnschrift',size=15)


    label_nome_user_adivinhacao = Label(janela_da_adivinhacao, text='ADIVINHAÇÃO', font=estilo_da_fonte_titulo,background='white',anchor=NE)
    label_nome_user_adivinhacao.place(x=220,y=1)

    label_espaco_principal_adivinhacao = Label(janela_da_adivinhacao, text= '',width=210, anchor=NW, background='black',font=('Ivy 1'), fg='black')
    label_espaco_principal_adivinhacao.place(x=213,y=42)

    escolher_adivinhacao = StringVar()
    caixa_combo_adivinhacao = ttk.Combobox(janela_da_adivinhacao,textvariable=escolher_adivinhacao)
    caixa_combo_adivinhacao['values']= [0,1,2,3,4,5]
    caixa_combo_adivinhacao.place(x=240,y=240)



    label_COM_texto_adivinhacao = Label(janela_da_adivinhacao,text='COM',font=setilo_da_fonte_label_principal,background='white')
    label_COM_texto_adivinhacao.place(x=560,y=58)


    imagem_versus_adivinhacao = PhotoImage(file='./imgs/versus preto e branco certo.png')


    label_player_texto_adivinhacao = Label(janela_da_adivinhacao, text='PLAYER', font=setilo_da_fonte_label_principal,background='white')
    label_player_texto_adivinhacao.place(x=9,y=58)


    label_vs_adivinhacao = Label(janela_da_adivinhacao,image=imagem_versus_adivinhacao,background='white')
    label_vs_adivinhacao.place(x=274,y=130)
    

    botao_jogar_adivinhacao = Button(janela_da_adivinhacao,command=jogo_adivinhacao, text='JOGAR',relief='sunken',bg='black',fg='white',width=15,font=estilo_da_fonte_widgets)
    botao_jogar_adivinhacao.place(x=247,y=270)


    botao_retornar_adivinhacao = Button(janela_da_adivinhacao, text='<<',command=volta_janela_principal_adivinhacao,relief='sunken',width=6,height=1,background='black',font=estilo_da_fonte_widgets,foreground='white')
    botao_retornar_adivinhacao.place(x=2,y=2)

def janela_gerador_senha():
    global janela_gera_senha
    global caixa_combo_gerador,label_nome_user_gerador,label_espaco_principal_gerador,colocar_a_senha_gerada,botao_gerar_senha,botao_sair_gerador

    janela_depoislogin.withdraw()
    janela_gera_senha = Toplevel()
    janela_gera_senha.title(' ')
    janela_gera_senha.geometry('470x200+700+390')
    janela_gera_senha.configure(background='white')
    janela_gera_senha.resizable(width=FALSE,height=FALSE)
    janela_gera_senha.iconbitmap('./imgs/cubo.ico')
    estilo_da_fonte_titulo = tkfont.Font(family='Bahnschrift', size=23)

    estilo_da_fonte_widgets = tkfont.Font(family='Bahnschrift', size=11)

    setilo_da_fonte_label_principal = tkfont.Font(family='Bahnschrift',size=15)


    label_nome_user_gerador = Label(janela_gera_senha, text='GERADOR', font=estilo_da_fonte_titulo,background='white',anchor=NE)
    label_nome_user_gerador.place(x=162,y=1)

    label_espaco_principal_gerador = Label(janela_gera_senha, text= '',width=210, anchor=NW, background='black',font=('Ivy 1'), fg='black')
    label_espaco_principal_gerador.place(x=125,y=42)

    escolher_gerador = StringVar()
    caixa_combo_gerador = ttk.Combobox(janela_gera_senha,textvariable=escolher_gerador)
    caixa_combo_gerador['values']= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    caixa_combo_gerador.place(x=211,y=63)



    label_player_texto_adivinhacao = Label(janela_gera_senha, text='TAMANHO: ', font=setilo_da_fonte_label_principal,background='white')
    label_player_texto_adivinhacao.place(x=100,y=58)

    colocar_a_senha_gerada = Entry(janela_gera_senha, width=25, justify='left',font=('',14), highlightthickness=3, relief='solid')
    colocar_a_senha_gerada.place(x=90,y=100)


    botao_gerar_senha = Button(janela_gera_senha, text='GERAR',relief='sunken',command=GeraSenha,bg='black',fg='white',width=17,font=estilo_da_fonte_widgets)
    botao_gerar_senha.place(x=227,y=150)

    botao_sair_gerador = Button(janela_gera_senha, text='SAIR',relief='sunken',bg='black',fg='white',width=13,font=estilo_da_fonte_widgets,command=volta_janela_principal_gerador)
    botao_sair_gerador.place(x=90,y=150)

def janela_jogodavelha():
    global janela_TICTACTOE
    global player1_tictac,player2_tictac,label_x1,label_x2,label_x3,label_x4,label_x5,label_x6,label_x7,label_x8,label_x9,label_o1,label_o2,label_o3,label_o4,label_o5,label_o6,label_o7,label_o8,label_o9,botao_circulo_x1,botao_circulo_x2,botao_circulo_x3,botao_circulo_x4,botao_circulo_x5,botao_circulo_x6,botao_circulo_x7,botao_circulo_x8,botao_circulo_x9,botao_voltar_tictac,botao_dnv_tictac,imagem_dnv_tictac
    global botao_circulo_PLAYER_x1,botao_circulo_PLAYER_x2,botao_circulo_PLAYER_x3,botao_circulo_PLAYER_x4,botao_circulo_PLAYER_x5,botao_circulo_PLAYER_x6,botao_circulo_PLAYER_x7,botao_circulo_PLAYER_x8,botao_circulo_PLAYER_x9
    global botao_inicial_x1,botao_inicial_x2,botao_inicial_x3,botao_inicial_x4,botao_inicial_x5,botao_inicial_x6,botao_inicial_x7,botao_inicial_x8,botao_inicial_x9,caixa_combo_tictac

    
    

    janela_depoislogin.withdraw()
    janela_TICTACTOE = Toplevel()
    janela_TICTACTOE.title(' ')
    janela_TICTACTOE.geometry('472x430+700+390')
    janela_TICTACTOE.configure(background='white')
    janela_TICTACTOE.resizable(width=FALSE,height=FALSE)
    janela_TICTACTOE.iconbitmap('./imgs/cubo.ico')

    estilo_da_fonte_titulo = tkfont.Font(family='Bahnschrift', size=23)
    estilo_da_fonte_logado = tkfont.Font(family='Bahnschrift',size=16)
    estilo_da_fonte_widgets = tkfont.Font(family='Bahnschrift', size=11)

    # TELA PRINCIPAL
    label_TICTACTOE = Label(janela_TICTACTOE, text='TIC TAC TOE', font=estilo_da_fonte_titulo,background='white',anchor=NE)
    label_TICTACTOE.place(x=155,y=5)

    label_espaco_vertical = Label(janela_TICTACTOE, text= '',width=1,height=122, anchor=NW, background='black',font=('Ivy 1'), fg='black')
    label_espaco_vertical.place(x=190,y=70)

    label_espaco_vertical2 = Label(janela_TICTACTOE, text= '',width=1,height=122, anchor=NW, background='black',font=('Ivy 1'), fg='black')
    label_espaco_vertical2.place(x=277,y=70)

    label_espaco_horizontal = Label(janela_TICTACTOE, text= '',width=270,height=1, anchor=NW, background='black',font=('Ivy 1'), fg='black')
    label_espaco_horizontal.place(x=100,y=150)

    label_espaco_horizontal2 = Label(janela_TICTACTOE, text= '',width=270,height=1, anchor=NW, background='black',font=('Ivy 1'), fg='black')
    label_espaco_horizontal2.place(x=100,y=230)


    player1_tictac = Label(janela_TICTACTOE, text='PLAYER 1', font=estilo_da_fonte_logado,foreground='black',background='white')
    player1_tictac.place(x=1,y=50)

    player2_tictac = Label(janela_TICTACTOE, text='PLAYER 2', font=estilo_da_fonte_logado,foreground='black',background='white')
    player2_tictac.place(x=370,y=50)

    label_x1 = Label(janela_TICTACTOE,text='X',font=('Helvetica','43','bold'),background='white',foreground='blue',)
    label_x1.place(x=123,y=78)

    label_x2 = Label(janela_TICTACTOE,text='X',font=('Helvetica','43','bold'),background='white',foreground='blue',)
    label_x2.place(x=123,y=158)

    label_x3 = Label(janela_TICTACTOE,text='X',font=('Helvetica','43','bold'),background='white',foreground='blue',)
    label_x3.place(x=123,y=241)




    label_x4 = Label(janela_TICTACTOE,text='X',font=('Helvetica','43','bold'),background='white',foreground='blue',)
    label_x4.place(x=216,y=78)

    label_x5 = Label(janela_TICTACTOE,text='X',font=('Helvetica','43','bold'),background='white',foreground='blue',)
    label_x5.place(x=216,y=158)

    label_x6 = Label(janela_TICTACTOE,text='X',font=('Helvetica','43','bold'),background='white',foreground='blue',)
    label_x6.place(x=216,y=241)


    label_x7 = Label(janela_TICTACTOE,text='X',font=('Helvetica','43','bold'),background='white',foreground='blue',)
    label_x7.place(x=304,y=78)

    label_x8 = Label(janela_TICTACTOE,text='X',font=('Helvetica','43','bold'),background='white',foreground='blue',)
    label_x8.place(x=304,y=158)

    label_x9 = Label(janela_TICTACTOE,text='X',font=('Helvetica','43','bold'),background='white',foreground='blue',)
    label_x9.place(x=304,y=241)


    label_o1 = Label(janela_TICTACTOE,text='O',font=('Helvetica','43','bold'),background='white',foreground='red',)
    label_o1.place(x=123,y=78)

    label_o2 = Label(janela_TICTACTOE,text='O',font=('Helvetica','43','bold'),background='white',foreground='red',)
    label_o2.place(x=123,y=158)

    label_o3 = Label(janela_TICTACTOE,text='O',font=('Helvetica','43','bold'),background='white',foreground='red',)
    label_o3.place(x=123,y=241)


    label_o4 = Label(janela_TICTACTOE,text='O',font=('Helvetica','43','bold'),background='white',foreground='red',)
    label_o4.place(x=216,y=78)

    label_o5 = Label(janela_TICTACTOE,text='O',font=('Helvetica','43','bold'),background='white',foreground='red',)
    label_o5.place(x=216,y=158)

    label_o6 = Label(janela_TICTACTOE,text='O',font=('Helvetica','43','bold'),background='white',foreground='red',)
    label_o6.place(x=216,y=241)


    label_o7 = Label(janela_TICTACTOE,text='O',font=('Helvetica','43','bold'),background='white',foreground='red',)
    label_o7.place(x=304,y=78)

    label_o8 = Label(janela_TICTACTOE,text='O',font=('Helvetica','43','bold'),background='white',foreground='red',)
    label_o8.place(x=304,y=158)

    label_o9 = Label(janela_TICTACTOE,text='O',font=('Helvetica','43','bold'),background='white',foreground='red',)
    label_o9.place(x=304,y=241)


    botao_circulo_x1 = Button(janela_TICTACTOE,command=TicTacToe_b1_COM, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_x1.place(x=3000,y=3000)

    botao_circulo_x2 = Button(janela_TICTACTOE,command=TicTacToe_b2_COM, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_x2.place(x=3000,y=3000)

    botao_circulo_x3 = Button(janela_TICTACTOE,command=TicTacToe_b3_COM, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_x3.place(x=3000,y=3000)




    botao_circulo_x4 = Button(janela_TICTACTOE,command=TicTacToe_b4_COM, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_x4.place(x=3000,y=3000)

    botao_circulo_x5 = Button(janela_TICTACTOE,command=TicTacToe_b5_COM, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_x5.place(x=3000,y=3000)

    botao_circulo_x6 = Button(janela_TICTACTOE,command=TicTacToe_b6_COM, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_x6.place(x=3000,y=3000)


    botao_circulo_x7 = Button(janela_TICTACTOE,command=TicTacToe_b7_COM, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_x7.place(x=3000,y=3000)

    botao_circulo_x8 = Button(janela_TICTACTOE,command=TicTacToe_b8_COM, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_x8.place(x=3000,y=3000)

    botao_circulo_x9 = Button(janela_TICTACTOE,command=TicTacToe_b9_COM, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_x9.place(x=3000,y=3000)



    botao_circulo_PLAYER_x1 = Button(janela_TICTACTOE,command=TicTacToe_b1, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_PLAYER_x1.place(x=3000,y=3000)

    botao_circulo_PLAYER_x2 = Button(janela_TICTACTOE,command=TicTacToe_b2, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_PLAYER_x2.place(x=3000,y=3000)

    botao_circulo_PLAYER_x3 = Button(janela_TICTACTOE,command=TicTacToe_b3, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_PLAYER_x3.place(x=3000,y=3000)




    botao_circulo_PLAYER_x4 = Button(janela_TICTACTOE,command=TicTacToe_b4, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_PLAYER_x4.place(x=3000,y=3000)

    botao_circulo_PLAYER_x5 = Button(janela_TICTACTOE,command=TicTacToe_b5, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_PLAYER_x5.place(x=3000,y=3000)

    botao_circulo_PLAYER_x6 = Button(janela_TICTACTOE,command=TicTacToe_b6, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_PLAYER_x6.place(x=3000,y=3000)


    botao_circulo_PLAYER_x7 = Button(janela_TICTACTOE,command=TicTacToe_b7, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_PLAYER_x7.place(x=3000,y=3000)

    botao_circulo_PLAYER_x8 = Button(janela_TICTACTOE,command=TicTacToe_b8, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_PLAYER_x8.place(x=3000,y=3000)

    botao_circulo_PLAYER_x9 = Button(janela_TICTACTOE,command=TicTacToe_b9, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_circulo_PLAYER_x9.place(x=3000,y=3000)


    botao_inicial_x1 = Button(janela_TICTACTOE, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_inicial_x1.place(x=113,y=80)

    botao_inicial_x2 = Button(janela_TICTACTOE, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_inicial_x2.place(x=113,y=160)

    botao_inicial_x3 = Button(janela_TICTACTOE, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_inicial_x3.place(x=113,y=240)




    botao_inicial_x4 = Button(janela_TICTACTOE, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_inicial_x4.place(x=200,y=80)

    botao_inicial_x5 = Button(janela_TICTACTOE, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_inicial_x5.place(x=200,y=160)

    botao_inicial_x6 = Button(janela_TICTACTOE, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_inicial_x6.place(x=200,y=240)


    botao_inicial_x7 = Button(janela_TICTACTOE, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_inicial_x7.place(x=287,y=80)

    botao_inicial_x8 = Button(janela_TICTACTOE, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_inicial_x8.place(x=287,y=160)

    botao_inicial_x9 = Button(janela_TICTACTOE, text=' ',relief='flat',bg='white',fg='white',width=8,height=3,font=estilo_da_fonte_widgets)
    botao_inicial_x9.place(x=287,y=240)


    botao_voltar_tictac = Button(janela_TICTACTOE, text='SAIR',command=volta_janela_principal_tictactoe,relief='flat',bg='black',fg='white',width=8,font=estilo_da_fonte_widgets)
    botao_voltar_tictac.place(x=115,y=380)

    botao_jogar_tictac = Button(janela_TICTACTOE, text='JOGAR',command=IniciarTICTAC,relief='flat',bg='black',fg='white',width=15,font=estilo_da_fonte_widgets)
    botao_jogar_tictac.place(x=200,y=380)

    imagem_dnv_tictac = PhotoImage(file='./imgs/pngegg.png')
    botao_dnv_tictac = Button(janela_TICTACTOE,command=ReiniciarTicTac, image=imagem_dnv_tictac,compound=CENTER,width=25,height=26,relief='solid',background='black',foreground='black')
    botao_dnv_tictac.place(x=335,y=380)

    vs_com_pl = Label(janela_TICTACTOE, text='VS:', font=estilo_da_fonte_logado,foreground='black',background='white')
    vs_com_pl .place(x=155,y=340)

    escolher_VS_tictac = StringVar()
    caixa_combo_tictac = ttk.Combobox(janela_TICTACTOE,textvariable=escolher_VS_tictac,width=18)
    caixa_combo_tictac['values']= ['COM','PLAYER 2']
    caixa_combo_tictac.place(x=200,y=345)

def janela_Calculadora():
    global janela_da_calculadora
    global mostrar_calculo
    janela_depoislogin.withdraw()
    janela_da_calculadora = Toplevel()
    janela_da_calculadora.title(' ')
    janela_da_calculadora.geometry('400x383+700+390')
    janela_da_calculadora.configure(background='#1C1C1C')
    janela_da_calculadora.resizable(width=FALSE,height=FALSE)
    janela_da_calculadora.iconbitmap('./imgs/cubo.ico')
    estilo_da_fonte_titulo = tkfont.Font(family='Bahnschrift', size=23)

    estilo_da_fonte_widgets = tkfont.Font(family='Bahnschrift', size=11)

    setilo_da_fonte_label_principal = tkfont.Font(family='Bahnschrift',size=15)

    mostrar_calculo = Entry(janela_da_calculadora,width=25,font=('Digital-7',24), relief='sunken',background='black',foreground='red')
    mostrar_calculo.place(x=10,y=27)

    label_calculadora_numero = Label(janela_da_calculadora,text='Calculadora InFRAME',font=('Digital-7','11'),background='#1C1C1C',foreground='white')
    label_calculadora_numero.place(x=260,y=3)


    botao_c = Button(janela_da_calculadora,command=apagarTudo ,text='C',bg='#EEE8AA',fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_c.place(x=10,y=70)

    botao_7 = Button(janela_da_calculadora,command=botao7, text='7',bg='#f1f2f3',fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_7.place(x=10,y=132)

    botao_4 = Button(janela_da_calculadora,command=botao4,text='4',bg='#f1f2f3',fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_4.place(x=10,y=194)

    botao_1 = Button(janela_da_calculadora, text='1',bg='#f1f2f3',fg='black',width=8,height=2,relief='flat',command=botao1,font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_1.place(x=10,y=256)

    botao_0 = Button(janela_da_calculadora,command=botao0, text='0',bg='#f1f2f3',fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_0.place(x=10,y=318)

    mostrar_calculo.insert(0, ' ')

    botao_ce = Button(janela_da_calculadora,command=apagarUltimo ,text='CE',bg='#EEE8AA',fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_ce.place(x=105,y=70)

    botao_8 = Button(janela_da_calculadora,command=botao8, text='8',bg='#f1f2f3',fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_8.place(x=105,y=132)

    botao_5 = Button(janela_da_calculadora,command=botao5, text='5',bg='#f1f2f3',fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_5.place(x=105,y=194)

    botao_2 = Button(janela_da_calculadora,command=botao2, text='2',bg='#f1f2f3',fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_2.place(x=105,y=256)

    botao_ponto = Button(janela_da_calculadora, text='.',bg='#f1f2f3',command=botaoponto,fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_ponto.place(x=105,y=318)


    botao_porcento = Button(janela_da_calculadora, text='%',bg='#EEE8AA',command=botaoporcento,fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_porcento.place(x=200,y=70)

    botao_9 = Button(janela_da_calculadora,command=botao9, text='9',bg='#f1f2f3',fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_9.place(x=200,y=132)

    botao_6 = Button(janela_da_calculadora,command=botao6, text='6',bg='#f1f2f3',fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_6.place(x=200,y=194)

    botao_3 = Button(janela_da_calculadora,command=botao3, text='3',bg='#f1f2f3',fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_3.place(x=200,y=256)

    botao_igual = Button(janela_da_calculadora,command=Calculadora, text='=',bg='#DAA520',fg='black',width=18,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_igual.place(x=200,y=318)

    botao_divide = Button(janela_da_calculadora,command=botaodivide, text='/',bg='#EEE8AA',fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_divide.place(x=299,y=70)

    botao_multiplica = Button(janela_da_calculadora,command=botaomultiplica, text='*',bg='#EEE8AA',fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_multiplica.place(x=299,y=132)

    botao_menos = Button(janela_da_calculadora,command=botaomenos, text='-',bg='#EEE8AA',fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_menos.place(x=299,y=194)

    botao_mais = Button(janela_da_calculadora,command=botaomais, text='+',bg='#EEE8AA',fg='black',width=8,height=2,relief='flat',font=('Franklin Gothic Book','13','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_mais.place(x=299,y=256)

    botao_voltar = Button(janela_da_calculadora, text='<<',bg='#f1f2f3',fg='black',width=8,height=1,command=volta_janela_principal_calculadora,relief='flat',font=('Franklin Gothic Book','7','bold'),highlightthickness=0,highlightbackground='#ccc',activebackground='#ccc',highlightcolor='#ccc',cursor='hand2')
    botao_voltar.place(x=11,y=4)

def GeraSenha():
    colocar_a_senha_gerada.delete(0,'end')
    tamanho = int(caixa_combo_gerador.get())
    letras = string.ascii_letters
    numeros = '0123456789'
    simbolos = '+-*&%$#@'
    senhas = ''
    senha_verdadeira = ''
    for i in range(0,tamanho,1):
        senhas = (letras + numeros + simbolos)
        senha_verdadeira += random.choice(senhas)
    
    colocar_a_senha_gerada.insert(0,senha_verdadeira)

def esconder():
    label_player.place(x=3000,y=3000)
    label_COM.place(x=3000,y=3000)

def jogo_jokenpo():
    global label_player
    global label_COM
    jogadapc = random.randrange(1,4,1)
    jogadaplayer= caixa_combo.get()

     
    if jogadaplayer=='Pedra' and jogadapc==3:
        
        
        label_player = Label(janela_do_jokenpo,image=imagem_pedra,background='white')
        label_player.place(x=9,y=93)
        time.sleep(0.2)
        label_COM = Label(janela_do_jokenpo,image=imagem_tesoura_direita,background='white')
        label_COM.place(x=417,y=93)
        messagebox.showinfo(' ','VOCÊ ME GANHOU!!')
        esconder()
    elif jogadaplayer=='Pedra' and jogadapc==2:
        
        
        label_player = Label(janela_do_jokenpo,image=imagem_pedra,background='white')
        label_player.place(x=9,y=93)
        time.sleep(0.5)
        label_COM = Label(janela_do_jokenpo,image=imagem_papel_direita,background='white')
        label_COM.place(x=430,y=93)
        messagebox.showwarning(' ','VOCÊ PERDEU!!')
        esconder()
    
    elif jogadaplayer=='Pedra' and jogadapc==1:
        
        
        label_player = Label(janela_do_jokenpo,image=imagem_pedra,background='white')
        label_player.place(x=9,y=93)
        time.sleep(0.5)
        label_COM = Label(janela_do_jokenpo,image=imagem_pedra_direita,background='white')
        label_COM.place(x=430,y=93)
        messagebox.showinfo(' ','EMPATE!!')
        esconder()
    elif jogadaplayer=='Papel' and jogadapc==1:
        
        
        label_player = Label(janela_do_jokenpo,image=imagem_papel,background='white')
        label_player.place(x=9,y=93)
        time.sleep(0.5)
        label_COM = Label(janela_do_jokenpo,image=imagem_pedra_direita,background='white')
        label_COM.place(x=430,y=93)
        messagebox.showinfo(' ','VOCÊ ME GANHOU!!')
        esconder()
    elif jogadaplayer=='Papel' and jogadapc==3:
        
        
        label_player = Label(janela_do_jokenpo,image=imagem_papel,background='white')
        label_player.place(x=9,y=93)
        time.sleep(0.5)
        label_COM = Label(janela_do_jokenpo,image=imagem_tesoura_direita,background='white')
        label_COM.place(x=417,y=93)
        messagebox.showwarning(' ','VOCÊ PERDEU!!')
        esconder()
    elif jogadaplayer=='Papel' and jogadapc==2:
        
        
        label_player = Label(janela_do_jokenpo,image=imagem_papel,background='white')
        label_player.place(x=9,y=93)
        time.sleep(0.5)
        label_COM = Label(janela_do_jokenpo,image=imagem_papel_direita,background='white')
        label_COM.place(x=430,y=93)
        messagebox.showinfo(' ','EMPATE!!')
        esconder()
    elif jogadaplayer=='Tesoura' and jogadapc==2:
        
        
        label_player = Label(janela_do_jokenpo,image=imagem_tesoura,background='white')
        label_player.place(x=0,y=93)
        time.sleep(0.5)
        label_COM = Label(janela_do_jokenpo,image=imagem_papel_direita,background='white')
        label_COM.place(x=430,y=93)
        messagebox.showinfo(' ','VOCÊ ME GANHOU!!')
        esconder()
    elif jogadaplayer=='Tesoura' and jogadapc==1:
        
        
        label_player = Label(janela_do_jokenpo,image=imagem_tesoura,background='white')
        label_player.place(x=0,y=93)
        time.sleep(0.5)
        label_COM = Label(janela_do_jokenpo,image=imagem_pedra_direita,background='white')
        label_COM.place(x=430,y=93)
        messagebox.showwarning(' ','VOCÊ PERDEU!!')
        esconder()
    elif jogadaplayer=='Tesoura' and jogadapc==3:
        
        
        label_player = Label(janela_do_jokenpo,image=imagem_tesoura,background='white')
        label_player.place(x=0,y=93)
        time.sleep(2)
        label_COM = Label(janela_do_jokenpo,image=imagem_tesoura_direita,background='white')
        label_COM.place(x=417,y=93)
        messagebox.showinfo(' ','EMPATE!!')
        esconder()

def jogo_adivinhacao():
    jogo = int(caixa_combo_adivinhacao.get())
    escolher = random.randrange(0,6,1)

    if jogo==1:
        imagem_numero1 = PhotoImage(file='./imgs/numero 1.png')
        label_numero1 = Label(janela_da_adivinhacao,image=imagem_numero1,background='white')
        label_numero1.place(x=29,y=90)
    elif jogo==2:
        imagem_numero2 = PhotoImage(file='./imgs/numero 2.png')
        label_numero2 = Label(janela_da_adivinhacao,image=imagem_numero2,background='white')
        label_numero2.place(x=41,y=105)
    elif jogo==3:
        imagem_numero3= PhotoImage(file='./imgs/numero 3.png')
        label_numero3 = Label(janela_da_adivinhacao,image=imagem_numero3,background='white')
        label_numero3.place(x=37,y=95)
    elif jogo==4:
        imagem_numero4 = PhotoImage(file='./imgs/numero 4.png')
        label_numero4 = Label(janela_da_adivinhacao,image=imagem_numero4,background='white')
        label_numero4.place(x=30,y=103)
    elif jogo==5:
        imagem_numero5 = PhotoImage(file='./imgs/numero 5.png')
        label_numero5 = Label(janela_da_adivinhacao,image=imagem_numero5,background='white')
        label_numero5.place(x=43,y=82)
    elif jogo==0:
        imagem_numero0 = PhotoImage(file='./imgs/numero 0.png')
        label_numero0 = Label(janela_da_adivinhacao,image=imagem_numero0,background='white')
        label_numero0.place(x=60,y=110)


    if escolher==1:
        imagem_numero1_direita = PhotoImage(file='./imgs/numero 1 direita.png')
        label_numero1_direita = Label(janela_da_adivinhacao,image=imagem_numero1_direita,background='white')
        label_numero1_direita.place(x=450,y=90)
    elif escolher==2:
        imagem_numero2_direita = PhotoImage(file='./imgs/numero 2 direita.png')
        label_numero2_direita = Label(janela_da_adivinhacao,image=imagem_numero2_direita,background='white')
        label_numero2_direita.place(x=462,y=105)
    elif escolher==3:
        imagem_numero3_direita= PhotoImage(file='./imgs/numero 3 direita.png')
        label_numero3_direita = Label(janela_da_adivinhacao,image=imagem_numero3_direita,background='white')
        label_numero3_direita.place(x=458,y=95)
    elif escolher==4:
        imagem_numero4_direita = PhotoImage(file='./imgs/numero 4 direita.png')
        label_numero4_direita = Label(janela_da_adivinhacao,image=imagem_numero4_direita,background='white')
        label_numero4_direita.place(x=451,y=103)
    elif escolher==5:
        imagem_numero5_direita = PhotoImage(file='./imgs/numero 5 direita.png')
        label_numero5_direita = Label(janela_da_adivinhacao,image=imagem_numero5_direita,background='white')
        label_numero5_direita.place(x=450,y=82)
    elif escolher==0:
        imagem_numero0_direita = PhotoImage(file='./imgs/numero 0 direita.png')
        label_numero0_direita = Label(janela_da_adivinhacao,image=imagem_numero0_direita,background='white')
        label_numero0_direita.place(x=481,y=110)

    if jogo==escolher:
        messagebox.showinfo(' ','VOCÊ ME GANHOU!!')
        
    elif jogo!=escolher:
        messagebox.showwarning(' ','VOCÊ PERDEU!!')


janela = Tk()
janela.title(' ')
janela.geometry('310x300+700+390')
janela.configure(background='white')
janela.resizable(width=FALSE,height=FALSE)
janela.iconbitmap('./imgs/cubo.ico')

estilo_da_fonte_titulo = tkfont.Font(family='Bahnschrift', size=23)

estilo_da_fonte_logado = tkfont.Font(family='Bahnschrift',size=16)

estilo_da_fonte_widgets = tkfont.Font(family='Bahnschrift', size=11)

# TELA PRINCIPAL
label_login = Label(janela, text='LOGIN', font=estilo_da_fonte_titulo,background='white',anchor=NE)
label_login.place(x=9,y=5)

label_espaco = Label(janela, text= '',width=275, anchor=NW, background='black',font=('Ivy 1'), fg='black')
label_espaco.place(x=15,y=48)

label_usuario = Label(janela, text='Usuário *', font=estilo_da_fonte_widgets,background='white')
label_usuario.place(x=9,y=80)

input_user = Entry(janela, width=25, justify='left',font=('',14), highlightthickness=3, relief='solid')
input_user.place(x=13,y=110)


label_senha = Label(janela, text='Palavra passe *', font=estilo_da_fonte_widgets,background='white')
label_senha.place(x=9,y=150)

input_senha = Entry(janela, width=25, justify='left',font=('',14), highlightthickness=3, relief='solid',show='*')
input_senha.place(x=13,y=180)

botao_entrar = Button(janela, text='Cadastrar',command=CadastraUsuario,relief='flat',bg='black',fg='white',width=15,font=estilo_da_fonte_widgets)
botao_entrar.place(x=13,y=240)

botao_cadastrar = Button(janela, text='Entrar',command=LogaUsuario,relief='flat',bg='black',fg='white',width=15,font=estilo_da_fonte_widgets)
botao_cadastrar.place(x=160,y=240)


janela.mainloop()