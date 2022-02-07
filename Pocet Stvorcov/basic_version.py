"""
 * @name Pocet Stvorcov
 * @language Python
 * @author FekyDEV
 * @authorId 603505971507101698
 * @version 1.1.0
 * @invite sKKEyUn
 * @source https://github.com/FekyDEV/python-school/edit/main/Pocet%20Stvorcov/basic_version.py
 * @license MIT
 """

## VSTUP ##
import turtle
pero = turtle.Turtle()
tabula = turtle.Screen()

## KÓD ##
def stvorec(n):
    n = int(n) # PREMENA "N" NA ČÍSLO (STRING TO NUMBER)
    for j in range(n): # OPAKOVAŤ N-KRÁT
        # ŠTVOREC
        for i in range(4): # ŠTVOREC (OPAKOVAŤ 4-KRÁT)
            pero.forward(50) # DĹŽKA ŠTVORCA
            pero.left(90) # UHOL ŠTVORCA
        # PRESUN
        pero.penup() # ZDVIHNÚŤ PERO
        pero.left(180) # OTOČIŤ SA
        pero.forward(70) # DLŽKA ŠTVORCA + 20
        pero.right(180) # OTOČIŤ SA
        pero.pendown() # POLOŽIŤ PERO

## VÝSTUP ##
stvorec(3) # POČET ŠTVORCOV

tabula.mainloop() # PONECHAŤ OKNO OTVORENÉ
