import turtle
from random import choice

pencil=turtle.Turtle()
pencil.speed(10000)
COLOURS=["red","blue","green","black"]

for i in range(180):
    c=choice(COLOURS)
    pencil.pencolor(c)
    pencil.forward(100)
    pencil.right(30)
    pencil.forward(20)
    pencil.left(60)
    pencil.forward(50)
    pencil.right(30)
    pencil.penup()
    pencil.setposition(0,0)
    pencil.pendown()
    pencil.right(2)
turtle.done()

#########################################################################################################
def valid_move_or_not(piece,currentpos,nextpos):
    pos={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
    cpos=pos.get(currentpos[0])
    tup1=(int(cpos),int(currentpos[1]))
    npos=pos.get(nextpos[0])
    tup2=(int(npos),int(nextpos[1]))
    if (piece=="Knight") or (piece=="Bishop"):
        move=[abs(tup2[0]-tup1[0]),abs(tup2[1]-tup1[1])]
        position=[abs(tup2[0]-tup1[0]),abs(tup2[1]-tup1[1])]
    if (move[0]==1 and move[1]==2 or move[0]==2 and move[1]==1) or (position[0]==position[1]):
        return True
    return False

if __name__=='__main__':
	print(valid_move_or_not("Knight","a1","a2"))