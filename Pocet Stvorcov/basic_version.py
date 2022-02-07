"""
 * @name Pocet Stvorcov
 * @language Python
 * @author FekyDEV
 * @authorId 603505971507101698
 * @version 1.0.0
 * @invite sKKEyUn
 * @source https://github.com/FekyDEV/python-school/edit/main/Pocet%20Stvorcov/basic_version.py
 * @license MIT
 """

import turtle
pero = turtle.Turtle()
tabula = turtle.Screen()

def štvorec(n):
    n = int(n)
    for j in range(n): # OPAKOVAŤ N-KRÁT
        for i in range(4): # ŠTVOREC
            pero.forward(50) # DĹŽKA ŠTVORCA
            pero.left(90) # UHOL ŠTVORCA
        # PRESUN
        pero.penup()
        pero.left(180) # OTOČIŤ SA
        pero.forward(70) # DLŽKA ŠTVORCA + 20
        pero.right(180) # OTOČIŤ SA
        pero.pendown()

štvorec(3) # POČET ŠTVORCOV

tabula.mainloop() # PONECHAŤ OKNO OTVORENÉ
