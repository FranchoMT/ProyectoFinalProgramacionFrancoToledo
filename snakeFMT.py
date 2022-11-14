import turtle
import time
import random

posponer = 0.1


#configuracion de la ventana
tk = turtle.Screen()
tk.title("El juego de la serpiente")
tk.bgcolor("black")
tk.setup(width = 600, height = 600)
tk.tracer(0)

#cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"


#comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)
comida.direction = "stop"

#segmentos / cuerpo de la serpiente
segmentos = []


#Funciones

def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"








def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#Teclado

tk.listen()
tk.onkeypress(arriba, "w")
tk.onkeypress(abajo, "s")
tk.onkeypress(izquierda, "a")
tk.onkeypress(derecha, "d")



while True:
    tk.update()
#coliciones comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
    
    #mover el cuerpo de la serpiente:
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos [index - 1].xcord()
        y = segmentos [index - 1].ycord()
        segmentos [index].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcord()
        y = cabeza.ycord()
        segmentos[0].goto(x,y)

    mov()
    time.sleep(posponer)