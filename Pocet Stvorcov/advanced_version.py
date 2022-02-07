import turtle
tabula = turtle.Screen()
pero = turtle.Turtle()

value = turtle.textinput("Stvorce", "zadaj hodnotu `n` (číslo)")

pero.speed(100)

if value.isnumeric():
    def hore(x):
        if x == "left":
            z = 90
        if x == "right":
            z = 270

        pero.penup()
        pero.left(90)
        pero.fd(120)
        pero.right(z)
        pero.pendown()
#
    def presun(x):
        pero.penup()
        if x == "left":
            pero.forward(70)
            pero.left(180)
        if x == "right":
            pero.left(180)
            pero.forward(70)
            pero.right(180)
            pero.pendown()

#
    def stvorec(x):


        for i in range(4):
            pero.fd(50)
            if x == "left":
                pero.left(90)
            if x == "right":
                pero.right(90)
#
    def uloha(n):
        n = int(n)
        pocet = 0

        for j in range(n):
            pocet = (pocet+1)

            if pocet < 5:
                print("n < 5")
                stvorec("left")
                presun("right")
            else:
                if pocet == 5:
                    print(".")
                    pero.penup()
                    pero.forward(70)
                    pero.pendown()
                    hore("left")
                    stvorec("right")
                    #presun("right")
                else:
                    print("..")
                    stvorec("right")
                    presun("left")
                    pero.left(180)
                    pero.pendown()

    uloha(value)
else:
    print("Chyba!")

tabula.mainloop()
