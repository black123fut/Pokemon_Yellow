from tkinter import *
import socket
import pickle
import random


def duel():
    global canvas, pika, tablero
    root = Tk()
    root.title("Pokemon Duel")
    root.geometry("400x600")

    tablero = [[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]
               ]
    canvas = Canvas(root, width=400, height=600)
    campo = PhotoImage(file="duelos\Tablero.png")
    canvas.create_image(400, 600, anchor=SE, image=campo)

    pika_img = PhotoImage(file="duelos\Pikachu.png")
    chariz_img = PhotoImage(file="duelos\Charizard.png")
    blasto_img = PhotoImage(file="duelos\Blastoise.png")
    pika = canvas.create_image(197, 392, anchor=CENTER, image=pika_img, tags="PIKACHU")


    canvas.pack()
    panel()
    root.mainloop()


def panel():
    ventana = Toplevel()
    ventana.title("Panel")
    ventana.geometry("280x280")
    ventana.config(bg="black")
    boton_right = Button(ventana, width=12, height=4, command=mueve_derecha, text="Derecha", bg="red")
    boton_right.place(x=190, y=110)

    boton_left = Button(ventana, width=12, height=4, command=mueve_izquierda, text="Izquierda", bg="red")
    boton_left.place(x=0, y=110)

    boton_top = Button(ventana, width=13, height=7, command=mueve_arriba, text="Arriba", bg="red")
    boton_top.place(x=95, y=0)

    boton_down = Button(ventana, width=13, height=7, command=mueve_abajo, text="Abajo", bg="red")
    boton_down.place(x=95, y=180)

    boton_diagonal = Button(ventana, width=13, height=4, command=mueve_diagonal, text="Diagonal", bg="red")
    boton_diagonal.place(x=95, y=110)


    ventana.mainloop()


def mueve_derecha():
    x, y = canvas.coords(pika)
    if x == 197 and y == 392:  # Tablero[4][3]
        canvas.move("PIKACHU", 54, 0)
    elif x == 143 and y == 392:  # Tablero[4][2]
        canvas.move("PIKACHU", 54, 0)
    elif x == 89 and y == 392:  # Tablero[4][1]
        canvas.move("PIKACHU", 54, 0)
    elif x == 35 and y == 392:  # Tablero[4][0]
        canvas.move("PIKACHU", 54, 0)
    elif x == 251 and y == 392:  # Tablero[4][4]
        canvas.move("PIKACHU", 54, 0)
    elif x == 305 and y == 392:  # Tablero[4][5]
        canvas.move("PIKACHU", 54, 0)  # Tablero[4][6]
    elif x == 118 and y == 321:  # Tablero[3][2]
        canvas.move("PIKACHU", 80, 0)
    elif x == 198 and y == 321:  # Tablero[3][3]
        canvas.move("PIKACHU", 78, 0)  # Tablero[3[4]
    elif x == 121 and y == 189:  # Tablero[1][2]
        canvas.move("PIKACHU", 76, 0)
    elif x == 197 and y == 189:  # Tablero[1][3]
        canvas.move("PIKACHU", 79, 0)  # Tablero[1][4]
    elif x == 50 and y == 128:  # Tablero[0][0]
        canvas.move("PIKACHU", 49, 0)
    elif x == 99 and y == 128:  # Tablero[0][1]
        canvas.move("PIKACHU", 49, 0)
    elif x == 148 and y == 128:  # Tablero[0][2]
        canvas.move("PIKACHU", 49, 0)
    elif x == 197 and y == 128:  # Tablero[0][3]  chunche amarillo
        canvas.move("PIKACHU", 49, 0)
    elif x == 246 and y == 128:  # Tablero[0][4]
        canvas.move("PIKACHU", 49, 0)
    elif x == 295 and y == 128:  # Tablero[0][5]
        canvas.move("PIKACHU", 49, 0)  # Tablero[0][6]


def mueve_izquierda():
    x, y = canvas.coords(pika)
    if x == 197 and y == 392:  # Tablero[4][3]
        canvas.move("PIKACHU", -54, 0)
    elif x == 143 and y == 392:  # Tablero[4][2]
        canvas.move("PIKACHU", -54, 0)
    elif x == 89 and y == 392:  # Tablero[4][1]
        canvas.move("PIKACHU", -54, 0)  # Tablero[4][0]
    elif x == 251 and y == 392:  # Tablero[4][4]
        canvas.move("PIKACHU", -54, 0)
    elif x == 305 and y == 392:  # Tablero[4][5]
        canvas.move("PIKACHU", -54, 0)
    elif x == 359 and y == 392:  # Tablero[4][6]
        canvas.move("PIKACHU", -54, 0)
    elif x == 276 and y == 321:  # Tablero[3][4]
        canvas.move("PIKACHU", -78, 0)
    elif x == 198 and y == 321:  # Tablero[3][3]
        canvas.move("PIKACHU", -80, 0)  # Tablero[3[2]
    elif x == 197 and y == 189:  # Tablero[1][3]
        canvas.move("PIKACHU", -76, 0)  # Tablero[1][2]
    elif x == 276 and y == 189:  # Tablero[1][4]
        canvas.move("PIKACHU", -79, 0)
    elif x == 99 and y == 128:  # Tablero[0][1]
        canvas.move("PIKACHU", -49, 0)  # Tablero[0][0]
    elif x == 148 and y == 128:  # Tablero[0][2]
        canvas.move("PIKACHU", -49, 0)
    elif x == 197 and y == 128:  # Tablero[0][3]  chunche amarillo
        canvas.move("PIKACHU", -49, 0)
    elif x == 246 and y == 128:  # Tablero[0][4]
        canvas.move("PIKACHU", -49, 0)
    elif x == 295 and y == 128:  # Tablero[0][5]
        canvas.move("PIKACHU", -49, 0)
    elif x == 344 and y == 128:  # Tablero[0][6]
        canvas.move("PIKACHU", -49, 0)


def mueve_arriba():
    x, y = canvas.coords(pika)
    if x == 35 and y == 392:  # Tablero[4][0]
        canvas.move("PIKACHU", 3, -71)
    elif x == 38 and y == 321:  # Tablero[3][0]
        canvas.move("PIKACHU", 4, -68)
    elif x == 42 and y == 253:  # Tablero[2][0]
        canvas.move("PIKACHU", 3, -64)
    elif x == 45 and y == 189:  # Tablero[1][0]
        canvas.move("PIKACHU", 5, -61)  # Tablero[0][0]
    elif x == 359 and y == 392:  # Tablero[4][6]
        canvas.move("PIKACHU", -2, -71)
    elif x == 357 and y == 321:  # Tablero[3][6]
        canvas.move("PIKACHU", -5, -68)
    elif x == 352 and y == 253:  # Tablero[2][6]
        canvas.move("PIKACHU", -4, -64)
    elif x == 348 and y == 189:  # Tablero[1][6]
        canvas.move("PIKACHU", -4, -61)  # Tablero[0][6]

    elif x == 118 and y == 321:  # Tablero[3][2]
        canvas.move("PIKACHU", 2, -68)
    elif x == 120 and y == 253:  # Tablero[2][2]
        canvas.move("PIKACHU", 1, -64)  # Tablero[1][4]

    elif x == 276 and y == 321:  # Tablero[3][4]
        canvas.move("PIKACHU", 0, -68)
    elif x == 276 and y == 253:  # Tablero[2][4]
        canvas.move("PIKACHU", 0, -64)  # Tablero[1][4]


def mueve_abajo():
    x, y = canvas.coords(pika)
    if x == 38 and y == 321:  # Tablero[3][0]
        canvas.move("PIKACHU", -3, 71)  # Tablero[4][0]
    elif x == 42 and y == 253:  # Tablero[2][0]
        canvas.move("PIKACHU", -4, 68)
    elif x == 45 and y == 189:  # Tablero[1][0]
        canvas.move("PIKACHU", -3, 64)
    elif x == 50 and y == 128:  # Tablero[0][0]
        canvas.move("PIKACHU", -5, 61)

    elif x == 357 and y == 321:  # Tablero[3][6]
        canvas.move("PIKACHU", 2, 71)
    elif x == 352 and y == 253:  # Tablero[2][6]
        canvas.move("PIKACHU", 5, 68)
    elif x == 348 and y == 189:  # Tablero[1][6]
        canvas.move("PIKACHU", 4, 64)
    elif x == 344 and y == 128:
        canvas.move("PIKACHU", 4, 61)  # Tablero[0][6]

    elif x == 121 and y == 189:  # Tablero[1][2]
        canvas.move("PIKACHU", -1, 64)
    elif x == 120 and y == 253:  # Tablero[2][2]
        canvas.move("PIKACHU", -2, 68)  # Tablero[3][2]

    elif x == 276 and y == 189:  # Tablero[3][4]
        canvas.move("PIKACHU", 0, 64)
    elif x == 276 and y == 253:  # Tablero[2][4]
        canvas.move("PIKACHU", 0, 68)  # Tablero[1][4]


def mueve_diagonal():
    x, y = canvas.coords(pika)
    if x == 251 and y == 392:
        canvas.move("PIKACHU", -53, -71)
    elif x == 197 and y == 189:
        canvas.move("PIKACHU", -49, -61)
    elif x == 359 and y == 392:
        canvas.move("PIKACHU", -83, -71)
    elif x == 276 and y == 189:
        canvas.move("PIKACHU", 68, -61)
    elif x == 121 and y == 189:
        canvas.move("PIKACHU", -71, -61)
    elif x == 35 and y == 392:
        canvas.move("PIKACHU", 83, -71)
    elif x == 118 and y == 321:
        canvas.move("PIKACHU", -83, 71)
    elif x == 198 and y == 321:
        canvas.move("PIKACHU", 53, 71)
    elif x == 276 and y == 321:
        canvas.move("PIKACHU", 83, 71)
    elif x == 50 and y == 128:
        canvas.move("PIKACHU", 71, 61)
    elif x == 148 and y == 128:
        canvas.move("PIKACHU", 49, 61)
    elif x == 344 and y == 128:
        canvas.move("PIKACHU", -68, 61)

print(duel())
