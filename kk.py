# from turtle import *
import turtle
t = turtle.Turtle()


def escalier(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)


# def carre(taille , nb):
#     for i in range(0 ,nb):
#         t.forward(taille)
#         t.left(90)
# carre(100,4)
escalier(50, 4)
turtle.done()
