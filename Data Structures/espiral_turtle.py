import turtle as tt
from time import sleep

tt.bgcolor('black')
tt.pensize(2)
tt.speed(10000)
tt.shape("turtle")
tt.color('blue')

sleep(0.5)

cores = [
        'red', 'magenta', 'blue', 
        'cyan', 'green', 'white', 
        'yellow'
]

for i in range(9):
    for cor in cores:
        tt.color(cor)
        tt.circle(80)

        tt.left(10)
        if i % 2 == 0:
            tt.stamp()


tt.clear()
tt.penup()
tt.forward(40)
sleep(0.3)
tt.forward(40)
sleep(0.3)
tt.forward(40)


fonte3 = ("Comic Sans", 30, "bold")
tt.write("Programação", False, "center", fonte3)